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
jude = "^" + NP_stripped.jude + "*"


# test 1
train1500_1 = {
    "Matthew": [matthew[:1500]],
    "Mark": [mark[:1500]],
    "Luke": [luke[:1500]],
    "John": [john[:1500]],
    "Peter": [peter1[:1500]],
    "Jacob": [jacob[:1500]],
    "Paul": [romans[:1500]],
    "Jude": [jude[:1500]]
}

test1500_1 = matthew[1500:]
author1500_1 = "Matthew"

# test 2
train1500_2 = {
    "Matthew": [matthew[-1500:]],
    "Mark": [mark[1500:3000]],
    "Luke": [acts[:1500]],
    "John": [john1[:1500]],
    "Peter": [peter2[:1500]],
    "Jacob": [jacob[:1500]],
    "Paul": [corinthians1[:1500]],
    "Jude": [jude[:1500]]
}

test1500_2 = matthew[:-1500]
author1500_2 = "Matthew"

# test 3
train1500_3 = {
    "Matthew": [matthew[1500:3000]],
    "Mark": [mark[1500:3000]],
    "Luke": [luke[1500:3000]],
    "John": [john[1500:3000]],
    "Peter": [peter1[1500:3000]],
    "Jacob": [jacob[1500:3000]],
    "Paul": [romans[1500:3000]],
    "Jude": [jude[:1500]]
}

test1500_3 = acts[-70000:]
author1500_3 = "Luke"

# test 4
train1500_4 = {
    "Matthew": [matthew[3000:4500]],
    "Mark": [mark[3000:4500]],
    "Luke": [acts[1500:3000]],
    "John": [john1[1500:3000]],
    "Peter": [peter2[1500:3000]],
    "Jacob": [jacob[-1500:]],
    "Paul": [corinthians1[1500:3000]],
    "Jude": [jude[:1500]]
}

test1500_4 = luke[-70000:]
author1500_4 = "Luke"

# test 5
train1500_5 = {
    "Matthew": [matthew[4500:6000]],
    "Mark": [mark[-1500:]],
    "Luke": [acts[2000:3500]],
    "John": [revelation[:1500]],
    "Peter": [peter1[3000:4500]],
    "Jacob": [jacob[2000:3500]],
    "Paul": [corinthians2[:1500]],
    "Jude": [jude[:1500]]
}

test1500_5 = mark[:-1500]
author1500_5 = "Mark"

# test 6
train1500_6 = {
    "Matthew": [matthew[6000:7500]],
    "Mark": [mark[:1500]],
    "Luke": [luke[2000:3500]],
    "John": [john[-1500:]],
    "Peter": [peter2[3000:4500]],
    "Jacob": [jacob[-1500:]],
    "Paul": [thessalonians1[:1500]],
    "Jude": [jude[:1500]]
}

test1500_6 = mark[1500:]
author1500_6 = "Mark"

# test 7
train1500_7 = {
    "Matthew": [matthew[7500:9000]],
    "Mark": [mark[2000:3500]],
    "Luke": [acts[4500:6000]],
    "John": [john1[-1500:]],
    "Peter": [peter1[4500:6000]],
    "Jacob": [jacob[-1500:]],
    "Paul": [galatians[:1500]],
    "Jude": [jude[:1500]]
}

test1500_7 = matthew[:7500]
author1500_7 = "Matthew"

# test 8
train1500_8 = {
    "Matthew": [matthew[9000:10500]],
    "Mark": [mark[3500:5000]],
    "Luke": [luke[4500:6000]],
    "John": [john[4500:6000]],
    "Peter": [peter2[4500:6000]],
    "Jacob": [jacob[3500:5000]],
    "Paul": [philippians[:1500]],
    "Jude": [jude[:1500]]
}

test1500_8 = mark[-5000:]
author1500_8 = "Mark"

# test 9
train1500_9 = {
    "Matthew": [matthew[11000:12500]],
    "Mark": [mark[5000:6500]],
    "Luke": [acts[6000:7500]],
    "John": [revelation[6000:7500]],
    "Peter": [peter1[6000:7500]],
    "Jacob": [jacob[6000:7500]],
    "Paul": [galatians[:1500]],
    "Jude": [jude[-1500:]]
}

test1500_9 = luke[:70000]
author1500_9 = "Luke"

