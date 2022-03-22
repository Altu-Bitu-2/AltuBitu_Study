import sys #변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline #입력받기

"""
[외계인의 기타연주]
각 줄마다 외계인이 누르고 있는 프렛을 스택에 저장하기
매 입력에 대해 이번에 누를 프렛이 해당 줄에서 가장 높은 프렛이어야 함
1. 이번에 눌러야 할 프렛보다 높은 프렛에서 손가락을 전부 떼기
2. 만약 이번에 눌러야 할 프렛을 누르고 있지 않다면 누르기
"""

n, p = map(int, input().split()) #입력받아 변수 n,k에 저장
stack = [[0] for _ in range(7)]  # 1번 줄부터 6번줄 까지
answer = 0 # 매번 스택이 비었는지 확인할 필요 없도록 미리 0번을 스택에 넣어 둠

for _ in range(n): #n번 반복
    # 입력
    line, fret = map(int, input().split()) #입력받아 line, fret에 저장

    # 연산
    while stack[line][-1] > fret:    # 프렛에서 손가락 떼기
        stack[line].pop() #스택에서 맨 마지막 요소를 돌려주고 그 요소는 삭제
        answer += 1 #스택 개수 증가 표기
    if stack[line][-1] != fret:    # 프렛 누르기
        stack[line].append(fret) #스택에 프렛 주가 저장
        answer += 1 #스택 개수 증가 표기

# 출력
print(answer)#정답 출력