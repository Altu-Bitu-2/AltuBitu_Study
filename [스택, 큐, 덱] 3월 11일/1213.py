import sys
from collections import Counter

word = list(map(str, sys.stdin.readline().strip()))
word.sort()
check = Counter(word)

cnt = 0 #홀수의 개수
center = "" # 홀수의 문자

for i in check:
    if check[i] % 2 != 0:
        cnt += 1
        center += i
        word.remove(i)
    if cnt > 1:
        break

if cnt > 1:
    print("I'm Sorry Hansoo")

else:

    res = ""
    for i in range(0, len(word), 2):
        res += word[i]

    print(res + center + res[::-1])