from new_testament_texts.letter_texts import P_letters, NP_letters

luke = "^" + NP_letters.luke + "*"
acts = "^" + NP_letters.acts + "*"
john = "^" + NP_letters.john + "*"
john1 = "^" + NP_letters.john1 + "*"
john2 = "^" + NP_letters.john2 + "*"
john3 = "^" + NP_letters.john3 + "*"
revelation = "^" + NP_letters.revelation + "*"
matthew = "^" + NP_letters.matthew + "*"
mark = "^" + NP_letters.mark + "*"
peter1 = "^" + NP_letters.peter1 + "*"
peter2 = "^" + NP_letters.peter2 + "*"
jacob = "^" + NP_letters.jacob + "*"
romans = "^" + P_letters.romans + "*"
corinthians1 = "^" + P_letters.corinthians1 + "*"
corinthians2 = "^" + P_letters.corinthians2 + "*"
galatians = "^" + P_letters.galatians + "*"
philemon = "^" + P_letters.philemon + "*"
thessalonians1 = "^" + P_letters.thessalonians1 + "*"
philippians = "^" + P_letters.philippians + "*"

luke = luke + acts
john = john + john1 + john2 + john3 + revelation
matthew = matthew
paul = romans + corinthians1 + corinthians2 + philippians + philemon + thessalonians1 + galatians

def get_blocks(text, block_size):
    start = 0
    end = block_size

    block_list = list()

    while end <= len(text):
        block_list.append(text[start:end])
        start += block_size
        end += block_size

    return block_list

k = 90000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
paul_list = get_blocks(paul, k)


# test 1
train90000_1 = {
    "Luke": [luke_list[0]],
    "Paul": [paul_list[0]]
}
test90000_1 = "".join(matthew[-17000:])
author90000_1 = "Matthew"

# test 2
train90000_2 = {
    "Luke": [luke_list[0]],
    "Paul": [paul[-k:]]
}
test90000_2 = "".join(matthew[:17000])
author90000_2 = "Matthew"

# test 3
train90000_3 = {
    "Luke": [luke_list[1]],
    "Paul": [paul_list[0]]
}
test90000_3 = "".join(matthew[-7000:])
author90000_3 = "Matthew"

# test 4
train90000_4 = {
    "Luke": [luke_list[1]],
    "Paul": [paul[-k:]]
}
test90000_4 = "".join(matthew[1000:16000])
author90000_4 = "Matthew"

# test 5
train90000_5 = {
    "Luke": [luke[-k:]],
    "Paul": [paul_list[0]]
}
test90000_5 = "".join(matthew[300:1000])
author90000_5 = "Matthew"

# test 6
train90000_6 = {
    "Luke": [luke[-k:]],
    "Paul": [paul[-k:]]
}
test90000_6 = "".join(matthew[-4000:-3000])
author90000_6 = "Matthew"

# test 7
train90000_7 = {
    "Luke": [luke[-int(k/2):] + luke[:int(k/2)]],
    "Paul": [paul[-int(k/2):] + paul[:int(k/2)]]
}
test90000_7 = "".join(matthew[-500:])
author90000_7 = "Matthew"

# test 8
train90000_8 = {
    "Luke": [luke[45000:45000+k]],
    "Paul": [paul[45000:45000+k]]
}
test90000_8 = "".join(matthew[:500])
author90000_8 = "Matthew"

# test 9
train90000_9 = {
    "Luke": [luke[45000+k:45000+2*k]],
    "Paul": [paul[45000:45000+k]]
}
test90000_9 = "".join(luke_list[1])
author90000_9 = "Luke"

# test 10
train90000_10 = {
    "Luke": [luke_list[0][:30000], luke_list[1][:30000], luke[180000:180000+30000]],
    "Paul": [paul_list[0][:45000], paul[90000:90000+int(k/2)]]
}
test90000_10 = "".join(luke_list[0])
author90000_10 = "Luke"



# final tuples list
tuples_list = [
    (train90000_1, test90000_1, author90000_1),
    (train90000_2, test90000_2, author90000_2),
    (train90000_3, test90000_3, author90000_3),
    (train90000_4, test90000_4, author90000_4),
    (train90000_5, test90000_5, author90000_5),
    (train90000_6, test90000_6, author90000_6),
    (train90000_7, test90000_7, author90000_7),
    (train90000_8, test90000_8, author90000_8),
    (train90000_9, test90000_9, author90000_9),
    (train90000_10, test90000_10, author90000_10)
]