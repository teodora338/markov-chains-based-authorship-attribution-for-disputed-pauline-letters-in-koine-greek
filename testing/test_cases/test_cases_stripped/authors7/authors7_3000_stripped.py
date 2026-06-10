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

k = 3000

# test 1
train3000_1 = {
    "Matthew": [matthew[:3000]],
    "Mark": [mark[:3000]],
    "Luke": [luke[:3000]],
    "John": [john[:3000]],
    "Peter": [peter1[:3000]],
    "Jacob": [jacob[:3000]],
    "Paul": [romans[:3000]]
}
test3000_1 = matthew[3000:]
author3000_1 = "Matthew"

# test 2
train3000_2 = {
    "Matthew": [matthew[-3000:]],
    "Mark": [mark[3000:6000]],
    "Luke": [acts[:3000]],
    "John": [john1[:3000]],
    "Peter": [peter2[:3000]],
    "Jacob": [jacob[3000:6000]],
    "Paul": [corinthians1[:3000]]
}
test3000_2 = matthew[:-3000]
author3000_2 = "Matthew"

# test 3
train3000_3 = {
    "Matthew": [matthew[3000:6000]],
    "Mark": [mark[6000:9000]],
    "Luke": [luke[3000:6000]],
    "John": [john[3000:6000]],
    "Peter": [peter1[3000:6000]],
    "Jacob": [jacob[6000:9000]],
    "Paul": [romans[3000:6000]]
}
test3000_3 = acts[-70000:]
author3000_3 = "Luke"

# test 4
train3000_4 = {
    "Matthew": [matthew[6000:9000]],
    "Mark": [mark[6000:9000]],
    "Luke": [acts[3000:6000]],
    "John": [john1[3000:6000]],
    "Peter": [peter2[3000:6000]],
    "Jacob": [jacob[-3000:]],
    "Paul": [corinthians1[3000:6000]]
}
test3000_4 = luke[-70000:]
author3000_4 = "Luke"

# test 5
train3000_5 = {
    "Matthew": [matthew[9000:12000]],
    "Mark": [mark[-3000:]],
    "Luke": [acts[6000:9000]],
    "John": [john[6000:9000]],
    "Peter": [peter1[6000:9000]],
    "Jacob": [jacob[6000:9000]],
    "Paul": [corinthians2[:3000]]
}
test3000_5 = mark[:-3000]
author3000_5 = "Mark"

# test 6
train3000_6 = {
    "Matthew": [matthew[12000:12000+k]],
    "Mark": [mark[9000:9000+k]],
    "Luke": [luke[6000:6000+k]],
    "John": [john[-k:]],
    "Peter": [peter2[-k:]],
    "Jacob": [jacob[-k:]],
    "Paul": [thessalonians1[:k]]
}
test3000_6 = mark[:3*k]
author3000_6 = "Mark"

# test 7
train3000_7 = {
    "Matthew": [matthew[5*k:6*k]],
    "Mark": [mark[3*k:4*k]],
    "Luke": [acts[3*k:4*k]],
    "John": [john1[-k:]],
    "Peter": [peter1[-k:]],
    "Jacob": [jacob[-k:]],
    "Paul": [galatians[:k]]
}
test3000_7 = matthew[:5*k]
author3000_7 = "Matthew"

# test 8
train3000_8 = {
    "Matthew": [matthew[6*k:7*k]],
    "Mark": [mark[3*k:4*k]],
    "Luke": [luke[3*k:4*k]],
    "John": [john[3*k:4*k]],
    "Peter": [peter2[-k:]],
    "Jacob": [jacob[2000:5000]],
    "Paul": [philippians[:k]]
}
test3000_8 = mark[4*k:]
author3000_8 = "Mark"

# test 9
train3000_9 = {
    "Matthew": [matthew[7*k:8*k]],
    "Mark": [mark[4*k:5*k]],
    "Luke": [acts[4*k:5*k]],
    "John": [revelation[3*k:4*k]],
    "Peter": [peter1[1000:4000]],
    "Jacob": [jacob[2000:5000]],
    "Paul": [galatians[:3000]]
}
test3000_9 = luke[:70000]
author3000_9 = "Luke"

