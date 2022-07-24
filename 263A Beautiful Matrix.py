matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row = i
            column = j


out = abs(row-2)+abs(column-2)
print(out)
