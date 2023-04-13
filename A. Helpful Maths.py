s = input()

num = list(map(str, s.split("+")))

num=sorted(num)

result_string = '+'.join(str(nums) for nums in num)
print(result_string)