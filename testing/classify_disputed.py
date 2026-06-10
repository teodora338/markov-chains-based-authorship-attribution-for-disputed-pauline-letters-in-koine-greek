import math
from collections import defaultdict, Counter
from nltk.util import ngrams

from test_cases.test_cases_stripped.authors5 import authors5_50000_stripped
from test_cases.test_cases_stripped.authors4 import authors4_70000_stripped, authors4_90000_stripped
from test_cases.test_cases_stripped.authors3 import authors3_120000_stripped

from test_cases.test_cases_letters.authors5 import authors5_50000_letters
from test_cases.test_cases_letters.authors4 import authors4_90000_letters, authors4_70000_letters
from test_cases.test_cases_letters.authors3 import authors3_120000_letters


from disputed_letters import *

from luke_paul_tests.letters import luke_paul_50000, luke_paul_70000, luke_paul_90000, luke_paul_120000
from luke_paul_tests.stripped import luke_paul_50000_stripped, luke_paul_70000_stripped, luke_paul_90000_stripped, luke_paul_120000_stripped


dsp_list = disputed_names_pairs


def tokenize(text, mode):
    """Returns tokens list from given text

    Example: "text tool"
    - if mode == "letters": ["t", "e", "x", "t", " ", "t", "o", "o", "l"]
    - if mode == "words": ["text", "tool"]"""

    if mode == "words":
        tokens = text.split(" ")
    else:
        tokens = list(text)

    return tokens


def create_tuples(tokens_list):
    n_grams = ngrams(tokens_list, 2)
    n_grams = list(n_grams)

    return list(n_grams)


def replace_rare_tokens(tokens, freqs, limit):
    rare_tokens = {k for k, v in freqs.items() if (v <= limit and k != "^" and k != "*")}

    # Replace rare tokens in sequence
    new_tokens = ["?" if token in rare_tokens else token for token in tokens]

    return new_tokens


class PrepareTexts:
    def __init__(self, texts, mode, replace_rare=False, limit_rare=0):
        self.texts = texts
        self.mode = mode
        self.replace_rare = replace_rare  # boolean for whether to put "?" instead of rare tokens
        self.limit_rare = limit_rare  # max frequency considered rare

        self.tokens_lists = list()  # list of lists of tokenized text of the author
        self.tuples_lists = list()  # list of lists of tuples version of the text of the author
        self.tokens_grouped = list()  # list of all tokens from authors text

        if self.replace_rare:  # if the boolean is True (we want to replace rare words (but not tags) in train data with "?")
            self.replace_rare_func()
        else:
            self.prepare()

    def prepare(self):
        for text in self.texts:
            tokens = tokenize(text, self.mode)
            self.tokens_lists.append(tokens)
            self.tokens_grouped += tokens

            tuples = create_tuples(tokens)
            self.tuples_lists.append(tuples)

    def replace_rare_func(self):
        temp_tokens_lists = list()

        for text in self.texts:
            tokens = tokenize(text, self.mode)
            temp_tokens_lists.append(tokens)
            self.tokens_grouped += tokens

        freqs = Counter(self.tokens_grouped)
        self.tokens_grouped.clear()  # to add updated tokens

        for i in range(len(self.texts)):
            new_tokens = replace_rare_tokens(temp_tokens_lists[i], freqs, self.limit_rare)
            self.tokens_lists.append(new_tokens)
            self.tokens_grouped += new_tokens

            tuples = create_tuples(new_tokens)
            self.tuples_lists.append(tuples)

    def get_prepared(self):
        return self.tokens_grouped, self.tokens_lists, self.tuples_lists


