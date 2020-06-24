from sys import *
n = int(stdin.readline())
list_scores = []
list_ranks = []
for j in range(n):
    score, rank = map(float, stdin.readline().split())
    list_scores.append(score)
    list_ranks.append(rank)
list_scores.sort(reverse=True)
list_ranks.sort()
p_score = float(stdin.readline())
times = list_scores.index(p_score) 
rank_init = 1
rank_avg = list_ranks[0]
for x in range(times):
    rank_avg = list_ranks[x]
    rank_init = 2 * rank_avg - rank_init + 1
if times == 0:
    rank_last = 2 * rank_avg - rank_init
else:
    rank_last = 2 * list_ranks[x+1] - rank_init
print(int(rank_init))
print(int(rank_last))