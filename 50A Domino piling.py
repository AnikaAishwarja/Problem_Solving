board_length, board_width = list(map(int,input().split()))
area = board_length * board_width

if 1 <= board_length <= 16 and 1 <= board_width <= 16:
    print(area//2)
else:
    print(0)