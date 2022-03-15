import sys

input = sys.stdin.readline #입력 받기

# ver1) 셋을 이용한 풀이입니다.


t = int(input()) #변수 t에 정수형으로 저장 (개수)

for _ in range(t): #개수 동안
    # 입력
    n = int(input())# 정수 개수
    note1 = set(map(int, input().split())) #수첩1 set
    m = int(input()) #정수 개수
    note2 = list(map(int, input().split())) #수첩2 set

    # note2에 있는 숫자를 하나씩 꺼내 note1에 있는지 비교합니다.
    for num in note2: #수첩2 개수동안
        if num in note1: #있다면
            print(1) #1출력
        else:#없다면
            print(0)#0출력