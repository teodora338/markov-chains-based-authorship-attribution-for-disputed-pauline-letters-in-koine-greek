from new_testament_texts.stripped_texts import P_stripped, NP_stripped

luke = "^ " + NP_stripped.luke + " *"
acts = "^ " + NP_stripped.acts + " *"
john = "^ " + NP_stripped.john + " *"
john1 = "^ " + NP_stripped.john1 + " *"
john2 = "^ " + NP_stripped.john2 + " *"
john3 = "^ " + NP_stripped.john3 + " *"
revelation = "^ " + NP_stripped.revelation + " *"
matthew = "^ " + NP_stripped.matthew + " *"
mark = "^ " + NP_stripped.mark + " *"
peter1 = "^ " + NP_stripped.peter1 + " *"
peter2 = "^ " + NP_stripped.peter2 + " *"
jacob = "^ " + NP_stripped.jacob + " *"
romans = "^ " + P_stripped.romans + " *"
corinthians1 = "^ " + P_stripped.corinthians1 + " *"
corinthians2 = "^ " + P_stripped.corinthians2 + " *"
galatians = "^ " + P_stripped.galatians + " *"
philemon = "^ " + P_stripped.philemon + " *"
thessalonians1 = "^ " + P_stripped.thessalonians1 + " *"
philippians = "^ " + P_stripped.philippians + " *"
jude = "^ " + NP_stripped.jude + " *"

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

k = 50000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
mark_list = get_blocks(mark, k)
paul_list = get_blocks(paul, k)


# test 1
train50000_1 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[2]],
    "Paul": [paul_list[0]]
}
test50000_1 = " ".join(matthew_list[1:])
author50000_1 = "Matthew"

# test 2
train50000_2 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],
    "John": [john_list[2]],
    "Paul": [paul_list[1]]
}
test50000_2 = " ".join([matthew_list[0]])
author50000_2 = "Matthew"

# test 3
train50000_3 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[2]],
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test50000_3 = " ".join([matthew[-k:]])
author50000_3 = "Matthew"

# test 4
train50000_4 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark[-k:]],
    "Luke": [luke_list[3]],
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test50000_4 = " ".join([matthew[-1000:-500]])
author50000_4 = "Matthew"

# test 5
train50000_5 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[2]],
    "John": [john_list[2]],
    "Paul": [paul_list[0]]
}
test50000_5 = " ".join([matthew[-4000:]])
author50000_5 = "Matthew"

# test 6
train50000_6 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test50000_6 = " ".join([matthew[105000:]])
author50000_6 = "Matthew"

# test 7
train50000_7 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[2]],
    "Paul": [paul_list[1]]
}
test50000_7 = " ".join(luke_list[1:])
author50000_7 = "Luke"

# test 8
train50000_8 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark[-k:]],
    "Luke": [luke_list[0]],
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test50000_8 = " ".join(luke_list[2:4])
author50000_8 = "Luke"

# test 9
train50000_9 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test50000_9 = " ".join(luke_list[:2])
author50000_9 = "Luke"

# test 10
train50000_10 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test50000_10 = " ".join([luke_list[3]])
author50000_10 = "Luke"

# test 11
train50000_11 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[3]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test50000_11 = " ".join(luke_list[0:3])
author50000_11 = "Luke"

# test 12
train50000_12 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test50000_12 = " ".join([luke_list[0]])
author50000_12 = "Luke"

# test 13
train50000_13 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test50000_13 = " ".join([mark[-17000:]])
author50000_13 = "Mark"

# test 14
train50000_14 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test50000_14 = " ".join([mark[:17000]])
author50000_14 = "Mark"

# test 15
train50000_15 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test50000_15 = " ".join([mark[:2000]])
author50000_15 = "Mark"

# test 16
train50000_16 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[0]],
    "Paul": [paul_list[1]]
}
test50000_16 = " ".join([mark[-5000:]])
author50000_16 = "Mark"

# test 17
train50000_17 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test50000_17 = " ".join([mark[3000:12000]])
author50000_17 = "Mark"

# test 18
train50000_18 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],
    "Paul": [paul_list[0]]
}
test50000_18 = " ".join([mark[4000:16000]])
author50000_18 = "Mark"


# test 19
train50000_19 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test50000_19 = " ".join([mark[50000:60000]])
author50000_19 = "Mark"

# test 20
train50000_20 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[0]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test50000_20 = " ".join([john_list[1]])
author50000_20 = "John"

# test 21
train50000_21 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[1]]
}
test50000_21 = " ".join([john_list[0]])
author50000_21 = "John"

# test 22
train50000_22 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test50000_22 = " ".join([john_list[2]])
author50000_22 = "John"

# test 23
train50000_23 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test50000_23 = " ".join([john_list[0]])
author50000_23 = "John"

# test 24
train50000_24 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test50000_24 = " ".join([john[-k:]])
author50000_24 = "John"

# test 25
train50000_25 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[1]]
}
test50000_25 = " ".join(john_list[1:])
author50000_25 = "John"

# test 26
train50000_26 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[1]]
}
test50000_26 = " ".join([paul[:10000]])
author50000_26 = "Paul"

# test 27
train50000_27 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[2]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test50000_27 = " ".join([paul_list[1]])
author50000_27 = "Paul"

# test 28
train50000_28 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test50000_28 = " ".join([paul_list[0]])
author50000_28 = "Paul"

# test 29
train50000_29 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test50000_29 = " ".join([paul[-40000:]])
author50000_29 = "Paul"

# test 30
train50000_30 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[0]],          
    "John": [john_list[1]],
    "Paul": [paul_list[0]]
}
test50000_30 = " ".join([paul[-k:]])
author50000_30 = "Paul"

# test 31
train50000_31 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],
    "Paul": [paul_list[1]]
}
test50000_31 = " ".join([paul[-5500:]])
author50000_31 = "Paul"

# test 32
train50000_32 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark[-k:]],
    "Luke": [luke_list[1]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test50000_32 = " ".join([paul[-70000:-50000]])
author50000_32 = "Paul"

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
    (train50000_10, test50000_10, author50000_10),
    (train50000_11, test50000_11, author50000_11),
    (train50000_12, test50000_12, author50000_12),
    (train50000_13, test50000_13, author50000_13),
    (train50000_14, test50000_14, author50000_14),
    (train50000_15, test50000_15, author50000_15),
    (train50000_16, test50000_16, author50000_16),
    (train50000_17, test50000_17, author50000_17),
    (train50000_18, test50000_18, author50000_18),
    (train50000_19, test50000_19, author50000_19),
    (train50000_20, test50000_20, author50000_20),
    (train50000_21, test50000_21, author50000_21),
    (train50000_22, test50000_22, author50000_22),
    (train50000_23, test50000_23, author50000_23),
    (train50000_24, test50000_24, author50000_24),
    (train50000_25, test50000_25, author50000_25),
    (train50000_26, test50000_26, author50000_26),
    (train50000_27, test50000_27, author50000_27),
    (train50000_28, test50000_28, author50000_28),
    (train50000_29, test50000_29, author50000_29),
    (train50000_30, test50000_30, author50000_30),
    (train50000_31, test50000_31, author50000_31),
    (train50000_32, test50000_32, author50000_32)
]