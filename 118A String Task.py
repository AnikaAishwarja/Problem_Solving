s = input().lower()
dot = '.'
vowel = ['a', 'e', 'i', 'o', 'u','y']
add = ''
output = []

for element in s:
    if element not in vowel:
        output.append(dot)
        output.append(element)

print(add.join(output))
