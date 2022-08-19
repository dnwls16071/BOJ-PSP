# You record all of the scoring activity at a basketball game. Points are scored by a 3-point shot, a 2-point field goal, or a 1-point free throw.

# You know the number of each of these types of scoring for the two teams: the Apples and the Bananas. Your job is to determine which team won, or if the game ended in a tie.

Apple = []
for i in range(3):
    Apple.append(int(input()))

Banana = []
for i in range(3):
    Banana.append(int(input()))

Apple_score = 0
for i in range(len(Apple)):
    Apple_score += Apple[i] * (len(Apple) - i)

Banana_score = 0
for i in range(len(Banana)):
    Banana_score += Banana[i] * (len(Banana) - i)

if Apple_score > Banana_score:
    print("A")
elif Apple_score < Banana_score:
    print("B")
else:
    print("T")