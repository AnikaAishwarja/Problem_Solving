participant, cutoff = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
if participant >= cutoff:
    for i in range(0,len(lst)):
     if lst[i]>0 and lst[i]>= lst[cutoff-1]:
         count +=1

print(count)