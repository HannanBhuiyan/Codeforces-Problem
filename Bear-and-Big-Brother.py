array_num = input().split()
l = int(array_num[0])
b = int(array_num[1])
count = 0
while(l <= b):
    l *= 3
    b *= 2
    count += 1

print(count)