# test 10
train1500_10 = {
    "Matthew": [matthew[12500:14000]],
    "Mark": [mark[5000:6500]],
    "Luke": [acts[6000:7500]],
    "John": [john1[6000:7500]],
    "Peter": [peter2[-1500:]],
    "Jacob": [jacob[6000:7500]],
    "Paul": [romans[-1500:]],
    "Jude": [jude[-1500:]]
}

test1500_10 = jacob[:6000]
author1500_10 = "Jacob"

# test 11
train1500_11 = {
    "Matthew": [matthew[14000:15500]],
    "Mark": [mark[6500:8000]],
    "Luke": [acts[7500:9000]],
    "John": [john1[7500:9000]],
    "Peter": [peter2[:1500]],
    "Jacob": [jacob[:1500]],
    "Paul": [corinthians1[-1500:]],
    "Jude": [jude[-1500:]]
}

test1500_11 = revelation[:]
author1500_11 = "John"

# test 12
train1500_12 = {
    "Matthew": [matthew[17000:18500]],
    "Mark": [mark[10500:12000]],
    "Luke": [acts[9000:10500]],
    "John": [john[9000:10500]],
    "Peter": [peter1[9000:10500]],
    "Jacob": [jacob[-1500:]],
    "Paul": [philippians[-1500:]],
    "Jude": [jude[-1500:]]
}

test1500_12 = jacob[:1500]
author1500_12 = "Jacob"

# test 13
train1500_13 = {
    "Matthew": [matthew[15500:17000]],
    "Mark": [mark[9000:10500]],
    "Luke": [luke[7500:9000]],
    "John": [john[7500:9000]],
    "Peter": [peter1[7500:9000]],
    "Jacob": [jacob[:1500]],
    "Paul": [philemon[-1500:]],
    "Jude": [jude[-1500:]]
}

test1500_13 = jacob[1500:]
author1500_13 = "Jacob"

# test 14
train1500_14 = {
    "Matthew": [matthew[17000:18500]],
    "Mark": [mark[10500:12000]],
    "Luke": [acts[9000:10500]],
    "John": [john1[9000:10500]],
    "Peter": [peter2[-1500:]],
    "Jacob": [jacob[-1500:]],
    "Paul": [romans[3000:4500]],
    "Jude": [jude[-1500:]]
}

test1500_14 = peter1[:]
author1500_14 = "Peter"

# test 15
train1500_15 = {
    "Matthew": [matthew[18500:20000]],
    "Mark": [mark[12000:13500]],
    "Luke": [acts[10500:12000]],
    "John": [john[10500:12000]],
    "Peter": [peter2[:1500]],
    "Jacob": [jacob[3000:4500]],
    "Paul": [corinthians1[3000:4500]],
    "Jude": [jude[-1500:]]
}

test1500_15 = peter1[:]
author1500_15 = "Peter"

# test 16
train1500_16 = {
    "Matthew": [matthew[20000:21500]],
    "Mark": [mark[13500:15000]],
    "Luke": [luke[10500:12000]],
    "John": [john[10500:12000]],
    "Peter": [peter1[-1500:]],
    "Jacob": [jacob[:1500]],
    "Paul": [corinthians2[3000:4500]],
    "Jude": [jude[-1500:]]
}

test1500_16 = peter2[:]
author1500_16 = "Peter"

# test 17
train1500_17 = {
    "Matthew": [matthew[21500:23000]],
    "Mark": [mark[15000:16500]],
    "Luke": [acts[12000:13500]],
    "John": [john1[:1500]],
    "Peter": [peter2[-1500:]],
    "Jacob": [jacob[-1500:]],
    "Paul": [galatians[3000:4500]],
    "Jude": [jude[-1500:]]
}

test1500_17 = jude[:1500]
author1500_17 = "Jude"

# test 18
train1500_18 = {
    "Matthew": [matthew[23000:24500]],
    "Mark": [mark[16500:18000]],
    "Luke": [luke[12000:13500]],
    "John": [john[-1500:]],
    "Peter": [peter1[-1500:]],
    "Jacob": [jacob[-1500:]],
    "Paul": [thessalonians1[3000:4500]],
    "Jude": [jude[:1500]]
}

test1500_18 = jude[-1500:]
author1500_18 = "Jude"

# test 19
train1500_19 = {
    "Matthew": [matthew[24500:26000]],
    "Mark": [mark[18000:19500]],
    "Luke": [luke[13500:15000]],
    "John": [john[13500:15000]],
    "Peter": [peter1[2000:3500]],
    "Jacob": [jacob[:1500]],
    "Paul": [corinthians1[4500:6000]],
    "Jude": [jude[:1500]]
}

