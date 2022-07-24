number_of_array = list(map(int, input().split()))
score_array = list(map(int, input().split()))
participant_number = number_of_array[0]
temp = score_array[number_of_array[-1] - 1]
winer = 0
for i in range(0, len(score_array)):
    if score_array[i] >= temp and score_array[i] > 0:
        winer += 1
print(winer)