# Markov Chain model class
class MarkovChain:
    def __init__(self, author, texts, mode, add_qm=False, replace_rare=False, rare_limit=0):
        self.author = author
        self.texts = texts
        self.mode = mode  # do we consider a letter as state or a word as state
        if mode == "words":
            print(f"Number of words for author {self.author}: {len(tokenize(self.texts[0], self.mode))}")
        self.add_qm = add_qm  # do we want to add "?" in Rx just in case of unseen state shows up in test set

        # get grouped tokens, token lists per text and tuples per text
        preparation = PrepareTexts(self.texts, self.mode, replace_rare, rare_limit)
        self.grouped_tokens, self.tokens_lists, self.tuples_lists = preparation.get_prepared()
        del preparation  # destroy object to free memory
        self.num_tokens = len(self.grouped_tokens)

        # dicts for counting transitions and frequencies
        self.transition_counts = defaultdict(Counter)
        self.history_counts = Counter()
        self.frequencies = Counter(self.grouped_tokens)

        # dicts to cache probs
        self.transition_probs = defaultdict(dict)
        self.marginal_probs = defaultdict(float)
        self.log_transition_probs = defaultdict(dict)

        # prepare Rx
        # Koine Greek alphabet with diacritics + [" ", "^", "*"]
        self.koine_greek_diacritics = "αβγδεζηθικλμνξοπρσςτυφχψωάὰᾶἀἁἄἂἆἅἃἇᾳᾴᾲᾷᾀᾁᾄᾂᾆᾅᾃᾇέὲἐἑἔἒἕἓήὴῆἠἡἤἢἦἥἣἧῃῄῂῇᾐᾑᾔᾒᾖᾕᾓᾗίὶῖἰἱἴἲἶἵἳἷϊΐῒῗόὸὀὁὄὂὅὃύὺῦὐὑὔὒὖὕὓὗϋΰῢῧώὼῶὠὡὤὢὦὥὣὧῳῴῲῷᾠᾡᾤᾢᾦᾥᾣᾧῤῥ ^*"

        # Koine Greek alphabet + [" ", "^", "*"]
        self.koine_greek_alphabet = "αβγδεζηθικλμνξοπρσςτυφχψω ^*"

        if self.mode == "words":
            self.Rx = list(set(self.grouped_tokens))  # all possible states in train set

            if add_qm and "?" not in self.Rx:  # if there is no "?" in Rx and we want to add it
                self.Rx.append("?")
        elif self.mode == "letters":
            self.Rx = self.koine_greek_diacritics  # with diacritics
        elif self.mode == "stripped":
            self.Rx = self.koine_greek_alphabet  # without diacritics

        # train author model (count and calculate probs)
        self.train()

    # calculate transitions and how times a state showed up as history
    def train(self):
        for tuples_list in self.tuples_lists:
            for from_state, to_state in tuples_list:  # add transitions for text
                self.history_counts[from_state] += 1
                self.transition_counts[from_state][to_state] += 1

        # calculate probs
        for from_state, to_states in self.transition_counts.items():
            # calculate transition probs
            for to_state in to_states.keys():
                self.transition_probs[from_state][to_state] = self.transition_counts[from_state][to_state] / \
                                                              self.history_counts[from_state]

        for state in self.Rx:
            # calculate marginal prob
            self.marginal_probs[state] = self.frequencies[state] / self.num_tokens

    def check_new_token(self, token):
        if token not in self.Rx:
            return "?"
        else:
            return token

    # get specific transition probability
    def get_transition_prob(self, from_token, to_token):
        from_state = self.check_new_token(from_token)
        to_state = self.check_new_token(to_token)

        return self.transition_probs.get(from_state, {}).get(to_state, 0)  # return 0 id it doesnt exist

    # get marginal prob for state
    def get_marginal_prob(self, state):
        st = self.check_new_token(state)

        return self.marginal_probs.get(st, 0)

    # calculate log probability for transition
    def calculate_log_transition_prob(self, from_state, to_state):
        prob = self.get_transition_prob(from_state, to_state)
        if prob == 0.0:
            return float("-inf")
        return math.log(prob)  # natural log

    # get specific transition log probability
    def get_log_transition_prob(self, from_token, to_token):
        from_state = self.check_new_token(from_token)
        to_state = self.check_new_token(to_token)

        if from_state in self.log_transition_probs.keys():
            if to_state in self.log_transition_probs[from_state].keys():
                return self.log_transition_probs[from_state][to_state]
            else:
                self.log_transition_probs[from_state][to_state] = self.calculate_log_transition_prob(from_state,
                                                                                                     to_state)
        else:
            self.log_transition_probs[from_state][to_state] = self.calculate_log_transition_prob(from_state, to_state)

        return self.log_transition_probs[from_state][to_state]

    # calculate and return log-likelihood, P(text | author = author)
    def text_log_likelihood(self, tuples):
        log_likelihood = 0.0
        counter_not_found = 0

        for from_state, to_state in tuples:
            transition_log_prob = self.get_log_transition_prob(from_state, to_state)

            if transition_log_prob == float("-inf"):
                counter_not_found += 1
                continue  # ignore degenerate cases
            else:
                log_likelihood += transition_log_prob

        percent = (counter_not_found / len(tuples)) * 100

        print(f"Percentage of not found transitions for author {self.author}: {percent}%")

        return log_likelihood


