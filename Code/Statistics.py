from collections import Counter

f = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/label.txt', 'r')

lst = []
line = f.readlines()[0].strip()
for c in line:
    if c != ' ':
        lst.append(int(c))
print(len(lst))
lst = Counter(lst)
print(lst)