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

k = 7000

luke_list = get_blocks(luke, k)
john_list = get_blocks(john, k)
matthew_list = get_blocks(matthew, k)
mark_list = get_blocks(mark, k)
peter_list = get_blocks(peter, k)
jacob_list = get_blocks(jacob, k)
paul_list = get_blocks(paul, k)


# test 1
train7000_1 = {
    "Matthew": [matthew_list[0]],
    "Mark": [mark_list[0]],
    "Luke": [luke_list[0]],
    "John": [john_list[0]],
    "Peter": [peter_list[0]],
    "Jacob": [jacob_list[0]],
    "Paul": [paul_list[0]]
}
test7000_1 = matthew_list[2] + " " + matthew_list[3]
author7000_1 = "Matthew"

# test 2
train7000_2 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[1]],
    "Luke": [luke_list[1]],
    "John": [john_list[1]],
    "Peter": [peter_list[1]],
    "Jacob": [jacob_list[0]],
    "Paul": [paul_list[1]]
}
test7000_2 = matthew_list[5] + " " + matthew_list[6]
author7000_2 = "Matthew"

# test 3
train7000_3 = {
    "Matthew": [matthew_list[8]],
    "Mark": [mark_list[8]],
    "Luke": [luke_list[8]],
    "John": [john_list[8]],
    "Peter": [peter_list[0]],
    "Jacob": [jacob_list[0]],
    "Paul": [paul_list[8]]
}
test7000_3 = matthew_list[10] + " " + matthew_list[11]
author7000_3 = "Matthew"

# test 4
train7000_4 = {
    "Matthew": [matthew_list[9]],
    "Mark": [mark_list[2]],
    "Luke": [luke_list[31]],
    "John": [john_list[5]],
    "Peter": [peter_list[0]],
    "Jacob": [jacob_list[0]],
    "Paul": [paul_list[3]]
}
test7000_4 = matthew_list[13] + " " + matthew_list[14]
author7000_4 = "Matthew"

# test 5
train7000_5 = {
    "Matthew": [matthew_list[1]],
    "Mark": [mark_list[2]],
    "Luke": [luke_list[3]],
    "John": [john_list[4]],
    "Paul": [paul_list[5]],
    "Peter": [peter_list[0]],
    "Jacob": [jacob_list[0]]
}
test7000_5 = " ".join(luke_list[4:])
author7000_5 = "Luke"

# test 6
train7000_6 = {
    "Matthew": [matthew_list[5]],
    "Mark": [mark_list[6]],
    "Luke": [luke_list[7]],
    "John": [john_list[8]],
    "Paul": [paul_list[9]],
    "Peter": [peter_list[1]],
    "Jacob": [jacob_list[0]]
}
test7000_6 = " ".join(luke_list[:7])
author7000_6 = "Luke"

# test 7
train7000_7 = {
    "Matthew": [matthew_list[10]],
    "Mark": [mark_list[5]],
    "Luke": [luke_list[10]],
    "John": [john_list[21]],
    "Paul": [paul_list[19]],
    "Peter": [peter_list[1]],
    "Jacob": [jacob_list[0]]
}
test7000_7 = " ".join(luke_list[11:])
author7000_7 = "Luke"

# test 8
train7000_8 = {
    "Matthew": [matthew_list[14]],
    "Mark": [mark_list[8]],
    "Luke": [luke_list[31]],
    "John": [john_list[21]],
    "Paul": [paul_list[19]],
    "Peter": [peter_list[1]],
    "Jacob": [jacob_list[0]]
}
test7000_8 = " ".join(luke_list[:10])
author7000_8 = "Luke"

# test 9
train7000_9 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[6]],          
    "John": [john_list[8]],          
    "Paul": [paul_list[10]],          
    "Peter": [peter_list[0]],         
    "Jacob": [jacob_list[0]]          
}
test7000_9 = " ".join(mark_list[3:])
author7000_9 = "Mark"

# test 10
train7000_10 = {
    "Matthew": [matthew_list[3]],            
    "Mark": [mark_list[6]],           
    "Luke": [luke_list[9]],          
    "John": [john_list[12]],          
    "Paul": [paul_list[15]],          
    "Peter": [peter_list[1]],         
    "Jacob": [jacob_list[0]]          
}
test7000_10 = " ".join(mark_list[7:])
author7000_10 = "Mark"

# test 11
train7000_11 = {
    "Matthew": [matthew_list[5]],            
    "Mark": [mark_list[5]],           
    "Luke": [luke_list[10]],          
    "John": [john_list[15]],          
    "Paul": [paul_list[15]],          
    "Peter": [peter_list[1]],         
    "Jacob": [jacob_list[0]]          
}
test7000_11 = " ".join(mark_list[8:])
author7000_11 = "Mark"