class TextLikelihoods:
    def __init__(self, text_name, tokens, authors_data, mode, ranks_dict, add_qm=False, replace_rare=False, rare_limit=0):
        self.text_name = text_name
        self.authors_data = authors_data
        self.mode = mode
        self.add_qm = add_qm
        self.replace_rare = replace_rare
        self.rare_limit = rare_limit

        self.markov_models = defaultdict()
        self.sorted_likelihoods = list()
        self.authors_data = authors_data
        self.tokens = tokens
        self.tuples = create_tuples(self.tokens)

        self.ranks_dict = ranks_dict

        self.train()

    def train(self):
        likelihoods = defaultdict(float)
        for author, texts in self.authors_data.items():
            self.markov_models[author] = MarkovChain(author, texts, self.mode, self.add_qm, self.replace_rare,
                                                     self.rare_limit)
            likelihoods[author] = self.markov_models[author].text_log_likelihood(self.tuples)

        self.sorted_likelihoods = sorted(likelihoods.items(), key=lambda x: x[1], reverse=True)

    def get_sorted_likelihoods(self):
        print(self.sorted_likelihoods)

        return self.sorted_likelihoods

    def predict(self):
        print(f"{self.sorted_likelihoods[0][0]}, {self.sorted_likelihoods[0][1]}")

        return self.sorted_likelihoods[0][0]

    def get_rank_of_true_author(self, auth):
        ranked_authors = [auth for auth, likelihood in self.sorted_likelihoods]

        return ranked_authors.index(auth)

    def add_author_ranks(self):
        for i in range(len(self.sorted_likelihoods)):
            self.ranks_dict[self.sorted_likelihoods[i][0]].append(i)

        return self.ranks_dict


def get_blocks(text, block_size):
    start = 0
    end = block_size

    block_list = list()

    while end <= len(text):
        block_list.append(text[start:end])
        start += block_size
        end += block_size

    return block_list

def average_author_rank(ranks_dict):
    for auth, ranks_list in ranks_dict.items():
        print(f"{auth} - {sum(ranks_list)/32}")


def experiment(num_authors, train_lengths, test_cases, mode, test_text, add_qm=False, replace_rare=False, rare_limit=0):
    print("===")
    print(f"Testing with {num_authors} authors and {train_lengths} chars per author for train set - Mode: {mode}")
    author_ranks = defaultdict(list)  # ranks each author gets
    real_and_predicted_counts = defaultdict(Counter)  # tuples in format (real, predicted)
    rank_counts = Counter()  # counting how many times the real author was ranked in that position

    tests = test_cases
    predicted_counts = Counter()

    ranks_dict = defaultdict(list)

    counter = 1
    for test in tests:
        print(f"TEST CASE {counter}")
        counter += 1

        dct = test[0]
        tkns = tokenize(test_text, mode)

        tl = TextLikelihoods(None, tkns, dct, mode, ranks_dict)  # construct and train model
        print("Predicted author:")
        predicted = tl.predict()  # predicted author
        print(predicted)
        predicted_counts[predicted] += 1
        print("Sorted ranks:")
        sorted_likelihoods = tl.get_sorted_likelihoods()  # authors sorted per likelihood
        rd = tl.add_author_ranks()
        print("--------------------")

    print("------------------------------------------------------------")
    print(predicted_counts)
    print(ranks_dict)
    average_author_rank(ranks_dict)


def classify_disputed(args_list):
    for disputed_text, text_name in dsp_list:
        print("===========================")
        print(f"Testing test: {text_name}")
        print("===========================")
        for args in args_list:
            experiment(args[0], args[1], args[2], args[3], disputed_text)


if __name__ == "__main__":
    args = [
        [5, 50000, authors5_50000_stripped.tuples_list, "stripped"],
        [4, 70000, authors4_70000_stripped.tuples_list, "stripped"],
        [4, 90000, authors4_90000_stripped.tuples_list, "stripped"],
        [3, 120000, authors3_120000_stripped.tuples_list, "stripped"],
        [5, 50000, authors5_50000_letters.tuples_list, "letters"],
        [4, 70000, authors4_70000_letters.tuples_list, "letters"],
        [4, 90000, authors4_90000_letters.tuples_list, "letters"],
        [3, 120000, authors3_120000_letters.tuples_list, "letters"]
    ]

    args_Luke_Paul = [
        [5, 50000, luke_paul_50000_stripped.tuples_list, "stripped"],
        [4, 70000, luke_paul_70000_stripped.tuples_list, "stripped"],
        [4, 90000, luke_paul_90000_stripped.tuples_list, "stripped"],
        [3, 120000, luke_paul_120000_stripped.tuples_list, "stripped"],
        [5, 50000, luke_paul_50000.tuples_list, "letters"],
        [4, 70000, luke_paul_70000.tuples_list, "letters"],
        [4, 90000, luke_paul_90000.tuples_list, "letters"],
        [3, 120000, luke_paul_120000.tuples_list, "letters"]
    ]

    classify_disputed(args_Luke_Paul)
    classify_disputed(args)