# test 10
train3000_10 = {
    "Matthew": [matthew[8*k:9*k]],
    "Mark": [mark[5*k:6*k]],
    "Luke": [acts[4*k:5*k]],
    "John": [revelation[4*k:5*k]],
    "Peter": [peter2[1000:4000]],
    "Jacob": [jacob[1000:4000]],
    "Paul": [romans[-3000:]]
}
test3000_10 = jacob[:1000]
author3000_10 = "Jacob"

# test 11
train3000_11 = {
    "Matthew": [matthew[9*k:10*k]],
    "Mark": [mark[6*k:7*k]],
    "Luke": [acts[5*k:6*k]],
    "John": [revelation[5*k:6*k]],
    "Peter": [peter2[-3000:]],
    "Jacob": [jacob[:3000]],
    "Paul": [corinthians1[-3000:]]
}
test3000_11 = john[:]
author3000_11 = "John"

# test 12
train3000_12 = {
    "Matthew": [matthew[10*k:11*k]],
    "Mark": [mark[7*k:8*k]],
    "Luke": [acts[6*k:7*k]],
    "John": [revelation[5*k:6*k]],
    "Peter": [peter1[1800:4800]],
    "Jacob": [jacob[-3000:]],
    "Paul": [philippians[-3000:]]
}
test3000_12 = jacob[:3000]
author3000_12 = "Jacob"

# test 13
train3000_13 = {
    "Matthew": [matthew[11*k:12*k]],
    "Mark": [mark[8*k:9*k]],
    "Luke": [luke[6*k:7*k]],
    "John": [john[5*k:6*k]],
    "Peter": [peter1[5000:8000]],
    "Jacob": [jacob[:3000]],
    "Paul": [philippians[-3000:]]
}
test3000_13 = jacob[3000:9000]
author3000_13 = "Jacob"

# test 14
train3000_14 = {
    "Matthew": [matthew[12*k:13*k]],
    "Mark": [mark[9*k:10*k]],
    "Luke": [luke[7*k:8*k]],
    "John": [revelation[5*k:6*k]],
    "Peter": [peter2[2000:5000]],
    "Jacob": [jacob[-k:]],
    "Paul": [thessalonians1[5000:8000]]
}
test3000_14 = peter1[:]
author3000_14 = "Peter"

# test 15
train3000_15 = {
    "Matthew": [matthew[13*k:14*k]],
    "Mark": [mark[10*k:11*k]],
    "Luke": [acts[7*k:8*k]],
    "John": [john[5*k:6*k]],
    "Peter": [peter2[-k:]],
    "Jacob": [jacob[6000:9000]],
    "Paul": [galatians[6000:9000]]
}
test3000_15 = peter1[:]
author3000_15 = "Peter"

# test 16
train3000_16 = {
    "Matthew": [matthew[13*k:14*k]],
    "Mark": [mark[10*k:11*k]],
    "Luke": [acts[7*k:8*k]],
    "John": [john[6*k:7*k]],
    "Peter": [peter1[-k:]],
    "Jacob": [jacob[:k]],
    "Paul": [corinthians2[6000:9000]]
}
test3000_16 = peter2[:]
author3000_16 = "Peter"

# test 17
train3000_17 = {
    "Matthew": [matthew[-4*k:-3*k]],
    "Mark": [mark[11*k:12*k]],
    "Luke": [acts[8*k:9*k]],
    "John": [revelation[6*k:7*k]],
    "Peter": [peter2[-2*k:-k]],
    "Jacob": [jacob[-k:]],
    "Paul": [galatians[6000:9000]]
}
test3000_17 = romans[:] + thessalonians1[:]
author3000_17 = "Paul"

# test 18
train3000_18 = {
    "Matthew": [matthew[-5*k:-4*k]],
    "Mark": [mark[-2*k:-k]],
    "Luke": [acts[9*k:10*k]],
    "John": [john[6*k:7*k]],
    "Peter": [peter1[-3000:]],
    "Jacob": [jacob[-3000:]],
    "Paul": [thessalonians1[-k:]]
}
test3000_18 = corinthians1[:] + corinthians2[:]
author3000_18 = "Paul"

# test 19
train3000_19 = {
    "Matthew": [matthew[-6*k:-5*k]],
    "Mark": [mark[-12*k:-11*k]],
    "Luke": [acts[10*k:11*k]],
    "John": [john1[:k]],
    "Peter": [peter1[-3*k:-2*k]],
    "Jacob": [jacob[:k]],
    "Paul": [corinthians1[9000:12000]]
}
test3000_19 = galatians[:] + philippians[:]
author3000_19 = "Paul"

