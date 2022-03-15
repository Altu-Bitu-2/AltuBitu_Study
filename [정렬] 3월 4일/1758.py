import sys

read = sys.stdin.readline

N = int(read().strip("\n"))

tips = []

for _ in range(N):
    tips.append(int(read().strip("\n")))

tips.sort(reverse=True)
answer = 0

for index, money in enumerate(tips):
    tip = money - ((index + 1) - 1)

    if tip > 0:
        answer += tip

print(answer)