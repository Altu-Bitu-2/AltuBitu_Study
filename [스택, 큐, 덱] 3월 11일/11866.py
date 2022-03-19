import sys #변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque #list의 append(), pop()등의 메소드를 deque에서도 제공한다.
input = sys.stdin.readline #입력받기

n, k = map(int, input().split()) #입력받아 변수 n,k에 저장

que = deque(range(1, n+1)) # 1부터 n까지 deque에 넣어줍니다.
ans = []    # 정답 저장할 리스트

# que의 크기가 0이 될 때까지 반복
while len(que) != 0: #큐 크기가 0이 될때까지 반복
    # for _ in range(k-1):
    #     que.append(que.popleft())

    # .roate(n) : 양수면 n만큼 오른쪽으로 회전, 음수면 n만큼 왼쪽으로 회전하는 메소드
    que.rotate(-(k-1)) #-(k-1) 만큼 회전
    ans.append(que.popleft()) # k번째 수는 pop한 뒤 정답 리스트에 추가합니다.

# join메소드는 광장히 유용합니다. iterable 객체에 담긴 string들을 사이에 ', '로 이어 리턴하는 함수입니다.
# 그러기에 앞서, 정답 배열에는 정수형이 들어 있으므로, str()을 통해 문자열로 바꾸어야 합니다.
print('<'+', '.join(map(str, ans))+'>') #문자열로 봐꾼뒤, , 로 이어 프린트.