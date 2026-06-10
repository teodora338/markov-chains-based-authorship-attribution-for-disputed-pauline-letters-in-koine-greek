from new_testament_texts.stripped_texts import P_stripped, NP_stripped

luke = "^" + NP_stripped.luke + "*"
acts = "^" + NP_stripped.acts + "*"
john = "^" + NP_stripped.john + "*"
john1 = "^" + NP_stripped.john1 + "*"
john2 = "^" + NP_stripped.john2 + "*"
john3 = "^" + NP_stripped.john3 + "*"
revelation = "^" + NP_stripped.revelation + "*"
matthew = "^" + NP_stripped.matthew + "*"
mark = "^" + NP_stripped.mark + "*"
peter1 = "^" + NP_stripped.peter1 + "*"
peter2 = "^" + NP_stripped.peter2 + "*"
jacob = "^" + NP_stripped.jacob + "*"
romans = "^" + P_stripped.romans + "*"
corinthians1 = "^" + P_stripped.corinthians1 + "*"
corinthians2 = "^" + P_stripped.corinthians2 + "*"
galatians = "^" + P_stripped.galatians + "*"
philemon = "^" + P_stripped.philemon + "*"
thessalonians1 = "^" + P_stripped.thessalonians1 + "*"
philippians = "^" + P_stripped.philippians + "*"

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

k = 70000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
paul_list = get_blocks(paul, k)


# test 1
train70000_1 = {
    "Luke": [luke_list[0]],
    "Paul": [paul_list[0]]
}
test70000_1 = "".join(matthew[-37000:])
author70000_1 = "Matthew"

# test 2
train70000_2 = {
    "Luke": [luke_list[0]],
    "Paul": [paul_list[1]]
}
test70000_2 = "".join(matthew[:37000])
author70000_2 = "Matthew"

# test 3
train70000_3 = {
    "Luke": [luke_list[1]],
    "Paul": [paul_list[0]]
}
test70000_3 = "".join(matthew[-27000:])
author70000_3 = "Matthew"

# test 4
train70000_4 = {
    "Luke": [luke_list[1]],
    "Paul": [paul_list[1]]
}
test70000_4 = "".join(matthew[1000:16000])
author70000_4 = "Matthew"

# test 5
train70000_5 = {
    "Luke": [luke_list[2]],
    "Paul": [paul_list[0]]
}
test70000_5 = "".join(matthew[3000:10000])
author70000_5 = "Matthew"

# test 6
train70000_6 = {
    "Luke": [luke_list[2]],
    "Paul": [paul_list[1]]
}
test70000_6 = "".join(matthew[-4000:-3000])
author70000_6 = "Matthew"

# test 7
train70000_7 = {
    "Luke": [luke[-k:]],
    "Paul": [paul[-k:]]
}
test70000_7 = "".join(matthew[-500:])
author70000_7 = "Matthew"

# test 8
train70000_8 = {
    "Luke": [luke[-int(k/2):] + luke[:int(k/2)]],
    "Paul": [paul[-int(k/2):] + paul[:int(k/2)]]
}
test70000_8 = "".join(matthew[:500])
author70000_8 = "Matthew"

# test 9
train70000_9 = {
    "Luke": [luke[35000:35000+k]],
    "Paul": [paul[35000:35000+k]]
}
test70000_9 = "".join(luke_list[2])
author70000_9 = "Luke"

# test 10
train70000_10 = {
    "Luke": [luke[35000:35000+int(k/2)], luke[-int(k/2):]],
    "Paul": [paul[35000:35000+int(k/2)], paul[-int(k/2):]]
}
test70000_10 = "".join(luke_list[0])
author70000_10 = "Luke"


# final tuples list
tuples_list = [
    (train70000_1, test70000_1, author70000_1),
    (train70000_2, test70000_2, author70000_2),
    (train70000_3, test70000_3, author70000_3),
    (train70000_4, test70000_4, author70000_4),
    (train70000_5, test70000_5, author70000_5),
    (train70000_6, test70000_6, author70000_6),
    (train70000_7, test70000_7, author70000_7),
    (train70000_8, test70000_8, author70000_8),
    (train70000_9, test70000_9, author70000_9),
    (train70000_10, test70000_10, author70000_10)
]