word = input()
output = ""
count = 0
for ch in word:
    if ch not in output:
        output = output+ch

for i in output:
    count += 1

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")