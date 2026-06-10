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
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test90000_1 = "".join(matthew[-17000:])
author90000_1 = "Matthew"

# test 2
train90000_2 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_2 = "".join(matthew[:17000])
author90000_2 = "Matthew"

# test 3
train90000_3 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_3 = "".join(matthew[-7000:])
author90000_3 = "Matthew"

# test 4
train90000_4 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_4 = "".join(matthew[1000:16000])
author90000_4 = "Matthew"

# test 5
train90000_5 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_5 = "".join(matthew[300:1000])
author90000_5 = "Matthew"

# test 6
train90000_6 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test90000_6 = "".join(matthew[-4000:-3000])
author90000_6 = "Matthew"

# test 7
train90000_7 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_7 = "".join(matthew[-500:])
author90000_7 = "Matthew"

# test 8
train90000_8 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],
    "John": [john_list[0]],
    "Paul": [paul[-k:]]
}
test90000_8 = "".join(matthew[:500])
author90000_8 = "Matthew"

# test 9
train90000_9 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_9 = "".join(luke_list[1])
author90000_9 = "Luke"

# test 10
train90000_10 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_10 = "".join(luke_list[0])
author90000_10 = "Luke"

# test 11
train90000_11 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_11 = "".join(luke[:40000])
author90000_11 = "Luke"

# test 12
train90000_12 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test90000_12 = "".join(luke[-45000:])
author90000_12 = "Luke"

# test 13
train90000_13 = {
    "Matthew": [matthew_list[0]],        
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_13 = "".join(luke[100000:130000])
author90000_13 = "Luke"

# test 14
train90000_14 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test90000_14 = "".join(luke[-500:])
author90000_14 = "Luke"

# test 15
train90000_15 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul[-k:]]
}
test90000_15 = "".join(luke[-30000:-20000])
author90000_15 = "Luke"

# test 16
train90000_16 = {
    "Matthew": [matthew_list[0]],       
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_16 = "".join(luke[-15000:-7000])
author90000_16 = "Luke"

# test 17
train90000_17 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test90000_17 = "".join(john[-65000:])
author90000_17 = "John"

# test 18
train90000_18 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_18 = "".join(john[:40000])
author90000_18 = "John"


# test 19
train90000_19 = {
    "Matthew": [matthew_list[0]],        
    "Luke": [luke_list[0]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test90000_19 = "".join(john[-16000:])
author90000_19 = "John"

# test 20
train90000_20 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_20 = "".join(john[10000:35000])
author90000_20 = "John"

# test 21
train90000_21 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_21 = "".join(john[:4000])
author90000_21 = "John"

# test 22
train90000_22 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_22 = "".join(john[2000:4000])
author90000_22 = "John"

# test 23
train90000_23 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_23 = "".join(john[56000:-k])
author90000_23 = "John"

# test 24
train90000_24 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul[-k:]]
}
test90000_24 = "".join(john[-5000:-2000])
author90000_24 = "John"

# test 25
train90000_25 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul[-k:]]
}
test90000_25 = "".join(paul[:-k])
author90000_25 = "Paul"

# test 26
train90000_26 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_26 = "".join(paul[20000:50000])
author90000_26 = "Paul"

# test 27
train90000_27 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_27 = "".join(paul[-40000:])
author90000_27 = "Paul"

# test 28
train90000_28 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_28 = "".join(paul[:5000])
author90000_28 = "Paul"

# test 29
train90000_29 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_29 = "".join(paul[-3800:-2800])
author90000_29 = "Paul"

# test 30
train90000_30 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul_list[0]]
}
test90000_30 = "".join(paul[-12000:-4000])
author90000_30 = "Paul"

# test 31
train90000_31 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],          
    "John": [john[-k:]],
    "Paul": [paul[-k:]]
}
test90000_31 = "".join(paul[500:17000])
author90000_31 = "Paul"

# test 32
train90000_32 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test90000_32 = "".join(paul[90500:120000])
author90000_32 = "Paul"

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
    (train90000_10, test90000_10, author90000_10),
    (train90000_11, test90000_11, author90000_11),
    (train90000_12, test90000_12, author90000_12),
    (train90000_13, test90000_13, author90000_13),
    (train90000_14, test90000_14, author90000_14),
    (train90000_15, test90000_15, author90000_15),
    (train90000_16, test90000_16, author90000_16),
    (train90000_17, test90000_17, author90000_17),
    (train90000_18, test90000_18, author90000_18),
    (train90000_19, test90000_19, author90000_19),
    (train90000_20, test90000_20, author90000_20),
    (train90000_21, test90000_21, author90000_21),
    (train90000_22, test90000_22, author90000_22),
    (train90000_23, test90000_23, author90000_23),
    (train90000_24, test90000_24, author90000_24),
    (train90000_25, test90000_25, author90000_25),
    (train90000_26, test90000_26, author90000_26),
    (train90000_27, test90000_27, author90000_27),
    (train90000_28, test90000_28, author90000_28),
    (train90000_29, test90000_29, author90000_29),
    (train90000_30, test90000_30, author90000_30),
    (train90000_31, test90000_31, author90000_31),
    (train90000_32, test90000_32, author90000_32)
]