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

k = 15000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
mark_list = get_blocks(mark, k)
peter_list = get_blocks(peter, k)
paul_list = get_blocks(paul, k)


# test 1
train15000_1 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[3]],
    "Luke": [luke_list[14]],
    "John": [john_list[9]],
    "Peter": [peter_list[0]],
    "Paul": [paul_list[0]]
}
test15000_1 = " ".join(matthew_list[1:])
author15000_1 = "Matthew"

# test 2
train15000_2 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[2]],
    "Luke": [luke_list[13]],
    "John": [john_list[8]],
    "Peter": [peter[-k:]],
    "Paul": [paul_list[1]]
}
test15000_2 = " ".join(matthew_list[:1])
author15000_2 = "Matthew"

# test 3
train15000_3 = {
    "Matthew": [matthew_list[2]],
    "Mark": [mark_list[1]],
    "Luke": [luke_list[12]],
    "John": [john_list[8]],
    "Peter": [peter_list[0]],
    "Paul": [paul_list[8]]
}
test15000_3 = " ".join(matthew_list[4:])
author15000_3 = "Matthew"

# test 4
train15000_4 = {
    "Matthew": [matthew_list[6]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[11]],
    "John": [john_list[5]],
    "Peter": [peter[-k:]],
    "Paul": [paul_list[3]]
}
test15000_4 = " ".join(matthew_list[2:6])
author15000_4 = "Matthew"

# test 5
train15000_5 = {
    "Matthew": [matthew_list[4]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[10]],
    "John": [john_list[4]],
    "Paul": [paul_list[5]],
    "Peter": [peter_list[0]]
}
test15000_5 = " ".join(matthew_list[5:])
author15000_5 = "Matthew"

# test 6
train15000_6 = {
    "Matthew": [matthew_list[5]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[9]],
    "John": [john_list[1]],
    "Paul": [paul_list[2]],
    "Peter": [peter[-k:]]
}
test15000_6 = " ".join(luke_list[:9])
author15000_6 = "Luke"

# test 7
train15000_7 = {
    "Matthew": [matthew_list[6]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[8]],
    "John": [john_list[2]],
    "Paul": [paul_list[1]],
    "Peter": [peter[-k:]]
}
test15000_7 = " ".join(luke_list[11:])
author15000_7 = "Luke"

# test 8
train15000_8 = {
    "Matthew": [matthew_list[6]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[7]],
    "John": [john_list[3]],
    "Paul": [paul_list[1]],
    "Peter": [peter[-k:]]
}
test15000_8 = " ".join(luke_list[:6])
author15000_8 = "Luke"

# test 9
train15000_9 = {
    "Matthew": [matthew_list[5]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[8]],          
    "Paul": [paul_list[3]],          
    "Peter": [peter_list[0]]
}
test15000_9 = " ".join(luke_list[:5])
author15000_9 = "Luke"

# test 10
train15000_10 = {
    "Matthew": [matthew_list[4]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[5]],          
    "John": [john_list[7]],          
    "Paul": [paul_list[4]],          
    "Peter": [peter[-k:]]
}
test15000_10 = " ".join(luke_list[6:])
author15000_10 = "Luke"

# test 11
train15000_11 = {
    "Matthew": [matthew_list[3]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[4]],          
    "John": [john_list[5]],          
    "Paul": [paul_list[6]],          
    "Peter": [peter_list[0]],         
}
test15000_11 = " ".join(mark_list[:1])
author15000_11 = "Mark"

# test 12
train15000_12 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[6]],          
    "Paul": [paul_list[7]],          
    "Peter": [peter[-k:]],         
}
test15000_12 = " ".join(mark_list[2:])
author15000_12 = "Mark"

# test 13
train15000_13 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[2]],          
    "John": [john_list[4]],          
    "Paul": [paul_list[6]],          
    "Peter": [peter_list[0]],         
}
test15000_13 = " ".join(mark_list[:1])
author15000_13 = "Mark"

# test 14
train15000_14 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[1]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[3]],          
    "Peter": [peter_list[0]],         
}
test15000_14 = " ".join(mark_list[3:])
author15000_14 = "Mark"

# test 15
train15000_15 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[0]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[7]],          
    "Peter": [peter[-k:]],         
}
test15000_15 = " ".join(mark_list[2:])
author15000_15 = "Mark"

# test 16
train15000_16 = {
    "Matthew": [matthew_list[4]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[0]],          
    "John": [john_list[5]],          
    "Paul": [paul_list[4]],          
    "Peter": [peter_list[0]],         
}
test15000_16 = " ".join(john_list[2:5])
author15000_16 = "John"

# test 17
train15000_17 = {
    "Matthew": [matthew_list[6]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[12]],          
    "John": [john_list[8]],          
    "Paul": [paul_list[8]],          
    "Peter": [peter_list[0]],         
}
test15000_17 = " ".join(john_list[9:])
author15000_17 = "John"

# test 18
train15000_18 = {
    "Matthew": [matthew_list[5]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[7]],          
    "John": [john_list[7]],          
    "Paul": [paul_list[7]],          
    "Peter": [peter[-k:]],         
}
test15000_18 = " ".join(john_list[:5])
author15000_18 = "John"

