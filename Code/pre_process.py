import time

# f1 = open('old_label.txt', 'r')
# f2 = open('old_label.txt', 'w')
# for line in f1:
#     line = line.replace(',', '').strip()
#     # line.strip()
#     print(line)
#     f2.write(line + ' ')

# f1 = open('old_pred.txt', 'r')
# f2 = open('old_pred.txt', 'w')
# for line in f1:
#     line = line.replace(',', '').strip()
#     # line.strip()
#     print(line)
#     f2.write(line + ' ')

# f = open('../Code/old_label.txt', 'r')
# lst = []
# for c in f:
#     for i in c:
#         if i != ' ':
#             print(i)
#             lst.append(int(i))
# print(len(lst), lst)

# f1 = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/raw_label.txt', 'r')
# f2 = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/raw_label.txt', 'w')
# lst = []
# for line in f1:
#     line = line.replace("], device='cuda:0')", '')
#     if 'Branch-' in line:
#         line = line.split('[')[1]
#     line = line.strip().replace(',', '')
#     for c in line:
#         if c != ' ':
#             lst.append(c)
#             f2.write(c + ' ')
#         # print()
# print(len(lst))
# print(lst[:10])
# print(lst[-1])
# print(lst[-10:-1])


f1 = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/pred1.txt', 'r')
# f2 = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/raw_pred.txt', 'w')
lines = f1.readlines()
lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []
lst8 = []
lst9 = []

for line in lines:
    line = line.strip().split(',[')
    branch = line[0]
    value = line[1]
    # print(branch, value)
    if branch == 'Branch-0':
        lst1.append(value)
    elif branch == 'Branch-1':
        lst2.append(value)
    elif branch == 'Branch-2':
        lst3.append(value)
    elif branch == 'Branch-3':
        lst4.append(value)
    elif branch == 'Branch-4':
        lst5.append(value)
    elif branch == 'Branch-5':
        lst6.append(value)
    elif branch == 'Branch-6':
        lst7.append(value)
    elif branch == 'Branch-7':
        lst8.append(value)
    elif branch == 'Branch-8':
        lst9.append(value)

lst = []

for i in range(len(lst1)):
    lst.append(lst1[i])

for i in range(len(lst2)):
    if i % 2 == 0:
        lst.append(lst2[i])

for i in range(len(lst3)):
    if i % 3 == 0:
        lst.append(lst3[i])

for i in range(len(lst4)):
    if i % 4 == 0:
        lst.append(lst4[i])

for i in range(len(lst5)):
    if i % 5 == 0:
        lst.append(lst5[i])

for i in range(len(lst6)):
    if i % 6 == 0:
        lst.append(lst6[i])

for i in range(len(lst7)):
    if i % 7 == 0:
        lst.append(lst7[i])

for i in range(len(lst8)):
    if i % 8 == 0:
        lst.append(lst8[i])

for i in range(len(lst9)):
    if i % 9 == 0:
        lst.append(lst9[i])
ret = []
for item in lst:
    for c in item:
        if c != ',' and c != ' ':
            ret.append(c)
            f2.write(c + ' ')
print(len(ret))
