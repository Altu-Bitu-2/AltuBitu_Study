import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

"""
 PPT 트리의 정점의 수 구하기 응용
 [트리와 쿼리]
 1. 루트에서부터 dfs 탐색
 2. 각 노드를 루트로 하는 서브트리의 정점 수를 재귀적으로 계산
    - 서브트리에 속한 정점의 개수를 저장하는 dp 배열의 초기화를 -1로 해주고, dfs 탐색 시 현재 정점의 dp 값을 0으로 설정함으로써 자식 노드만 탐색할 수 있도록 함 (부모 노드에 0이 저장되어 있으므로 바로 리턴)
"""

def tree_dp(curr, graph): #트리 함수
    if subtree_cnt[curr] != -1: #만일 끝까지 갔다면
        return subtree_cnt[curr] #리턴

    # 서브트리에 속한 정점의 수를 세고, 저장
    subtree_cnt[curr] = 0   # 현재 노드를 0으로 표기하여 부모 자식간 계속 호출되지 않도록
    cnt = 1 #cnt는 1로 초기화
    for next in graph[curr]: #다음 그래프
        cnt += tree_dp(next, graph) #cnt 갱신

    subtree_cnt[curr] = cnt #cnt 새로운 값 넣기
    return cnt #리턴


# 입력
n, r, q = map(int, input().split()) #n,r,q 입력
graph = [list() for _ in range(n+1)] #그래프 리스트
subtree_cnt = [-1]*(n+1) #서브트리

for _ in range(n-1): #반복문
    u, v = map(int, input().split()) #u, v 값 넣기
    graph[u].append(v) #그래프 연결
    graph[v].append(u) #그래프 연결

# 연산
tree_dp(r, graph) #연산


# 출력
for _ in range(q): #출력
    print(subtree_cnt[int(input())]) #답 출력