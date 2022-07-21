number_array = input().split()

n = int(number_array[0])
k = int(number_array[1])
for i in range(0, k):
    r = n%10
    if r == 0:
        n //= 10
    else:
        n -= 1
print(n)

