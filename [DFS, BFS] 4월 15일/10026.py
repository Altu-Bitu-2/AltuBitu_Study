import sys
from collections import deque

input = sys.stdin.readline

"""
[적록색약]
그림의 색을 기준으로 구역을 나누는 문제
1. 적록색약이 아닌 사람 기준으로 구역을 나눈다.
2. 그림의 초록을 모두 빨강으로 바꾼 후, 적록색약인 사람 기준으로 구역을 나눈다.
"""


def bfs(i, j, picture, visited): #탐색 함수
    dr = [-1, 1, 0, 0] #row
    dc = [0, 0, -1, 1] #column

    que = deque() #큐 생성
    que.append((i, j)) #큐 추가
    visited[i][j] = True #방문 체크

    while que: #큐가 있을동안
        r, c = que.popleft() #큐 값을 변수에 넣는다
        for x in range(4): #반복
            new_r = r + dr[x] #값 업데이트
            new_c = c + dc[x] #값 업데이트
            
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c]: # 새 좌표가 범위에 맞지 않거나 이미 방문했으면
                continue #건너 뜀
            if picture[new_r][new_c] != picture[r][c]: #업데이트와 달라도 
                continue #건너 뜀
            visited[new_r][new_c] = True #나머진 방문함
            que.append((new_r, new_c)) #큐에 추가

    return #리턴


def count_area(n, picture): #area 세기
    visited = [[False] * n for _ in range(n)] #방문 체크
    area = 0 #area 0으로 초기화

    for i in range(n): #i열
        for j in range(n): #j행 반복문
            if visited[i][j]: #방문 했으면
                continue #건너 뜀

            area += 1 #그렇지 않으면 추가
            bfs(i, j, picture, visited) #bfs 함수 호출

    return area #area 리턴


def green_to_red(n, picture): #초록을 빨강으로 바꾸는 함수
    for i in range(n): #i열
        for j in range(n): #j행 반복문
            if picture[i][j] == 'G': #초록이면
                picture[i][j] = 'R' #빨강으로 바꾸기

    return picture #리턴


# 입력
n = int(input()) #입력
picture = [list(input().rstrip()) for _ in range(n)] #사진 생성
ans = [] #답 넣을 변수

ans.append(count_area(n, picture)) #답에 추가
picture = green_to_red(n, picture) #빨강으로 바꾸기
ans.append(count_area(n, picture)) #답 추가

print(*ans) #답 출력