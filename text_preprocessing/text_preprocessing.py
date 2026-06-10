import re
import unicodedata
from pathlib import Path
import argparse

def preprocessing (book, current_path, path_after_preprocessing):
    """Preprocessing text

    Preprocessing method:
    1. Convert .txt to string
    2. Remove words in brackets and brackets
    3. Keep only Greek letter and spaces
    4. Collapse multiple spaces
    5. Convert all letters to lower case
    6. Normalize
    7. Convert string to .txt and save"""

    # .txt to string
    with open(Path(current_path) / f"{book}.txt", "r", encoding="utf-8") as f:
        unclean_text = f.read()

    # remove words in brackets and brackets
    no_brackets = re.sub(r'\[.*?\]', '', unclean_text)

    # keep only Greek letters and spaces
    only_greek = re.sub(r"[^\u0370-\u03FF\u1F00-\u1FFF\s]", " ", no_brackets)

    # collapse multiple spaces
    no_multiple_spaces = re.sub(r"\s+", " ", only_greek).strip()

    # to lower case
    lower = no_multiple_spaces.lower()

    # normalize
    normalized = unicodedata.normalize("NFC", lower)

    # ensure path exists
    Path(path_after_preprocessing).mkdir(parents=True, exist_ok=True)

    # string to .txt
    with open(Path(path_after_preprocessing) / f"{book}.txt", "w", encoding="utf-8") as f:
        f.write(normalized)

    return normalized

def strip_diacritics(text, book, path_after_stripping):
    """Strip diacritics

    Original: ἄνθρωπος
    Stripped: ανθρωπος"""

    # Step 1: decompose characters into base + combining marks
    decomposed = unicodedata.normalize("NFD", text)
    # Step 2: filter out all combining marks (accents, breathings, subscripts)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    # Step 3: recompose to a standard form
    final = unicodedata.normalize("NFC", stripped)

    # ensure path exists
    Path(path_after_stripping).mkdir(parents=True, exist_ok=True)

    # string to .txt
    with open(Path(path_after_stripping) / f"{book}.txt", "w", encoding="utf-8") as f:
        f.write(final)

    return final

def tag(text, book, path_after_tagging, mode):
    """Add tags

        Before: "text"
        After: "^ text * " (if mode is words) or "^text*" (if mode is letters)"""

    if mode == "words":
        text = " " + text + " "

    tagged = "^" + text + "*"

    # ensure path exists
    Path(path_after_tagging).mkdir(parents=True, exist_ok=True)

    # string to .txt
    with open(Path(path_after_tagging) / f"{book}.txt", "w", encoding="utf-8") as f:
        f.write(tagged)

    return tagged

def full_pipeline(book, path, clean_path, strip_path, tag_words_path, tag_strip_letters_path, tag_letters_path):
    """Returns: clean, tagged_words, stripped, tagged_letters_stripped, tagged_letters version

    --- CLEAN ---
    ανθρωπος θεος λογος αληθεια

    --- STRIPPED ---
    ανθρωπος θεος λογος αληθεια

    --- TAGGED WORDS ---
    ^ ανθρωπος θεος * ^ λογος αληθεια *

    --- TAGGED LETTERS ---
    ^ανθρωπος θεος*^λογος αληθεια*

    --- TAGGED LETTERS STRIPPED ---
    ^ανθρωπος θεος*^λογος αληθεια*
    """

    clean = preprocessing(book, path, clean_path)
    print(f"Length of cleaned: {len(clean)}")
    tagged_words = tag(clean, book, tag_words_path, "words")
    stripped = strip_diacritics(clean, book, strip_path)
    print(f"Length of stripped: {len(stripped)}")
    tagged_letters_stripped = tag(stripped, book, tag_strip_letters_path, "letters")
    tagged_letters = tag(clean, book, tag_letters_path, "letters")

    return clean, tagged_words, stripped, tagged_letters_stripped, tagged_letters

def group_books(book_list, path_in, path_out, mode):
    """Join books from same group in one file"""
    group = str()

    for book in book_list:
        with open(Path(path_in) / f"{book}.txt", "r", encoding="utf-8") as f:
            text = f.read()
        group+=text
        if mode == "words":
            group+=" "      # to separate books with " " (if states = words)

    if group and group[-1] == " ":
        group = group[:-1]      # to avoid extra " " at the end

    # ensure path exists
    Path(path_out).parent.mkdir(parents=True, exist_ok=True)

    # string to .txt
    with open(path_out, "w", encoding="utf-8") as f:
        f.write(group)

    return group

