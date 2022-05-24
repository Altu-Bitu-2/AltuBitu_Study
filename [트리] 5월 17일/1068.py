import sys

input = sys.stdin.readline

"""
 [트리]
 기존 리프 노드 개수를 세는 dfs 탐색에서 지우는 정점을 만나면 더 이상 탐색하지 않고 0을 리턴
 !주의! 지우는 정점이 해당 부모 노드의 유일한 자식 노드였을 경우, 해당 정점을 지우면 부모 노드가 리프 노드가 돼서 개수가 1 증가함을 주의
 !주의! 루트 노드가 항상 0이 아님을 주의
"""


# 주어진 정점을 지웠을 때의 리프 노드의 수
def erase_leaf_cnt(node, erase_node): # 주어진 정점을 지웠을 때의 리프 노드의 수
    if node == erase_node: #노드는 지워진 노드
        return 0 #리턴 0
    if not tree[node] or (len(tree[node]) == 1 and tree[node][0] == erase_node): #만약드리가 아니거나 길이가 1 그리고 트리가 지워진 노드
        return 1 #리턴 1

    cnt = 0 #cnt 는 0

    for i in range(len(tree[node])): #반복문
        cnt += erase_leaf_cnt(tree[node][i], erase_node) #cnt 갱신

    return cnt #리턴


# 입력
n = int(input()) #입력
tree = [list() for _ in range(n)] #트리 리스트

for idx, x in enumerate(input().split()): #반복문
    if x == "-1": # x가 -1일때
        root = idx #루트는 인덱스
    else: #또는
        tree[int(x)].append(idx) #트리 추가

erase_node = int(input()) #erase_node 입력

# 연산 & 출력
print(erase_leaf_cnt(root, erase_node)) #출력