import sys

input = sys.stdin.readline

"""
[분산처리]
- a^b의 일의 자리를 구하는 문제
- 일의 자리는 0~9 중 하나 이므로, 어떤 수를 계속 곱해 나가면 일의 자리는 패턴을 가지게 되어 있음
    ex) 2 -> 4 -> 8 -> 6 -> 2 ... 
- 0~9까지 일의 자리 패턴을 미리 구한 후, (b % 패턴의 길이)번째 수를 출력하면 된다.
- 0이 나올 경우 10번 컴퓨터가 처리하므로, 0이 출력되지 않도록 예외처리
"""

last_digit = [[i] for i in range(10)]  # 0부터 9까지의 패턴
size = []  # 패턴의 길이

for i in range(10):#10번 반복문
    temp = i #temp 변수에 i를 대입
    while i != (temp * i) % 10: #i에 i를 곱한뒤 일의자리 수가 같지 않은 경우
        temp *= i #temp는 temp에 i를 곱한 값
        temp %= 10 #temp는 십으로 나눈 값
        last_digit[i].append(temp) #일의자리수
    size.append(len(last_digit[i])) #합치기

# 입력
t = int(input())# 입력

# 입력 + 연산
for _ in range(t): #t인 동안
    a, b = map(int, input().split())#a,b에 대입
    a %= 10 #일의자리수가 a

    if a == 0: #a가 0이면
        print(10) #10출력
        continue #계속 이어서

    print(last_digit[a][b % size[a] - 1])#정답 출력