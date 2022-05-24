import sys
from collections import deque

input = sys.stdin.readline

"""
[숨바꼭질]
 x좌표 위에서 x-1, x+1, 2*x의 위치로 계속 이동하며 탐색
 가장 빠른 시간을 찾아야 하므로 주변 노드부터 탐색하는 풀이로 풀어서 k에 도달하면 바로 탐색 종료 (bfs)
"""
SIZE = 10 ** 5 #크기 10의 5승


def bfs(n, k): #bfs 함수
    time = [-1] * (SIZE + 1) #시간
    que = deque() #큐 선정
    que.append(n) #큐 초기화
    time[n] = 0 #시간 초기화

    while que: #큐 반복
        curr = que.popleft()#큐 왼쪽을 팝 시킴
        if curr == k: # 값이 k이면
            return time[curr] #걸린 시간 리턴

        for next in (curr * 2, curr + 1, curr - 1): #반복
            if next < 0 or next > SIZE or time[next] > -1: #만약 아직 값이 남아있다면
                continue #계속
            time[next] = time[curr] + 1 #시간 측정(1씩 더함)
            que.append(next) #다음 큐


n, k = map(int, input().split()) # 입력

print(bfs(n, k)) # 연산 + 출력