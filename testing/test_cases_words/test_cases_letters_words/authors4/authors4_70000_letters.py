from new_testament_texts.letter_texts import P_letters, NP_letters

luke = "^ " + NP_letters.luke + " *"
acts = "^ " + NP_letters.acts + " *"
john = "^ " + NP_letters.john + " *"
john1 = "^ " + NP_letters.john1 + " *"
john2 = "^ " + NP_letters.john2 + " *"
john3 = "^ " + NP_letters.john3 + " *"
revelation = "^ " + NP_letters.revelation + " *"
matthew = "^ " + NP_letters.matthew + " *"
mark = "^ " + NP_letters.mark + " *"
peter1 = "^ " + NP_letters.peter1 + " *"
peter2 = "^ " + NP_letters.peter2 + " *"
jacob = "^ " + NP_letters.jacob + " *"
romans = "^ " + P_letters.romans + " *"
corinthians1 = "^ " + P_letters.corinthians1 + " *"
corinthians2 = "^ " + P_letters.corinthians2 + " *"
galatians = "^ " + P_letters.galatians + " *"
philemon = "^ " + P_letters.philemon + " *"
thessalonians1 = "^ " + P_letters.thessalonians1 + " *"
philippians = "^ " + P_letters.philippians + " *"

luke = luke + " " + acts
john = john + " " + john1 + " " + john2 + " " + john3 + " " + revelation
matthew = matthew
mark = mark
peter = peter1 + " " + peter2
jacob = jacob
paul = romans + " " + corinthians1 + " " + corinthians2 + " " + philippians + " " + philemon + " " + thessalonians1 + " " + galatians

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
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test70000_1 = " ".join([matthew[-37000:]])
author70000_1 = "Matthew"

# test 2
train70000_2 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test70000_2 = " ".join([matthew[:37000]])
author70000_2 = "Matthew"

# test 3
train70000_3 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[2]],
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test70000_3 = " ".join([matthew[-27000:]])
author70000_3 = "Matthew"

# test 4
train70000_4 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test70000_4 = " ".join([matthew[1000:16000]])
author70000_4 = "Matthew"

# test 5
train70000_5 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[2]],
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test70000_5 = " ".join([matthew[3000:10000]])
author70000_5 = "Matthew"

# test 6
train70000_6 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test70000_6 = " ".join([matthew[-4000:-3000]])
author70000_6 = "Matthew"

# test 7
train70000_7 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test70000_7 = " ".join([matthew[-500:]])
author70000_7 = "Matthew"

# test 8
train70000_8 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test70000_8 = " ".join([matthew[:500]])
author70000_8 = "Matthew"

# test 9
train70000_9 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test70000_9 = " ".join([luke_list[2]])
author70000_9 = "Luke"

# test 10
train70000_10 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test70000_10 = " ".join([luke_list[0]])
author70000_10 = "Luke"

# test 11
train70000_11 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test70000_11 = " ".join([luke_list[2]])
author70000_11 = "Luke"

# test 12
train70000_12 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test70000_12 = " ".join([luke[-18000:]])
author70000_12 = "Luke"

# test 13
train70000_13 = {
    "Matthew": [matthew_list[0]],         
    "Luke": [luke_list[0]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[1]]
}
test70000_13 = " ".join([luke_list[1]])
author70000_13 = "Luke"

# test 14
train70000_14 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test70000_14 = " ".join([luke[-500:]])
author70000_14 = "Luke"

# test 15
train70000_15 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[2]],          
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test70000_15 = " ".join([luke_list[0]])
author70000_15 = "Luke"

# test 16
train70000_16 = {
    "Matthew": [matthew_list[0]],        
    "Luke": [luke_list[2]],          
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test70000_16 = " ".join([luke_list[1]])
author70000_16 = "Luke"

# test 17
train70000_17 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test70000_17 = " ".join([john_list[0]])
author70000_17 = "John"

# test 18
train70000_18 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test70000_18 = " ".join([john_list[1]])
author70000_18 = "John"


# test 19
train70000_19 = {
    "Matthew": [matthew_list[0]],         
    "Luke": [luke_list[0]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test70000_19 = " ".join([john[-16000:]])
author70000_19 = "John"

# test 20
train70000_20 = {
    "Matthew": [matthew[-k:]],            
    "Luke": [luke_list[0]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test70000_20 = " ".join([john[-10000:]])
author70000_20 = "John"

# test 21
train70000_21 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[1]]
}
test70000_21 = " ".join([john[:4000]])
author70000_21 = "John"

# test 22
train70000_22 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test70000_22 = " ".join([john[2000:4000]])
author70000_22 = "John"

# test 23
train70000_23 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test70000_23 = " ".join([john[-16000:]])
author70000_23 = "John"

# test 24
train70000_24 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test70000_24 = " ".join([john[-5000:-2000]])
author70000_24 = "John"

# test 25
train70000_25 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[1]]
}
test70000_25 = " ".join([paul_list[0]])
author70000_25 = "Paul"

# test 26
train70000_26 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[1]]
}
test70000_26 = " ".join([paul[20000:60000]])
author70000_26 = "Paul"

# test 27
train70000_27 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test70000_27 = " ".join([paul_list[1]])
author70000_27 = "Paul"

# test 28
train70000_28 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test70000_28 = " ".join([paul[70000:]])
author70000_28 = "Paul"

# test 29
train70000_29 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test70000_29 = " ".join([paul[-40000:]])
author70000_29 = "Paul"

# test 30
train70000_30 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[0]],          
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test70000_30 = " ".join([paul[-12000:-4000]])
author70000_30 = "Paul"

# test 31
train70000_31 = {
    "Matthew": [matthew_list[0]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test70000_31 = " ".join([paul[-500:]])
author70000_31 = "Paul"

# test 32
train70000_32 = {
    "Matthew": [matthew[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test70000_32 = " ".join([paul[80000:90000]])
author70000_32 = "Paul"

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
    (train70000_10, test70000_10, author70000_10),
    (train70000_11, test70000_11, author70000_11),
    (train70000_12, test70000_12, author70000_12),
    (train70000_13, test70000_13, author70000_13),
    (train70000_14, test70000_14, author70000_14),
    (train70000_15, test70000_15, author70000_15),
    (train70000_16, test70000_16, author70000_16),
    (train70000_17, test70000_17, author70000_17),
    (train70000_18, test70000_18, author70000_18),
    (train70000_19, test70000_19, author70000_19),
    (train70000_20, test70000_20, author70000_20),
    (train70000_21, test70000_21, author70000_21),
    (train70000_22, test70000_22, author70000_22),
    (train70000_23, test70000_23, author70000_23),
    (train70000_24, test70000_24, author70000_24),
    (train70000_25, test70000_25, author70000_25),
    (train70000_26, test70000_26, author70000_26),
    (train70000_27, test70000_27, author70000_27),
    (train70000_28, test70000_28, author70000_28),
    (train70000_29, test70000_29, author70000_29),
    (train70000_30, test70000_30, author70000_30),
    (train70000_31, test70000_31, author70000_31),
    (train70000_32, test70000_32, author70000_32)
]