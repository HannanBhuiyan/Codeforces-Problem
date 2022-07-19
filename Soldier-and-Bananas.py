num = list(map(int, input().split()))
sum = 0
for i in range(1, num[2]+1):
    sum += i

d = (sum*num[0]) - num[1]
if d < 0:
    print("0")
else:
    print(d)
