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

k = 150000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)

luke_block_30_180k = luke[30000:180000]
luke_block_50_200k = luke[50000:200000]
john_middle_5_155k = john[5000:155000]
john_middle_2_152k = john[200:152000]

# test 1
train150000_1 = {
    "Luke": [luke_list[0]],
    "John": [john_list[0]]
}
test150000_1 = "".join(luke[k:])
author150000_1 = "Luke"

# test 2
train150000_2 = {
    "Luke": [luke[-k:]],
    "John": [john[-k:]]
}
test150000_2 = "".join(luke[:60000])
author150000_2 = "Luke"

# test 3
train150000_3 = {
    "Luke": [luke_block_50_200k],
    "John": [john_middle_5_155k]
}
test150000_3 = "".join(luke[-7000:])
author150000_3 = "Luke"

# test 4
train150000_4 = {
    "Luke": [luke[-k:]],
    "John": [john_middle_2_152k]
}
test150000_4 = "".join(luke[:-k])
author150000_4 = "Luke"

# test 5
train150000_5 = {
    "Luke": [luke_block_30_180k],
    "John": [john[-k:]]
}
test150000_5 = "".join(luke[:30000])
author150000_5 = "Luke"

# test 6
train150000_6 = {
    "Luke": [luke_block_50_200k],
    "John": [john_list[0]]
}
test150000_6 = "".join(luke[220000:])
author150000_6 = "Luke"

# test 7
train150000_7 = {
    "Luke": [luke_block_50_200k],
    "John": [john_middle_5_155k]
}
test150000_7 = "".join(luke[:50000])
author150000_7 = "Luke"

# test 8
train150000_8 = {
    "Luke": [luke[-k:]],
    "John": [john_list[0]]
}
test150000_8 = "".join(luke[:500])
author150000_8 = "Luke"

# test 9
train150000_9 = {
    "Luke": [luke_list[0]],          
    "John": [john[-k:]]
}
test150000_9 = "".join(luke[210000:])
author150000_9 = "Luke"

# test 10
train150000_10 = {
    "Luke": [luke_block_30_180k],          
    "John": [john_middle_2_152k]
}
test150000_10 = "".join(luke[180000:200000])
author150000_10 = "Luke"

# test 11
train150000_11 = {
    "Luke": [luke_block_50_200k],          
    "John": [john[-k:]]
}
test150000_11 = "".join(luke[40000:50000])
author150000_11 = "Luke"

# test 12
train150000_12 = {
    "Luke": [luke[-k:]],          
    "John": [john_middle_5_155k]
}
test150000_12 = "".join(luke[:-k])
author150000_12 = "Luke"

# test 13
train150000_13 = {
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
}
test150000_13 = "".join(luke[170000:190000])
author150000_13 = "Luke"

# test 14
train150000_14 = {
    "Luke": [luke_block_30_180k],          
    "John": [john_list[0]]
}
test150000_14 = "".join(luke[-500:])
author150000_14 = "Luke"

# test 15
train150000_15 = {
    "Luke": [luke_block_50_200k],          
    "John": [john_list[0]]
}
test150000_15 = "".join(luke[-4000:])
author150000_15 = "Luke"

# test 16
train150000_16 = {
    "Luke": [luke[-k:]],          
    "John": [john_middle_5_155k]
}
test150000_16 = "".join(luke[3000:7000])
author150000_16 = "Luke"

# test 17
train150000_17 = {
    "Luke": [luke_list[0]],          
    "John": [john_middle_5_155k]
}
test150000_17 = "".join(john[3000:5000])
author150000_17 = "John"

# test 18
train150000_18 = {
    "Luke": [luke_block_30_180k],          
    "John": [john[-k:]]
}
test150000_18 = "".join(john[:2222])
author150000_18 = "John"


# test 19
train150000_19 = {
    "Luke": [luke_block_50_200k],          
    "John": [john_list[0]]
}
test150000_19 = "".join(john[-1300:])
author150000_19 = "John"

# test 20
train150000_20 = {
    "Luke": [luke[-k:]],          
    "John": [john_middle_5_155k]
}
test150000_20 = "".join(john[155000:])
author150000_20 = "John"

