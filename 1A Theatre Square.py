import math
lst = list(map(int, input().split()))
n = lst[0] #4
m = lst[1] #6
a = lst[2] #4
# print(round(m/a))

f = 0
if a>n and a>m:
    print(1)
elif a % n != 0 and a % m != 0:
    f = math.ceil(n/a) * math.ceil(m / a)
    print(f)
elif a % n != 0 and a % m == 0:
    f = math.ceil(n / a)
    print(f)
elif a % n == 0 and a % m != 0:
    f = (math.ceil(n/a) + math.ceil(m / a))-1
    print(f)
else:
    print(1)

    # if (n % a == 0):
    #     len = n // a
    # else:
    #     len = (n // a) + 1
    #
    # if (m % a == 0):
    #     bre = m // a
    # else:
    #     bre = (m // a) + 1
    #
    # print(len * bre)


