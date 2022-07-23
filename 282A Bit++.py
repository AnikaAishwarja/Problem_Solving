num_of_statements = int(input())
lst = []
count = 0
for i in range(0, num_of_statements):
    ele = str(input())
    if ele == "++X" or ele == "X++":
        count = count + 1
    else:
        count = count - 1

print(count)
