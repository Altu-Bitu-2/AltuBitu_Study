from sys import stdin
from collections import deque
N = int(stdin.readline())
card = list(map(int, stdin.readline().split()))

result = deque()

for i in range(N):
    if card[N-i-1] == 1:
        result.appendleft(i+1)
    elif card[N-i-1] == 2:
        result.insert(1,i+1)
    elif card[N-i-1] == 3:
        result.append(i+1)

print(*result)