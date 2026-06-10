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
mark = mark
peter = peter1 + peter2
jacob = jacob
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

k = 30000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
mark_list = get_blocks(mark, k)
paul_list = get_blocks(paul, k)


# test 1
train30000_1 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[6]],
    "John": [john_list[3]],
    "Paul": [paul_list[0]]
}
test30000_1 = "".join(matthew_list[1:])
author30000_1 = "Matthew"

# test 2
train30000_2 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[1]],
    "Luke": [luke_list[5]],
    "John": [john_list[4]],
    "Paul": [paul_list[1]]
}
test30000_2 = "".join(matthew_list[0])
author30000_2 = "Matthew"

# test 3
train30000_3 = {
    "Matthew": [matthew_list[2]],
    "Mark": [mark_list[1]],
    "Luke": [luke_list[4]],
    "John": [john_list[0]],
    "Paul": [paul_list[2]]
}
test30000_3 = "".join(matthew_list[1])
author30000_3 = "Matthew"

# test 4
train30000_4 = {
    "Matthew": [matthew_list[2]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[3]],
    "John": [john_list[1]],
    "Paul": [paul_list[3]]
}
test30000_4 = "".join(matthew[-10000:])
author30000_4 = "Matthew"

# test 5
train30000_5 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[2]],
    "John": [john_list[2]],
    "Paul": [paul_list[0]]
}
test30000_5 = "".join(matthew[-5000:])
author30000_5 = "Matthew"

# test 6
train30000_6 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[1]],
    "John": [john_list[3]],
    "Paul": [paul_list[0]]
}
test30000_6 = "".join(matthew[35000:40000])
author30000_6 = "Matthew"

# test 7
train30000_7 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[2]],
    "Paul": [paul_list[1]]
}
test30000_7 = "".join(luke_list[1:])
author30000_7 = "Luke"

# test 8
train30000_8 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[1]],
    "Luke": [luke_list[0]],
    "John": [john_list[4]],
    "Paul": [paul_list[1]]
}
test30000_8 = "".join(luke_list[2:4])
author30000_8 = "Luke"

# test 9
train30000_9 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[3]]
}
test30000_9 = "".join(luke_list[:2])
author30000_9 = "Luke"

# test 10
train30000_10 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[4]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[3]]
}
test30000_10 = "".join(luke_list[5:])
author30000_10 = "Luke"

# test 11
train30000_11 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[2]]
}
test30000_11 = "".join(luke_list[2:4])
author30000_11 = "Luke"

# test 12
train30000_12 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[2]]
}
test30000_12 = "".join(luke_list[2:6])
author30000_12 = "Luke"

# test 13
train30000_13 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[3]]
}
test30000_13 = "".join(mark[50000:])
author30000_13 = "Mark"

# test 14
train30000_14 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[3]]
}
test30000_14 = "".join(mark_list[0])
author30000_14 = "Mark"

# test 15
train30000_15 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[1]]
}
test30000_15 = "".join(mark[:2000])
author30000_15 = "Mark"

# test 16
train30000_16 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[5]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[1]]
}
test30000_16 = "".join(mark[-20000:])
author30000_16 = "Mark"

# test 17
train30000_17 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[0]]
}
test30000_17 = "".join(mark[20000:30000])
author30000_17 = "Mark"

# test 18
train30000_18 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[5]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[0]]
}
test30000_18 = "".join(mark[4000:16000])
author30000_18 = "Mark"


# test 19
train30000_19 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test30000_19 = "".join(mark[50000:60000])
author30000_19 = "Mark"

# test 20
train30000_20 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[0]]
}
test30000_20 = "".join(john_list[1])
author30000_20 = "John"

# test 21
train30000_21 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[3]]
}
test30000_21 = "".join(john_list[0])
author30000_21 = "John"

# test 22
train30000_22 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[0]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[3]]
}
test30000_22 = "".join(john_list[2])
author30000_22 = "John"

# test 23
train30000_23 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[2]]
}
test30000_23 = "".join(john_list[4])
author30000_23 = "John"

# test 24
train30000_24 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[5]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[1]]
}
test30000_24 = "".join(john_list[3:])
author30000_24 = "John"

# test 25
train30000_25 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[4]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[2]]
}
test30000_25 = "".join(john_list[2:4])
author30000_25 = "John"

# test 26
train30000_26 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[3]]
}
test30000_26 = "".join(paul[:1000])
author30000_26 = "Paul"

# test 27
train30000_27 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[0]]
}
test30000_27 = "".join(paul_list[1:])
author30000_27 = "Paul"

# test 28
train30000_28 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[1]]
}
test30000_28 = "".join(paul_list[2:])
author30000_28 = "Paul"

# test 29
train30000_29 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[4]],          
    "Paul": [paul_list[2]]
}
test30000_29 = "".join(paul[:500])
author30000_29 = "Paul"

# test 30
train30000_30 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[4]],          
    "Paul": [paul_list[2]]
}
test30000_30 = "".join(paul[45000:50000])
author30000_30 = "Paul"

# test 31
train30000_31 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[1]]
}
test30000_31 = "".join(paul[-55000:])
author30000_31 = "Paul"

# test 32
train30000_32 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[3]]
}
test30000_32 = "".join(paul[-19000:-5000])
author30000_32 = "Paul"

# final tuples list
tuples_list = [
    (train30000_1, test30000_1, author30000_1),
    (train30000_2, test30000_2, author30000_2),
    (train30000_3, test30000_3, author30000_3),
    (train30000_4, test30000_4, author30000_4),
    (train30000_5, test30000_5, author30000_5),
    (train30000_6, test30000_6, author30000_6),
    (train30000_7, test30000_7, author30000_7),
    (train30000_8, test30000_8, author30000_8),
    (train30000_9, test30000_9, author30000_9),
    (train30000_10, test30000_10, author30000_10),
    (train30000_11, test30000_11, author30000_11),
    (train30000_12, test30000_12, author30000_12),
    (train30000_13, test30000_13, author30000_13),
    (train30000_14, test30000_14, author30000_14),
    (train30000_15, test30000_15, author30000_15),
    (train30000_16, test30000_16, author30000_16),
    (train30000_17, test30000_17, author30000_17),
    (train30000_18, test30000_18, author30000_18),
    (train30000_19, test30000_19, author30000_19),
    (train30000_20, test30000_20, author30000_20),
    (train30000_21, test30000_21, author30000_21),
    (train30000_22, test30000_22, author30000_22),
    (train30000_23, test30000_23, author30000_23),
    (train30000_24, test30000_24, author30000_24),
    (train30000_25, test30000_25, author30000_25),
    (train30000_26, test30000_26, author30000_26),
    (train30000_27, test30000_27, author30000_27),
    (train30000_28, test30000_28, author30000_28),
    (train30000_29, test30000_29, author30000_29),
    (train30000_30, test30000_30, author30000_30),
    (train30000_31, test30000_31, author30000_31),
    (train30000_32, test30000_32, author30000_32)
]