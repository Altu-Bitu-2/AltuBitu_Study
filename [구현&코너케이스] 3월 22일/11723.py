import sys
input = sys.stdin.readline

"""
[집합] - 단순 구현 문제
ver2. 비스마스크 풀이
 1. true or false 라는 2가지 상태는 0 or 1로 나타낼 수 있음 (=이진수)
 2. int형에 담을 수 있는 가장 큰 수는 2^31-1 이고, 입력으로 들어오는 수는 최대 20이므로 비트마스크 사용 가능
 ex)
 0000 0000 0000 0000 0000 0010 => {1}
 0001 1111 1111 1111 1111 1110 => {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
 0000 0000 0000 0010 0000 1010 => {1, 3, 9}
 비트마스크에 대해 따로 알아보는걸 추천합니다.
"""

SIZE = 21 #SIZE는 21
m = int(input()) #m에 입력 값을 정수로 대입
s = 0 #s는 0으로 초기화

for _ in range(m): #m인 동안
    cmd = input().split() #cmd에 입력값 넣기

    if len(cmd) == 1: #cmd 길이가 1인 경우
        if (cmd[0] == "all"): # cmd가 all인 경우
            s = (1 << SIZE) - 1 #s값 계산
        else: #그렇지 않다면
            s = 0 #s는 0
        continue #계속
    else: #cmd 길이가 1이 아닌 경우
        num = int(cmd[1]) #num 는 cmd를 정수로 대입

    if cmd[0] == "add":     # OR 연산
        s |= (1 << num) #s 연산
    elif cmd[0] == "remove":    # NOT 연산 후 AND 연산
        s &= ~(1 << num) #s 연산
    elif cmd[0] == "check":     # AND 연산
        if s & (1 << num): #0이 아닌경우
            print(1) #1출력
        else: #0인경우
            print(0) #0출력
    elif cmd[0] == "toggle":    # XOR 연산
        s ^= (1 << num) #연산