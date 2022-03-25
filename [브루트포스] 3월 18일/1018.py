import sys#변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline#입력받기

"""
[체스판 다시 칠하기]
- 나올 수 있는 체스판의 경우: 2가지
    - (0, 0)이 검정인 경우, 흰색인 경우
    - 검정으로 시작하는 체스판의 경우, 인덱스 i+j가 짝수일 때 'B'임을 이용
1.  (0, 0) 인덱스부터 차례로 8*8 체스판 만들 때 바꿔야 하는 칸 수를 계산하고, 그 중 최솟값 구하기
보드 크기 <= 2,500
한 위치에 대한 체스판 비교 연산 = 64번
총 연산 수 = 2,500 * 64 < 1억 -> 브루트 포스 가능
"""
SIZE = 64 #크기는 64


# 검정으로 시작하는 체스판을 기준으로 계산(b_count) -> 절반(32) 이상이면 흰색으로 시작하는 체스판 카운트(64 - b_count) 리턴
def count_change(x, y, board): # (x, y)에서 시작하는 8*8 체스판을 만드는데 필요한 최소 카운트 리턴
    b_count = 0 #0으로 초기화

    for i in range(8): #8번 반복
        for j in range(8): #8번 반복
            if (i + j) % 2 == 0 and board[x + i][y + j] != 'B': # 검정으로 시작하는 경우, i+j가 짝수일 때 검정,
                b_count += 1 #b_count 1씩 증가
            elif (i + j) % 2 == 1 and board[x + i][y + j] != 'W': #아니면 흰색
                b_count += 1 #b_count 1씩 증가

    if b_count > SIZE // 2: # 최솟값 리턴
        return SIZE - b_count  # 흰색 시작 체스판 카운트
    return b_count  # 검정색 시작 체스판 카운트


n, m = map(int, input().split()) #n, m에 대입
board = [input().rstrip() for _ in range(n)] #board에 값 넣기
answer = SIZE  # 최대값으로 초기화

for i in range(n - 8 + 1): #가로 반복
    for j in range(m - 8 + 1): #세로 반복
        answer = min(answer, count_change(i, j, board)) # 답 도출