# test 20
train3000_20 = {
    "Matthew": [matthew[-6*k:-5*k]],
    "Mark": [mark[12*k:13*k]],
    "Luke": [acts[10*k:11*k]],
    "John": [john1[:k]],
    "Peter": [peter1[-3*k:-2*k]],
    "Jacob": [jacob[-k:]],
    "Paul": [corinthians2[9000:12000]]
}
test3000_20 = philemon[:]
author3000_20 = "Paul"

# test 21
train3000_21 = {
    "Matthew": [matthew[-6*k:-5*k]],
    "Mark": [mark[13*k:14*k]],
    "Luke": [acts[10*k:11*k]],
    "John": [john1[k:2*k]],
    "Peter": [peter2[-2*k:-k]],
    "Jacob": [jacob[-k:]],
    "Paul": [romans[3*k:4*k]]
}
test3000_21 = matthew[-5*k:]
author3000_21 = "Matthew"

# test 22
train3000_22 = {
    "Matthew": [matthew[-7*k:-6*k]],
    "Mark": [mark[14*k:15*k]],
    "Luke": [acts[11*k:12*k]],
    "John": [john1[2*k:3*k]],
    "Peter": [peter1[5000:8000]],
    "Jacob": [jacob[1500:4500]],
    "Paul": [corinthians1[9000:12000]]
}
test3000_22 = acts[:10000]
author3000_22 = "Luke"

# test 23
train3000_23 = {
    "Matthew": [matthew[-8*k:-7*k]],
    "Mark": [mark[15*k:16*k]],
    "Luke": [acts[12*k:13*k]],
    "John": [john1[-k:]],
    "Peter": [peter1[4000:7000]],
    "Jacob": [jacob[4000:7000]],
    "Paul": [galatians[9000:12000]]
}
test3000_23 = john2[:]
author3000_23 = "John"

# test 24
train3000_24 = {
    "Matthew": [matthew[-9*k:-8*k]],
    "Mark": [mark[-2*k:-k]],
    "Luke": [luke[12*k:13*k]],
    "John": [john[-4*k:-3*k]],
    "Peter": [peter2[1000:4000]],
    "Jacob": [jacob[1000:4000]],
    "Paul": [thessalonians1[-k:]]
}
test3000_24 = john1[:]
author3000_24 = "John"

# test 25
train3000_25 = {
    "Matthew": [matthew[-10*k:-9*k]],
    "Mark": [mark[-3*k:-2*k]],
    "Luke": [luke[13*k:14*k]],
    "John": [john1[-2*k:-k]],
    "Peter": [peter1[-k:]],
    "Jacob": [jacob[-k:]],
    "Paul": [philippians[-k:]]
}
test3000_25 = revelation[:]
author3000_25 = "John"

# test 26
train3000_26 = {
    "Matthew": [matthew[-11*k:-10*k]],
    "Mark": [mark[-4*k:-3*k]],
    "Luke": [luke[14*k:15*k]],
    "John": [john1[-3*k:-2*k]],
    "Peter": [peter2[4000:7000]],
    "Jacob": [jacob[2000:5000]],
    "Paul": [thessalonians1[-k:]]
}
test3000_26 = jacob[5000:]
author3000_26 = "Jacob"

# test 27
train3000_27 = {
    "Matthew": [matthew[-12*k:-11*k]],
    "Mark": [mark[-5*k:-4*k]],
    "Luke": [luke[15*k:16*k]],
    "John": [revelation[-6*k:-5*k]],
    "Peter": [peter2[4000:7000]],
    "Jacob": [jacob[4500:7500]],
    "Paul": [philippians[2500:5500]]
}
test3000_27 = mark[:-5*k]
author3000_27 = "Mark"

# test 28
train3000_28 = {
    "Matthew": [matthew[-13*k:-12*k]],
    "Mark": [mark[-6*k:-5*k]],
    "Luke": [luke[16*k:17*k]],
    "John": [revelation[-7*k:-6*k]],
    "Peter": [peter1[1500:4500]],
    "Jacob": [jacob[5500:8500]],
    "Paul": [galatians[-k:]]
}
test3000_28 = peter2[:5000]
author3000_28 = "Peter"