# test 12
train7000_12 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[5]],          
    "John": [john_list[7]],          
    "Paul": [paul_list[9]],          
    "Peter": [peter_list[1]],         
    "Jacob": [jacob_list[0]]          
}
test7000_12 = " ".join(mark_list[:2])
author7000_12 = "Mark"

# test 13
train7000_13 = {
    "Matthew": [matthew_list[10]],            
    "Mark": [mark_list[8]],           
    "Luke": [luke_list[12]],          
    "John": [john_list[14]],          
    "Paul": [paul_list[16]],          
    "Peter": [peter_list[0]],         
    "Jacob": [jacob_list[0]]          
}
test7000_13 = " ".join(john_list[:13])
author7000_13 = "John"

# test 14
train7000_14 = {
    "Matthew": [matthew_list[14]],            
    "Mark": [mark_list[7]],           
    "Luke": [luke_list[16]],          
    "John": [john_list[18]],          
    "Paul": [paul_list[19]],          
    "Peter": [peter_list[0]],         
    "Jacob": [jacob_list[0]]          
}
test7000_14 = " ".join(john_list[19:])
author7000_14 = "John"

# test 15
train7000_15 = {
    "Matthew": [matthew_list[11]],            
    "Mark": [mark_list[6]],           
    "Luke": [luke_list[13]],          
    "John": [john_list[15]],          
    "Paul": [paul_list[17]],          
    "Peter": [peter_list[0]],         
    "Jacob": [jacob_list[0]]          
}
test7000_15 = " ".join(john_list[15:])
author7000_15 = "John"

# test 16
train7000_16 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[0]],          
    "John": [john_list[0]],          
    "Paul": [paul_list[14]],          
    "Peter": [peter_list[1]],         
    "Jacob": [jacob_list[0]]          
}
test7000_16 = " ".join(john_list[2:])
author7000_16 = "John"

# test 17
train7000_17 = {
    "Matthew": [matthew_list[4]],            
    "Mark": [mark_list[8]],           
    "Luke": [luke_list[12]],          
    "John": [john_list[16]],          
    "Paul": [paul_list[18]],          
    "Peter": [peter_list[1]],         
    "Jacob": [jacob_list[0]]          
}
test7000_17 = " ".join(john_list[17:])
author7000_17 = "John"

# test 18
train7000_18 = {
    "Matthew": [matthew_list[7]],            
    "Mark": [mark_list[7]],           
    "Luke": [luke_list[7]],          
    "John": [john_list[17]],          
    "Paul": [paul_list[17]],          
    "Peter": [peter_list[1]],         
    "Jacob": [jacob_list[0]]          
}
test7000_18 = " ".join(paul_list[:15])
author7000_18 = "Paul"

