first_str = input().lower()
second_str = input().lower()

if first_str == second_str:
    print(0)
elif first_str > second_str:
    print(1)
else:
    print(-1)

# lst1 = []
# lst2 = []
# for character in first_str.lower():
#     lst1.append(ord(character))
# print(lst1)
# print(sum(lst1))
#
# for character in second_str.lower():
#     lst2.append(ord(character))
# print(lst2)
# print(sum(lst2))
#
# if sum(lst1) == sum(lst2):
#     print(0)
# elif sum(lst1) < sum(lst2):
#     print(-1)
# else:
#     print(1)