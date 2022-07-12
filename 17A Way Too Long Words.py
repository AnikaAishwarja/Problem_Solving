i = int(input())
lst = []
for x in range(0, i):
    lst.append(input())

for y in range(0, i):
    word=lst[y]
    length = len(word)
    if length <= 10:
        print(word)
    else:
        print(word[0], length - 2, word[length - 1], sep='')