# tuka
# test 19
train7000_19 = {
    "Matthew": [matthew_list[10]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[31]],          
    "John": [john_list[21]],          
    "Paul": [paul_list[19]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_19 = " ".join(paul_list[:18])
author7000_19 = "Paul"

# test 20
train7000_20 = {
    "Matthew": [matthew_list[11]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[30]],          
    "John": [john_list[20]],          
    "Paul": [paul_list[18]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_20 = " ".join(paul_list[19:])
author7000_20 = "Paul"

# test 21
train7000_21 = {
    "Matthew": [matthew_list[12]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[29]],          
    "John": [john_list[19]],          
    "Paul": [paul_list[16]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_21 = " ".join(paul_list[:5])
author7000_21 = "Paul"

# test 22
train7000_22 = {
    "Matthew": [matthew_list[13]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[28]],          
    "John": [john_list[18]],          
    "Paul": [paul_list[15]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_22 = " ".join(paul_list[4:15])
author7000_22 = "Paul"

# test 23
train7000_23 = {
    "Matthew": [matthew_list[14]],            
    "Mark": [mark_list[4]],           
    "Luke": [luke_list[27]],          
    "John": [john_list[17]],          
    "Paul": [paul_list[14]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_23 = " ".join([peter_list[0]])
author7000_23 = "Peter"

# test 24
train7000_24 = {
    "Matthew": [matthew_list[0]],            
    "Mark": [mark_list[5]],           
    "Luke": [luke_list[26]],          
    "John": [john_list[16]],          
    "Paul": [paul_list[13]],          
    "Peter": [peter[:k]],         
    "Jacob": [jacob[-k:]]          
}
test7000_24 = " ".join([peter[k:]])
author7000_24 = "Peter"

# test 25
train7000_25 = {
    "Matthew": [matthew_list[1]],            
    "Mark": [mark_list[6]],           
    "Luke": [luke_list[25]],          
    "John": [john_list[15]],          
    "Paul": [paul_list[12]],          
    "Peter": [peter[:k]],         
    "Jacob": [jacob[-k:]]          
}
test7000_25 = " ".join([peter[-k:]])
author7000_25 = "Peter"

# test 26
train7000_26 = {
    "Matthew": [matthew_list[2]],            
    "Mark": [mark_list[7]],           
    "Luke": [luke_list[24]],          
    "John": [john_list[14]],          
    "Paul": [paul_list[11]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_26 = " ".join([peter[:1000]])
author7000_26 = "Peter"

# test 27
train7000_27 = {
    "Matthew": [matthew_list[3]],            
    "Mark": [mark_list[8]],           
    "Luke": [luke_list[23]],          
    "John": [john_list[13]],          
    "Paul": [paul_list[10]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_27 = " ".join([peter[2000:3000]])
author7000_27 = "Peter"

# test 28
train7000_28 = {
    "Matthew": [matthew_list[4]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[22]],          
    "John": [john_list[12]],          
    "Paul": [paul_list[9]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_28 = " ".join([jacob[:-k]])
author7000_28 = "Jacob"

# test 29
train7000_29 = {
    "Matthew": [matthew_list[5]],            
    "Mark": [mark_list[1]],           
    "Luke": [luke_list[21]],          
    "John": [john_list[11]],          
    "Paul": [paul_list[8]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_29 = " ".join([jacob[:1000]])
author7000_29 = "Jacob"

# test 30
train7000_30 = {
    "Matthew": [matthew_list[6]],            
    "Mark": [mark_list[2]],           
    "Luke": [luke_list[20]],          
    "John": [john_list[10]],          
    "Paul": [paul_list[7]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[-k:]]          
}
test7000_30 = " ".join([jacob[1000:2000]])
author7000_30 = "Jacob"

# test 31
train7000_31 = {
    "Matthew": [matthew_list[7]],            
    "Mark": [mark_list[3]],           
    "Luke": [luke_list[19]],          
    "John": [john_list[9]],          
    "Paul": [paul_list[17]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[:k]]          
}
test7000_31 = " ".join([jacob[-1000:]])
author7000_31 = "Jacob"

# test 32
train7000_32 = {
    "Matthew": [matthew_list[8]],            
    "Mark": [mark_list[0]],           
    "Luke": [luke_list[18]],          
    "John": [john_list[8]],          
    "Paul": [paul_list[17]],          
    "Peter": [peter[-k:]],         
    "Jacob": [jacob[:k]]          
}
test7000_32 = " ".join([jacob[-2000:-1000]])
author7000_32 = "Jacob"

# final tuples list
tuples_list = [
    (train7000_1, test7000_1, author7000_1),
    (train7000_2, test7000_2, author7000_2),
    (train7000_3, test7000_3, author7000_3),
    (train7000_4, test7000_4, author7000_4),
    (train7000_5, test7000_5, author7000_5),
    (train7000_6, test7000_6, author7000_6),
    (train7000_7, test7000_7, author7000_7),
    (train7000_8, test7000_8, author7000_8),
    (train7000_9, test7000_9, author7000_9),
    (train7000_10, test7000_10, author7000_10),
    (train7000_11, test7000_11, author7000_11),
    (train7000_12, test7000_12, author7000_12),
    (train7000_13, test7000_13, author7000_13),
    (train7000_14, test7000_14, author7000_14),
    (train7000_15, test7000_15, author7000_15),
    (train7000_16, test7000_16, author7000_16),
    (train7000_17, test7000_17, author7000_17),
    (train7000_18, test7000_18, author7000_18),
    (train7000_19, test7000_19, author7000_19),
    (train7000_20, test7000_20, author7000_20),
    (train7000_21, test7000_21, author7000_21),
    (train7000_22, test7000_22, author7000_22),
    (train7000_23, test7000_23, author7000_23),
    (train7000_24, test7000_24, author7000_24),
    (train7000_25, test7000_25, author7000_25),
    (train7000_26, test7000_26, author7000_26),
    (train7000_27, test7000_27, author7000_27),
    (train7000_28, test7000_28, author7000_28),
    (train7000_29, test7000_29, author7000_29),
    (train7000_30, test7000_30, author7000_30),
    (train7000_31, test7000_31, author7000_31),
    (train7000_32, test7000_32, author7000_32)
]