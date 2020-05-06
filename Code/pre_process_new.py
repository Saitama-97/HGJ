# f1 = open('raw_label.txt', 'r')
# f2 = open('label.txt', 'w')
# lst = []
# i = 0
# for line in f1:
#     if 'Branch-0' in line:
#         line = line.split(',[')[1]
#         line = line.strip().replace(',', '')
#         # print(line)
#         for c in line:
#             if c != ' ':
#                 # print(c, end='')
#                 lst.append(c)
#         # print(i)
# for item in lst:
#     f2.write(item + ' ')
#     i += 1
# print(i)
# 1477850

# f1 = open('raw_pred.txt', 'r')
# f2 = open('pred.txt', 'w')
# lst = []
# for line in f1:
#     if 'Branch-0,' in line:
#         line = line.split(',[')[1]
#         line = line.strip().replace(',', '')
#         # print(line)
#         for c in line:
#             if c != ' ':
#                 lst.append(c)
# i = 0
# for item in lst:
#     f2.write(item + ' ')
#     i += 1
# print(i)


f = open('label.txt', 'r')
line = f.readlines()
print(line)
lst = []
for c in line:
    if c != ' ':
        lst.append(c)
print(len(lst))
print(lst)
