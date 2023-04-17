num = int(input())
stone = input()
count = 0

if len(stone) == num:
    for i in range(1, num):
        if stone[i] == stone[i - 1]:
            count += 1

    print(count)