# tuka
# test 19
train15000_19 = {
    "Matthew": [matthew_list[3]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[13]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[1]],          
    "Peter": [peter[-k:]],         
}
test15000_19 = " ".join(john_list[2:])
author15000_19 = "John"

# test 20
train15000_20 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[6]],          
    "Peter": [peter[-k:]],         
}
test15000_20 = " ".join(john_list[:2])
author15000_20 = "John"

# test 21
train15000_21 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[9]],          
    "John": [john_list[9]],          
    "Paul": [paul_list[6]],          
    "Peter": [peter[-k:]],         
}
test15000_21 = " ".join(paul_list[:5])
author15000_21 = "Paul"

# test 22
train15000_22 = {
    "Matthew": [matthew_list[3]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[8]],          
    "John": [john_list[8]],          
    "Paul": [paul_list[5]],          
    "Peter": [peter[-k:]],         
}
test15000_22 = " ".join(paul_list[6:])
author15000_22 = "Paul"

# test 23
train15000_23 = {
    "Matthew": [matthew_list[6]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[7]],          
    "John": [john_list[7]],          
    "Paul": [paul_list[4]],          
    "Peter": [peter[-k:]],         
}
test15000_23 = " ".join([paul_list[0]])
author15000_23 = "Paul"

# test 24
train15000_24 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[6]],          
    "Paul": [paul_list[3]],          
    "Peter": [peter[:k]],         
}
test15000_24 = " ".join(paul_list[:3])
author15000_24 = "Paul"

# test 25
train15000_25 = {
    "Matthew": [matthew_list[3]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[5]],          
    "John": [john_list[5]],          
    "Paul": [paul_list[2]],          
    "Peter": [peter[:k]],         
}
test15000_25 = " ".join([paul_list[3]])
author15000_25 = "Paul"

# test 26
train15000_26 = {
    "Matthew": [matthew_list[5]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[4]],          
    "John": [john_list[4]],          
    "Paul": [paul_list[1]],          
    "Peter": [peter[-k:]],         
}
test15000_26 = " ".join([paul[:1000]])
author15000_26 = "Paul"

# test 27
train15000_27 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[3]],          
    "John": [john_list[3]],          
    "Paul": [paul_list[0]],          
    "Peter": [peter[-k:]],         
}
test15000_27 = " ".join([peter[1000:2000]])
author15000_27 = "Peter"

# test 28
train15000_28 = {
    "Matthew": [matthew_list[5]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[12]],          
    "John": [john_list[2]],          
    "Paul": [paul_list[8]],          
    "Peter": [peter[-k:]],         
}
test15000_28 = " ".join([peter[:-k]])
author15000_28 = "Peter"

# test 29
train15000_29 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[11]],          
    "John": [john_list[1]],          
    "Paul": [paul_list[8]],          
    "Peter": [peter[-k:]],         
}
test15000_29 = " ".join([peter[:500]])
author15000_29 = "Peter"

# test 30
train15000_30 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[12]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[7]],          
    "Peter": [peter[:k]],         
}
test15000_30 = " ".join([peter[k:]])
author15000_30 = "Peter"

# test 31
train15000_31 = {
    "Matthew": [matthew_list[4]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[10]],          
    "John": [john_list[9]],          
    "Paul": [paul_list[1]],          
    "Peter": [peter[:k]],         
}
test15000_31 = " ".join([peter[-2000:]])
author15000_31 = "Peter"

# test 32
train15000_32 = {
    "Matthew": [matthew_list[4]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[8]],          
    "John": [john_list[8]],          
    "Paul": [paul_list[1]],          
    "Peter": [peter[:k]],         
}
test15000_32 = " ".join([peter[-1500:-500]])
author15000_32 = "Peter"

# final tuples list
tuples_list = [
    (train15000_1, test15000_1, author15000_1),
    (train15000_2, test15000_2, author15000_2),
    (train15000_3, test15000_3, author15000_3),
    (train15000_4, test15000_4, author15000_4),
    (train15000_5, test15000_5, author15000_5),
    (train15000_6, test15000_6, author15000_6),
    (train15000_7, test15000_7, author15000_7),
    (train15000_8, test15000_8, author15000_8),
    (train15000_9, test15000_9, author15000_9),
    (train15000_10, test15000_10, author15000_10),
    (train15000_11, test15000_11, author15000_11),
    (train15000_12, test15000_12, author15000_12),
    (train15000_13, test15000_13, author15000_13),
    (train15000_14, test15000_14, author15000_14),
    (train15000_15, test15000_15, author15000_15),
    (train15000_16, test15000_16, author15000_16),
    (train15000_17, test15000_17, author15000_17),
    (train15000_18, test15000_18, author15000_18),
    (train15000_19, test15000_19, author15000_19),
    (train15000_20, test15000_20, author15000_20),
    (train15000_21, test15000_21, author15000_21),
    (train15000_22, test15000_22, author15000_22),
    (train15000_23, test15000_23, author15000_23),
    (train15000_24, test15000_24, author15000_24),
    (train15000_25, test15000_25, author15000_25),
    (train15000_26, test15000_26, author15000_26),
    (train15000_27, test15000_27, author15000_27),
    (train15000_28, test15000_28, author15000_28),
    (train15000_29, test15000_29, author15000_29),
    (train15000_30, test15000_30, author15000_30),
    (train15000_31, test15000_31, author15000_31),
    (train15000_32, test15000_32, author15000_32)
]