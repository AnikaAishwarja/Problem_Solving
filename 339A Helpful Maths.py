lst = []
lst = input()
lst2 = []
loop = len(lst)
for i in range(0, loop):
    if "3" >= lst[i] > "0":
        lst2.append(lst[i])

print(lst2)
