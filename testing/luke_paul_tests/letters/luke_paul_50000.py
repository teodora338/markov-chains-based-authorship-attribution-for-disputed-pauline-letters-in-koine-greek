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
mark = mark
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

k = 50000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
mark_list = get_blocks(mark, k)
paul_list = get_blocks(paul, k)


# test 1
train50000_1 = {
    "Luke": [luke_list[0]],
    "Paul": [paul_list[0]]
}
test50000_1 = "".join(matthew_list[1:])
author50000_1 = "Matthew"

# test 2
train50000_2 = {
    "Luke": [luke_list[0]],
    "Paul": [paul_list[1]]
}
test50000_2 = "".join(matthew_list[0])
author50000_2 = "Matthew"

# test 3
train50000_3 = {
    "Luke": [luke_list[1]],
    "Paul": [paul_list[0]]
}
test50000_3 = "".join(matthew[-k:])
author50000_3 = "Matthew"

# test 4
train50000_4 = {
    "Luke": [luke_list[1]],
    "Paul": [paul_list[1]]
}
test50000_4 = "".join(matthew[-1000:-500])
author50000_4 = "Matthew"

# test 5
train50000_5 = {
    "Luke": [luke_list[2]],
    "Paul": [paul_list[0]]
}
test50000_5 = "".join(matthew[-4000:])
author50000_5 = "Matthew"

# test 6
train50000_6 = {
    "Luke": [luke_list[2]],
    "Paul": [paul_list[1]]
}
test50000_6 = "".join(matthew[105000:])
author50000_6 = "Matthew"

# test 7
train50000_7 = {
    "Luke": [luke_list[3]],
    "Paul": [paul_list[0]]
}
test50000_7 = "".join(luke_list[1:])
author50000_7 = "Luke"

# test 8
train50000_8 = {
    "Luke": [luke_list[3]],
    "Paul": [paul_list[1]]
}
test50000_8 = "".join(luke_list[2:4])
author50000_8 = "Luke"

# test 9
train50000_9 = {
    "Luke": [luke[-k:]],
    "Paul": [paul[-k:]]
}
test50000_9 = "".join(luke_list[:2])
author50000_9 = "Luke"

# test 10
train50000_10 = {
    "Luke": [luke[-int(k/2):] + luke[:int(k/2)]],
    "Paul": [paul[-int(k/2):] + paul[:int(k/2)]]
}
test50000_10 = "".join(luke_list[3])
author50000_10 = "Luke"


# final tuples list
tuples_list = [
    (train50000_1, test50000_1, author50000_1),
    (train50000_2, test50000_2, author50000_2),
    (train50000_3, test50000_3, author50000_3),
    (train50000_4, test50000_4, author50000_4),
    (train50000_5, test50000_5, author50000_5),
    (train50000_6, test50000_6, author50000_6),
    (train50000_7, test50000_7, author50000_7),
    (train50000_8, test50000_8, author50000_8),
    (train50000_9, test50000_9, author50000_9),
    (train50000_10, test50000_10, author50000_10)
]