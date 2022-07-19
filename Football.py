# way one
word_number = input()
if ("1"*7) in word_number or ("0"*7) in word_number:
    print("YES")
else:
    print("NO")

# way two
x = "0000000"
y = "1111111"
if x in word_number or y in word_number:
    print("YES")
else:
    print("NO")


#  way three
count = 0
zero = 0
one = 0
for i in word_number:
    if i == "1":
        one += 1
        zero = 0
    else:
        zero += 1
        one = 0
    if zero == 7 or one == 7:
        count = 1

if count == 1:
    print("YES")
else:
    print("NO")
