import sys

sys.setrecursionlimit(10 ** 8) #순환 범위 제한
input = sys.stdin.readline

"""
[트리의 부모 찾기]
- 1번 노드에서 출발해서 탐색
- 루트 노드에서 출발 했기 때문에, 현재 노드의 부모는 이전 노드가 된다.
- (주의) 트리 노드의 최대 수가 100,000이므로, 가능한 트리의 최대 깊이는 100,000번이 된다. 즉, 재귀 깊이 또한 100,000번이 되므로 재귀 깊이 제한을 재설정 해야한다.
"""


def dfs_recursion(prev, curr): #순환하는 함수
    if parent[curr]: #끝이면
        return #리턴

    parent[curr] = prev #부모는 이전 노트

    for next in adj_list[curr]: #다음
        dfs_recursion(curr, next) #순환
    return #리턴


n = int(input()) #입력
adj_list = [list() for _ in range(n + 1)] #adj 리스트 생성
parent = [0] * (n + 1) #부모 생성

for _ in range(n - 1): #반복문
    a, b = map(int, input().split()) #a,b 인덱스 생성
    adj_list[a].append(b) #a인덱스에 b 넣기
    adj_list[b].append(a) #b인덱스에 a 넣기

dfs_recursion(1, 1)  # 1번 노드는 루트노드이므로, 부모를 자기 자신으로 설정
print(*parent[2:], sep='\n') #답 출력