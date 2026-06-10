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
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test120000_1 = "".join(luke[-107000:])
author120000_1 = "Luke"

# test 2
train120000_2 = {
    "Luke": [luke_block_60_180k],
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test120000_2 = "".join(luke[:60000])
author120000_2 = "Luke"

# test 3
train120000_3 = {
    "Luke": [luke_block_100_220k],
    "John": [john_middle_10_130k],
    "Paul": [paul_middle_10_130k]
}
test120000_3 = "".join(luke[-7000:])
author120000_3 = "Luke"

# test 4
train120000_4 = {
    "Luke": [luke[-k:]],
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_4 = "".join(luke[:107000])
author120000_4 = "Luke"

# test 5
train120000_5 = {
    "Luke": [luke_list[0]],
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_5 = "".join(luke[-50000:])
author120000_5 = "Luke"

# test 6
train120000_6 = {
    "Luke": [luke_block_60_180k],
    "John": [john_list[0]],
    "Paul": [paul_middle_10_130k]
}
test120000_6 = "".join(luke[185000:])
author120000_6 = "Luke"

# test 7
train120000_7 = {
    "Luke": [luke_block_100_220k],
    "John": [john_middle_10_130k],
    "Paul": [paul[-k:]]
}
test120000_7 = "".join(luke[50000:100000])
author120000_7 = "Luke"

# test 8
train120000_8 = {
    "Luke": [luke[-k:]],
    "John": [john_list[0]],
    "Paul": [paul_middle_10_130k]
}
test120000_8 = "".join(luke[:500])
author120000_8 = "Luke"

# test 9
train120000_9 = {
    "Luke": [luke_list[0]],     
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_9 = "".join(luke[k:])
author120000_9 = "Luke"

# test 10
train120000_10 = {
    "Luke": [luke_block_60_180k],     
    "John": [john_middle_10_130k],
    "Paul": [paul_list[0]]
}
test120000_10 = "".join(luke[190000:200000])
author120000_10 = "Luke"

# test 11
train120000_11 = {
    "Luke": [luke_block_100_220k],     
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_11 = "".join(john[:-k])
author120000_11 = "John"

# test 12
train120000_12 = {
    "Luke": [luke[-k:]],     
    "John": [john_list[0]],
    "Paul": [paul_middle_10_130k]
}
test120000_12 = "".join(john[-20000:])
author120000_12 = "John"

# test 13
train120000_13 = {
    "Luke": [luke_list[0]],     
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test120000_13 = "".join(john[10000:30000])
author120000_13 = "John"

# test 14
train120000_14 = {
    "Luke": [luke_block_60_180k],     
    "John": [john_list[0]],    # 21
    "Paul": [paul_list[0]]
}
test120000_14 = "".join(john[-500:])
author120000_14 = "John"

# test 15
train120000_15 = {
    "Luke": [luke_block_100_220k],     
    "John": [john_list[0]],
    "Paul": [paul[-k:]]
}
test120000_15 = "".join(john[-4000:])
author120000_15 = "John"

# test 16
train120000_16 = {
    "Luke": [luke[-k:]],     
    "John": [john_middle_10_130k],
    "Paul": [paul_middle_10_130k]
}
test120000_16 = "".join(john[3000:7000])
author120000_16 = "John"

# test 17
train120000_17 = {
    "Luke": [luke_list[0]],     
    "John": [john_list[0]],    # 21
    "Paul": [paul_list[0]]
}
test120000_17 = "".join(john[-25000:-12000])
author120000_17 = "John"

# test 18
train120000_18 = {
    "Luke": [luke_block_60_180k],     
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_18 = "".join(john[:15000])
author120000_18 = "John"


# test 19
train120000_19 = {
    "Luke": [luke_block_100_220k],     
    "John": [john_list[0]],    # 21
    "Paul": [paul_middle_10_130k]
}
test120000_19 = "".join(john[-16000:])
author120000_19 = "John"

# test 20
train120000_20 = {
    "Luke": [luke[-k:]],     
    "John": [john_middle_10_130k],
    "Paul": [paul_list[0]]
}
test120000_20 = "".join(john[130000:])
author120000_20 = "John"

# test 21
train120000_21 = {
    "Luke": [luke_list[0]],     
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test120000_21 = "".join(john[:4000])
author120000_21 = "John"

# test 22
train120000_22 = {
    "Luke": [luke_list[0]],     
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test120000_22 = "".join(paul[2000:4000])
author120000_22 = "Paul"

# test 23
train120000_23 = {
    "Luke": [luke_list[0]],     
    "John": [john_middle_10_130k],
    "Paul": [paul_middle_10_130k]
}
test120000_23 = "".join(paul[130000:])
author120000_23 = "Paul"

# test 24
train120000_24 = {
    "Luke": [luke_block_60_180k],     
    "John": [john_list[0]],
    "Paul": [paul[-k:]]
}
test120000_24 = "".join(paul[2000:3000])
author120000_24 = "Paul"

# test 25
train120000_25 = {
    "Luke": [luke_block_100_220k],     
    "John": [john_list[0]],
    "Paul": [paul_middle_10_130k]
}
test120000_25 = "".join(paul[:10000])
author120000_25 = "Paul"

# test 26
train120000_26 = {
    "Luke": [luke[-k:]],     
    "John": [john_middle_10_130k],
    "Paul": [paul[-k:]]
}
test120000_26 = "".join(paul[2300:14000])
author120000_26 = "Paul"

# test 27
train120000_27 = {
    "Luke": [luke_block_60_180k],     
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_27 = "".join(paul[-4000:-500])
author120000_27 = "Paul"

# test 28
train120000_28 = {
    "Luke": [luke[-k:]],     
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test120000_28 = "".join(paul[10000:15000])
author120000_28 = "Paul"

# test 29
train120000_29 = {
    "Luke": [luke_block_100_220k],     
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test120000_29 = "".join(paul[-4000:])
author120000_29 = "Paul"

# test 30
train120000_30 = {
    "Luke": [luke_block_60_180k],     
    "John": [john_middle_10_130k],
    "Paul": [paul_middle_10_130k]
}
test120000_30 = "".join(paul[500:2000])
author120000_30 = "Paul"

# test 31
train120000_31 = {
    "Luke": [luke_block_100_220k],     
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test120000_31 = "".join(paul[17000:20000])
author120000_31 = "Paul"

# test 32
train120000_32 = {
    "Luke": [luke[-k:]],     
    "John": [john_list[0]],    # 21
    "Paul": [paul_list[0]]
}
test120000_32 = "".join(paul[-500:])
author120000_32 = "Paul"

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
    (train120000_10, test120000_10, author120000_10),
    (train120000_11, test120000_11, author120000_11),
    (train120000_12, test120000_12, author120000_12),
    (train120000_13, test120000_13, author120000_13),
    (train120000_14, test120000_14, author120000_14),
    (train120000_15, test120000_15, author120000_15),
    (train120000_16, test120000_16, author120000_16),
    (train120000_17, test120000_17, author120000_17),
    (train120000_18, test120000_18, author120000_18),
    (train120000_19, test120000_19, author120000_19),
    (train120000_20, test120000_20, author120000_20),
    (train120000_21, test120000_21, author120000_21),
    (train120000_22, test120000_22, author120000_22),
    (train120000_23, test120000_23, author120000_23),
    (train120000_24, test120000_24, author120000_24),
    (train120000_25, test120000_25, author120000_25),
    (train120000_26, test120000_26, author120000_26),
    (train120000_27, test120000_27, author120000_27),
    (train120000_28, test120000_28, author120000_28),
    (train120000_29, test120000_29, author120000_29),
    (train120000_30, test120000_30, author120000_30),
    (train120000_31, test120000_31, author120000_31),
    (train120000_32, test120000_32, author120000_32)
]