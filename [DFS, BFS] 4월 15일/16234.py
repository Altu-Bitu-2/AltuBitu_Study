import sys
from collections import deque

input = sys.stdin.readline

"""
[인구이동]
0. 인구이동이 일어날 수 있는 나라(처음에는 모든 나라)의 좌표를 좌표 큐에 저장
1. bfs 탐색을 통해 연합을 확인하고, 연합에 포함된 나라의 인구이동을 진행한다.
2. 인구 이동이 있었던 나라는 다음 날에도 인구이동이 시작될 수 있으므로 좌표 큐에 다시 넣어준다.
    -> 직전 이동이 있었던 나라에 대해서만 bfs 탐색 진행
    - 인구 이동이 일어나지 않은 두 나라 사이에서는 다음 날에도 인구이동이 일어날 수 없음
3. 인구이동이 전혀 일어나지 않을 때까지 반복
"""


def bfs(n, left, right, i, j, day): #탐색
    dr = [-1, 1, 0, 0] #row
    dc = [0, 0, -1, 1] #column

    que = deque() #큐 생성
    que.append((i, j)) #큐 추가
    total = 0  # 연합의 인구 수 합계
    count = 0  # 연합에 포함된 나라의 수
    cord = []  # 연합에 포함된 나라의 좌표

    while que: #큐가 있는 동안
        r, c = que.popleft() #큐 값 하나씩 넣음
        count += 1 #개수 추가
        total += board[r][c] #전체 합
        cord.append((r, c)) #r,c 쌍 추가

        for x in range(4): #반복문
            new_r = r + dr[x] #r 값 업데이트
            new_c = c + dc[x] #c 값 업데이트
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c] == day: # 새 좌표가 범위에 맞지 않거나 이미 방문했으면
                continue #건너 뜀

            # 이 때 여기서 visited에 표기를 하면 안됨
            # 현재는 조건에 맞지 않지만, 이후에 연합에 있는 다른 나라에 의해 연합에 들어올 수 있음

            if left <= abs(board[new_r][new_c] - board[r][c]) <= right: #차이의 절대값이 왼쪽 오른쪽 사이이면
                que.append((new_r, new_c)) #큐에 추가
                visited[new_r][new_c] = day #방문 표시

    # 적어도 나라 2개 이상이 모여야 연합을 이루었다고 볼 수 있음
    if count > 1: #수가 1보다 크면
        avg = total // count #평균은 총 합에 수를 나눔
        # 인구 이동
        for r, c in cord: #반복문
            board[r][c] = avg #평균을 기록
            # 인구의 이동이 있는 나라는 다음 이동이 시작될 가능성이 있음
            countries.append((r, c)) #나라에 추가

    return count > 1 #리턴


def simulation(n, left, right): #가상 함수
    day = 0 #날을 0으로 초기화
    while True: #참인 동안
        size = len(countries)  # 이번에 탐색할 수 있는 나라의 수
        flag = False #깃발 내리려두기
        day += 1 #날 1씩 추가
        for _ in range(size): #나라수 만큼 반복
            i, j = countries.popleft() #나라의 값 변수에 넣기
            if visited[i][j] == day: #방문 값과 날이 같으면
                continue #건너뜀
            visited[i][j] = day #방문에 날 기록
            if bfs(n, left, right, i, j, day):  # bfs 결과 true면 연합을 이루었다는 의미이므로 flag 표시
                flag = True #깃발 올림

        if not flag: #깃발이 없으면
            return day - 1 #날-1 값 리턴


# 입력
n, left, right = map(int, input().split()) # 입력
board = [list(map(int, input().split())) for _ in range(n)] #보드 생성

# 방문배열
visited = [[0] * n for _ in range(n)] #방문 배열 생성
# 나라
countries = deque([(i, j) for i in range(n) for j in range(n)]) #나라 생성

# 연산 + 출력
print(simulation(n, left, right)) #출력