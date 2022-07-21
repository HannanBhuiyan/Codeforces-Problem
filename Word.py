s = input()
lower = 0
upper = 0
for i in range(0, len(s)):
    if s[i].islower():
        lower += 1
    else:
        upper += 1

if lower == upper:
    print(s.lower())
elif lower > upper:
    print(s.lower())
elif upper > lower:
    print(s.upper())
