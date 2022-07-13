loop = int(input())
lst = []
count = 0
for i in range(0,loop):
    lst = list(map(int, input().split()))
    if lst.count(1) >= 2:
        count = count + 1
print(count)