test1500_19 = romans[:] + thessalonians1[:]
author1500_19 = "Paul"

# test 20
train1500_20 = {
    "Matthew": [matthew[26000:27500]],
    "Mark": [mark[19500:21000]],
    "Luke": [luke[15000:16500]],
    "John": [revelation[15000:16500]],
    "Peter": [peter1[3500:5000]],
    "Jacob": [jacob[3500:5000]],
    "Paul": [corinthians2[4500:6000]],
    "Jude": [jude[-1500:]]
}

test1500_20 = peter2[:5000]
author1500_20 = "Peter"

# test 21
train1500_21 = {
    "Matthew": [matthew[27500:29000]],
    "Mark": [mark[21000:22500]],
    "Luke": [acts[15000:16500]],
    "John": [john[16500:18000]],
    "Peter": [peter1[5000:6500]],
    "Jacob": [jacob[5000:6500]],
    "Paul": [romans[4500:6000]],
    "Jude": [jude[-1500:]]
}

test1500_21 = corinthians2[:] + corinthians1
author1500_21 = "Paul"

# test 22
train1500_22 = {
    "Matthew": [matthew[29000:30500]],
    "Mark": [mark[22500:24000]],
    "Luke": [acts[16500:18000]],
    "John": [revelation[18000:19500]],
    "Peter": [peter1[6500:8000]],
    "Jacob": [jacob[6500:8000]],
    "Paul": [corinthians1[4500:6000]],
    "Jude": [jude[-1500:]]
}

test1500_22 = galatians[:] + philippians[:]
author1500_22 = "Paul"

# test 23
train1500_23 = {
    "Matthew": [matthew[70000:71500]],
    "Mark": [mark[40000:41500]],
    "Luke": [luke[100000:101500]],
    "John": [revelation[30000:31500]],
    "Peter": [peter1[1000:2500]],
    "Jacob": [jacob[7000:8500]],
    "Paul": [galatians[4000:5500]],
    "Jude": [jude[1500:3000]]
}

test1500_23 = jude[:1000]
author1500_23 = "Jude"

# test 24
train1500_24 = {
    "Matthew": [matthew[60000:61500]],
    "Mark": [mark[60000:61500]],
    "Luke": [luke[25000:25500]],
    "John": [revelation[-1500:]],
    "Peter": [peter2[1000:2500]],
    "Jacob": [jacob[5000:6500]],
    "Paul": [thessalonians1[4000:5500]],
    "Jude": [jude[1500:3000]]
}

test1500_24 = jacob[:5000]
author1500_24 = "Jacob"

# test 25
train1500_25 = {
    "Matthew": [matthew[33500:35000]],
    "Mark": [mark[27000:28500]],
    "Luke": [acts[18000:19500]],
    "John": [revelation[21000:22500]],
    "Peter": [peter2[1500:3000]],
    "Jacob": [jacob[1500:3000]],
    "Paul": [philippians[4500:6000]],
    "Jude": [jude[-1500:]]
}

test1500_25 = philemon[:]
author1500_25 = "Paul"

# test 26
train1500_26 = {
    "Matthew": [matthew[35000:36500]],
    "Mark": [mark[28500:30000]],
    "Luke": [acts[19500:21000]],
    "John": [revelation[22500:24000]],
    "Peter": [peter2[3000:4500]],
    "Jacob": [jacob[-1500:]],
    "Paul": [philippians[6000:7500]],
    "Jude": [jude[:1500]]
}

test1500_26 = matthew[36500:]
author1500_26 = "Matthew"

# test 27
train1500_27 = {
    "Matthew": [matthew[35000:36500]],
    "Mark": [mark[30000:31500]],
    "Luke": [luke[19500:21000]],
    "John": [john[22500:24000]],
    "Peter": [peter2[4500:6000]],
    "Jacob": [jacob[4500:6000]],
    "Paul": [thessalonians1[6000:7500]],
    "Jude": [jude[:1500]]
}

test1500_27 = mark[31500:]
author1500_27 = "Mark"

# test 28
train1500_28 = {
    "Matthew": [matthew[36500:38000]],
    "Mark": [mark[31000:32500]],
    "Luke": [luke[21000:22500]],
    "John": [revelation[22500:24000]],
    "Peter": [peter2[-1500:]],
    "Jacob": [jacob[:1500]],
    "Paul": [galatians[6000:7500]],
    "Jude": [jude[:1500]]
}