# test 29
train3000_29 = {
    "Matthew": [matthew[-14*k:-13*k]],
    "Mark": [mark[-7*k:-6*k]],
    "Luke": [luke[-17*k:-16*k]],
    "John": [revelation[-8*k:-7*k]],
    "Peter": [peter1[-3000:]],
    "Jacob": [jacob[2500:5500]],
    "Paul": [corinthians2[15000:18000]]
}
test3000_29 = jacob[5500:]
author3000_29 = "Jacob"

# test 30
train3000_30 = {
    "Matthew": [matthew[-15*k:-14*k]],
    "Mark": [mark[-8*k:-7*k]],
    "Luke": [luke[-18*k:-17*k]],
    "John": [john[-8*k:-7*k]],
    "Peter": [peter2[-3000:]],
    "Jacob": [jacob[6500:9500]],
    "Paul": [corinthians1[30000:33000]]
}
test3000_30 = peter1[:] + peter2[:-3000]
author3000_30 = "Peter"

# test 31
train3000_31 = {
    "Matthew": [matthew[-17*k:-16*k]],
    "Mark": [mark[-9*k:-8*k]],
    "Luke": [luke[-19*k:-18*k]],
    "John": [revelation[-8*k:-7*k]],
    "Peter": [peter1[-3000:]],
    "Jacob": [jacob[2500:5500]],
    "Paul": [romans[:3000]]
}
test3000_31 = romans[3000:] + corinthians1[:] + corinthians2[:] + galatians[:] + philippians[:] + thessalonians1[:] + philemon[:]
author3000_31 = "Paul"

# test 32
train3000_32 = {
    "Matthew": [matthew[100000:103000]],
    "Mark": [mark[-k:]],
    "Luke": [luke[110000:113000]],
    "John": [john[50000:53000]],
    "Peter": [peter1[3000:6000]],
    "Jacob": [jacob[4000:7000]],
    "Paul": [galatians[-k:]]
}
test3000_32 = john3[:12000]
author3000_32 = "John"

# final tuples list with test books
tuples_list = [
    (train3000_1, test3000_1, author3000_1, "Matthew"),
    (train3000_2, test3000_2, author3000_2, "Matthew"),
    (train3000_3, test3000_3, author3000_3, "Acts"),
    (train3000_4, test3000_4, author3000_4, "Luke"),
    (train3000_5, test3000_5, author3000_5, "Mark"),
    (train3000_6, test3000_6, author3000_6, "Mark"),
    (train3000_7, test3000_7, author3000_7, "Matthew"),
    (train3000_8, test3000_8, author3000_8, "Mark"),
    (train3000_9, test3000_9, author3000_9, "Luke"),
    (train3000_10, test3000_10, author3000_10, "Jacob"),
    (train3000_11, test3000_11, author3000_11, "John"),
    (train3000_12, test3000_12, author3000_12, "Jacob"),
    (train3000_13, test3000_13, author3000_13, "Jacob"),
    (train3000_14, test3000_14, author3000_14, "1Peter"),
    (train3000_15, test3000_15, author3000_15, "1Peter"),
    (train3000_16, test3000_16, author3000_16, "2Peter"),
    (train3000_17, test3000_17, author3000_17, "Romans, 1Thessalonians"),
    (train3000_18, test3000_18, author3000_18, "1Corinthians, 2Corinthians"),
    (train3000_19, test3000_19, author3000_19, "Galatians, Philippians"),
    (train3000_20, test3000_20, author3000_20, "Philemon"),
    (train3000_21, test3000_21, author3000_21, "Matthew"),
    (train3000_22, test3000_22, author3000_22, "Acts"),
    (train3000_23, test3000_23, author3000_23, "2John"),
    (train3000_24, test3000_24, author3000_24, "1John"),
    (train3000_25, test3000_25, author3000_25, "Revelation"),
    (train3000_26, test3000_26, author3000_26, "Jacob"),
    (train3000_27, test3000_27, author3000_27, "Mark"),
    (train3000_28, test3000_28, author3000_28, "2Peter"),
    (train3000_29, test3000_29, author3000_29, "Jacob"),
    (train3000_30, test3000_30, author3000_30, "1Peter, 2Peter"),
    (train3000_31, test3000_31, author3000_31, "Romans, 1Corinthians, 2Corinthians, Galatians, Philippians, 1Thessalonians, Philemon"),
    (train3000_32, test3000_32, author3000_32, "3John")
]