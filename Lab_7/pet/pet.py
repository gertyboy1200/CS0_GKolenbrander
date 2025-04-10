max_score = 0
winner = 0

for i in range(5):
    scores = list(map(int,input().split()))
    total = sum(scores)
    if total > max_score:
        max_score = total
        winner = i + 1

print(winner, max_score)