test1500_28 = acts[:70000]
author1500_28 = "Luke"

# test 29
train1500_29 = {
    "Matthew": [matthew[38000:39500]],
    "Mark": [mark[32500:34000]],
    "Luke": [acts[21000:22500]],
    "John": [revelation[24000:25500]],
    "Peter": [peter1[-1500:]],
    "Jacob": [jacob[6000:7500]],
    "Paul": [romans[6000:7500]],
    "Jude": [jude[:1500]]
}

test1500_29 = john[:]
author1500_29 = "John"

# test 30
train1500_30 = {
    "Matthew": [matthew[39500:41000]],
    "Mark": [mark[34000:35500]],
    "Luke": [luke[21000:22500]],
    "John": [revelation[-1500:]],
    "Peter": [peter1[4000:5500]],
    "Jacob": [jacob[4000:5500]],
    "Paul": [corinthians1[4000:5500]],
    "Jude": [jude[:1500]]
}

test1500_30 = john1[:]
author1500_30 = "John"

# test 31
train1500_31 = {
    "Matthew": [matthew[41000:42500]],
    "Mark": [mark[35500:37000]],
    "Luke": [luke[22500:24000]],
    "John": [john1[-1500:]],
    "Peter": [peter1[4000:5500]],
    "Jacob": [jacob[3000:4500]],
    "Paul": [corinthians2[4000:5500]],
    "Jude": [jude[500:2000]]
}

test1500_31 = jude[2000:]
author1500_31 = "Jude"

# test 32
train1500_32 = {
    "Matthew": [matthew[50000:51500]],
    "Mark": [mark[50000:51500]],
    "Luke": [luke[25000:25500]],
    "John": [revelation[-1500:]],
    "Peter": [peter1[500:2000]],
    "Jacob": [jacob[3000:4500]],
    "Paul": [corinthians2[4000:5500]],
    "Jude": [jude[1500:3000]]
}

test1500_32 = john2[:] + john3[:]
author1500_32 = "John"

tuples_list = [
    (train1500_1, test1500_1, author1500_1, "Matthew"),
    (train1500_2, test1500_2, author1500_2, "Matthew"),
    (train1500_3, test1500_3, author1500_3, "Acts"),
    (train1500_4, test1500_4, author1500_4, "Luke"),
    (train1500_5, test1500_5, author1500_5, "Mark"),
    (train1500_6, test1500_6, author1500_6, "Mark"),
    (train1500_7, test1500_7, author1500_7, "Matthew"),
    (train1500_8, test1500_8, author1500_8, "Mark"),
    (train1500_9, test1500_9, author1500_9, "Luke"),
    (train1500_10, test1500_10, author1500_10, "Jacob"),
    (train1500_11, test1500_11, author1500_11, "Revelation"),
    (train1500_12, test1500_12, author1500_12, "Jacob"),
    (train1500_13, test1500_13, author1500_13, "Jacob"),
    (train1500_14, test1500_14, author1500_14, "1 Peter"),
    (train1500_15, test1500_15, author1500_15, "1 Peter"),
    (train1500_16, test1500_16, author1500_16, "2 Peter"),
    (train1500_17, test1500_17, author1500_17, "Jude"),
    (train1500_18, test1500_18, author1500_18, "Jude"),
    (train1500_19, test1500_19, author1500_19, "Romans, 1 Thessalonians"),
    (train1500_20, test1500_20, author1500_20, "2 Peter"),
    (train1500_21, test1500_21, author1500_21, "2 Corinthians, 1 Corinthians"),
    (train1500_22, test1500_22, author1500_22, "Galatians, Philippians"),
    (train1500_23, test1500_23, author1500_23, "Jude"),
    (train1500_24, test1500_24, author1500_24, "Jacob"),
    (train1500_25, test1500_25, author1500_25, "Philemon"),
    (train1500_26, test1500_26, author1500_26, "Matthew"),
    (train1500_27, test1500_27, author1500_27, "Mark"),
    (train1500_28, test1500_28, author1500_28, "Acts"),
    (train1500_29, test1500_29, author1500_29, "John"),
    (train1500_30, test1500_30, author1500_30, "1 John"),
    (train1500_31, test1500_31, author1500_31, "Jude"),
    (train1500_32, test1500_32, author1500_32, "2 John, 3 John")
]