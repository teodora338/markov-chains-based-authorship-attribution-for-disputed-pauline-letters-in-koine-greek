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

k = 120000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
paul_list = get_blocks(paul, k)

luke_block_60_180k = luke[60000:180000]
luke_block_100_220k = luke[100000:220000]
john_middle_10_130k = john[10000:130000]
paul_middle_10_130k = paul[10000:130000]


# test 1
train120000_1 = {
    "Luke": [luke_list[0]],
    "Paul": [paul_list[0]]
}
test120000_1 = "".join(luke[-107000:])
author120000_1 = "Luke"

# test 2
train120000_2 = {
    "Luke": [luke_list[0]],
    "Paul": [paul[-k:]]
}
test120000_2 = "".join(luke[:60000])
author120000_2 = "Luke"

# test 3
train120000_3 = {
    "Luke": [luke[-k:]],
    "Paul": [paul_list[0]]
}
test120000_3 = "".join(luke[-7000:])
author120000_3 = "Luke"

# test 4
train120000_4 = {
    "Luke": [luke[-k:]],
    "Paul": [paul[-k:]]
}
test120000_4 = "".join(luke[:107000])
author120000_4 = "Luke"

# test 5
train120000_5 = {
    "Luke": [luke[-int(k/2):] + luke[:int(k/2)]],
    "Paul": [paul[-int(k/2):] + paul[:int(k/2)]]
}
test120000_5 = "".join(luke[-50000:])
author120000_5 = "Luke"

# test 6
train120000_6 = {
    "Luke": [luke[114000-int(k/2):114000+int(k/2)]],
    "Paul": [paul[70000-int(k/2):70000+int(k/2)]]
}
test120000_6 = "".join(luke[185000:])
author120000_6 = "Luke"

# test 7
train120000_7 = {
    "Luke": [luke[10000:10000+k]],
    "Paul": [paul[10000:10000+k]]
}
test120000_7 = "".join(luke[50000:100000])
author120000_7 = "Luke"

# test 8
train120000_8 = {
    "Luke": [luke[-k-10000:-10000]],
    "Paul": [paul[-k-10000:-10000]]
}
test120000_8 = "".join(luke[:500])
author120000_8 = "Luke"

# test 9
train120000_9 = {
    "Luke": [luke[20000:20000+k]],
    "Paul": [paul[20000:20000+k]]
}
test120000_9 = "".join(luke[k:])
author120000_9 = "Luke"

# test 10
train120000_10 = {
    "Luke": [luke[-k-20000:-20000]],
    "Paul": [paul[-k-20000:-20000]]
}
test120000_10 = "".join(luke[190000:200000])
author120000_10 = "Luke"



# final tuples list
tuples_list = [
    (train120000_1, test120000_1, author120000_1),
    (train120000_2, test120000_2, author120000_2),
    (train120000_3, test120000_3, author120000_3),
    (train120000_4, test120000_4, author120000_4),
    (train120000_5, test120000_5, author120000_5),
    (train120000_6, test120000_6, author120000_6),
    (train120000_7, test120000_7, author120000_7),
    (train120000_8, test120000_8, author120000_8),
    (train120000_9, test120000_9, author120000_9),
    (train120000_10, test120000_10, author120000_10)
]