def group_cross_validation(book_list, path_in, path_out, mode):
    """Join books from same group in one file, except one of the books in order to perform cross validation later"""
    list_of_grouped = list()

    for omitted_book in book_list:
        group = list()
        for book in book_list:
            if book != omitted_book:
                group.append(book)

        unique_out_path = Path(path_out) / f"omitted_{omitted_book}.txt"

        omitted_group = group_books(group, path_in, unique_out_path, mode)
        print(f"Omitted: {omitted_book} - length: {len(omitted_group)}")
        list_of_grouped.append(omitted_group)

    return list_of_grouped

def main(base_dir=".", output_dir="output"):
    """Calls preprocessing text functions"""
    # groups and books
    groups = {
        "undisputed": (
            "1Corinthians", "1Thessalonians", "2Corinthians",
            "Galatians", "Philemon", "Philippians", "Romans"
        ),
        "disputed": (
            "1Timothy", "2Thessalonians", "2Timothy",
            "Colossians", "Ephesians", "Hebrews", "Titus"
        ),
        "notpaul": (
            "1John", "1Peter", "2John", "2Peter", "3John",
            "Acts", "Jacob", "John", "Jude", "Luke", "Mark",
            "Matthew", "Revelation"
        )
    }

    # define preprocessing steps and their folders
    preprocess_configs = {
        "clean": {"subdir": "clean", "mode": "words"},
        "stripped": {"subdir": "stripped", "mode": "words"},
        "tagged_words": {"subdir": "tagged/words", "mode": "words"},
        "tagged_letters": {"subdir": "tagged/letters", "mode": "letters"},
        "tagged_letters_stripped": {"subdir": "tagged/letters_stripped", "mode": "letters"},
    }

    # input dirs before preprocessing
    input_dirs = {
        "undisputed": Path(base_dir) / "notnormalized/undisputed",
        "disputed": Path(base_dir) / "notnormalized/disputed",
        "notpaul": Path(base_dir) / "notnormalized/notpaul"
    }

    # 1. Run preprocessing for each book (make every version of book)
    for group, books in groups.items(): # iterate through evey group
        for book in books:  # iterate through every book in that group
            print(f"Book: {book}")
            cl, tg_w, st, tg_l_s, tg_l = full_pipeline(
                book,
                input_dirs[group],
                Path(output_dir) / "clean" / group,
                Path(output_dir) / "stripped" / group,
                Path(output_dir) / "tagged/words" / group,
                Path(output_dir) / "tagged/letters_stripped" / group,
                Path(output_dir) / "tagged/letters" / group
            )

    # 2. Group books by category (
    for name, cfg in preprocess_configs.items():    # iterate though every version configuration
        for group, books in groups.items():     # iterate trough every group
            in_path = Path(output_dir) / cfg["subdir"] / group
            out_path = Path(output_dir) / "grouped" / cfg["subdir"] / f"{group}.txt"
            gr = group_books(books, in_path, out_path, cfg["mode"])
            print(f"Length of group {group} in config {name}: {len(gr)}")

    # 3. Cross-validation only for undisputed
    for name, cfg in preprocess_configs.items():    # iterate trough every version configuration
        group_cross_validation(
            groups["undisputed"],
            Path(output_dir) / cfg["subdir"] / "undisputed",
            Path(output_dir) / "cross_validation_undisputed" / cfg["subdir"],
            cfg["mode"]
        )

    # 4. Full NT grouping
    for name, cfg in preprocess_configs.items():    # iterate through configs
        path = Path(output_dir) / "grouped" / cfg["subdir"]
        out_path = Path(output_dir) / "full_new_testament" / f"{name}.txt"
        nt = group_books(list(groups.keys()), path, out_path, cfg["mode"])
        print(f"Created full NT {name} version with length: {len(nt)}")

def count_words(base_dir=".", input_dir="output"):
    """Counting words in each clean version of book"""
    # groups and books
    groups = {
        "undisputed": (
            "1Corinthians", "1Thessalonians", "2Corinthians",
            "Galatians", "Philemon", "Philippians", "Romans"
        ),
        "disputed": (
            "1Timothy", "2Thessalonians", "2Timothy",
            "Colossians", "Ephesians", "Hebrews", "Titus"
        ),
        "notpaul": (
            "1John", "1Peter", "2John", "2Peter", "3John",
            "Acts", "Jacob", "John", "Jude", "Luke", "Mark",
            "Matthew", "Revelation"
        )
    }

    # printing number of words in each NT book
    for group, books in groups.items():  # iterate through evey group
        for book in books:  # iterate through every book in that group
            print(f"Book: {book}")

            with open(Path(input_dir) / "clean" / group / f"{book}.txt", "r", encoding="utf-8") as f:
                book_content = f.read()

            print(f"Number of words:")
            print(len(book_content.split()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_dir", default=".")
    parser.add_argument("--output", default="output")
    args = parser.parse_args()

    main(base_dir=args.base_dir, output_dir=args.output)
    count_words()