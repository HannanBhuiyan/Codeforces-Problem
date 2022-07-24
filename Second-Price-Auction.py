b = int(input())
arr = list(map(int, input().split()))
max_num = 0
for i in range(len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]

def secondmax(arr):
  sublist = [x for x in arr if x < max(arr)]
  return max(sublist)

print(arr.index(max_num)+1, secondmax(arr))