# test 21
train150000_21 = {
    "Luke": [luke_list[0]],          
    "John": [john[-k:]]
}
test150000_21 = "".join(john[:4000])
author150000_21 = "John"

# test 22
train150000_22 = {
    "Luke": [luke_list[0]],          
    "John": [john_middle_2_152k]
}
test150000_22 = "".join(john[:1000])
author150000_22 = "John"

# test 23
train150000_23 = {
    "Luke": [luke_list[0]],          
    "John": [john_middle_5_155k]
}
test150000_23 = "".join(john[:5000])
author150000_23 = "John"

# test 24
train150000_24 = {
    "Luke": [luke_block_30_180k],          
    "John": [john_list[0]]
}
test150000_24 = "".join(john[-2000:])
author150000_24 = "John"

# test 25
train150000_25 = {
    "Luke": [luke_block_50_200k],          
    "John": [john_middle_2_152k]
}
test150000_25 = "".join(john[:2000])
author150000_25 = "John"

# test 26
train150000_26 = {
    "Luke": [luke[-k:]],          
    "John": [john_middle_5_155k]
}
test150000_26 = "".join(john[300:4000])
author150000_26 = "John"

# test 27
train150000_27 = {
    "Luke": [luke_block_30_180k],          
    "John": [john[-k:]]
}
test150000_27 = "".join(john[:500])
author150000_27 = "John"

# test 28
train150000_28 = {
    "Luke": [luke[-k:]],          
    "John": [john[-k:]]
}
test150000_28 = "".join(john[:2500])
author150000_28 = "John"

# test 29
train150000_29 = {
    "Luke": [luke_block_50_200k],          
    "John": [john[-k:]]
}
test150000_29 = "".join(john[1200:3200])
author150000_29 = "John"

# test 30
train150000_30 = {
    "Luke": [luke_block_30_180k],          
    "John": [john_middle_5_155k]
}
test150000_30 = "".join(john[500:2000])
author150000_30 = "John"

# test 31
train150000_31 = {
    "Luke": [luke_block_50_200k],          
    "John": [john[-k:]]
}
test150000_31 = "".join(john[:5000])
author150000_31 = "John"

# test 32
train150000_32 = {
    "Luke": [luke[-k:]],          
    "John": [john_list[0]]
}
test150000_32 = "".join(john[-3333:])
author150000_32 = "John"

# final tuples list
tuples_list = [
    (train150000_1, test150000_1, author150000_1),
    (train150000_2, test150000_2, author150000_2),
    (train150000_3, test150000_3, author150000_3),
    (train150000_4, test150000_4, author150000_4),
    (train150000_5, test150000_5, author150000_5),
    (train150000_6, test150000_6, author150000_6),
    (train150000_7, test150000_7, author150000_7),
    (train150000_8, test150000_8, author150000_8),
    (train150000_9, test150000_9, author150000_9),
    (train150000_10, test150000_10, author150000_10),
    (train150000_11, test150000_11, author150000_11),
    (train150000_12, test150000_12, author150000_12),
    (train150000_13, test150000_13, author150000_13),
    (train150000_14, test150000_14, author150000_14),
    (train150000_15, test150000_15, author150000_15),
    (train150000_16, test150000_16, author150000_16),
    (train150000_17, test150000_17, author150000_17),
    (train150000_18, test150000_18, author150000_18),
    (train150000_19, test150000_19, author150000_19),
    (train150000_20, test150000_20, author150000_20),
    (train150000_21, test150000_21, author150000_21),
    (train150000_22, test150000_22, author150000_22),
    (train150000_23, test150000_23, author150000_23),
    (train150000_24, test150000_24, author150000_24),
    (train150000_25, test150000_25, author150000_25),
    (train150000_26, test150000_26, author150000_26),
    (train150000_27, test150000_27, author150000_27),
    (train150000_28, test150000_28, author150000_28),
    (train150000_29, test150000_29, author150000_29),
    (train150000_30, test150000_30, author150000_30),
    (train150000_31, test150000_31, author150000_31),
    (train150000_32, test150000_32, author150000_32)
]