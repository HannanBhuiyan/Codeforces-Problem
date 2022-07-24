n = int(input())
still_now = 0
capacity = 0
for i in range(0, n):
    pout, pin = map(int, input().split())
    still_now -= pout
    still_now += pin
    capacity = max(still_now, capacity)
print(capacity)



 
