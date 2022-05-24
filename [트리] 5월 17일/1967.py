import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

"""
 [트리의 지름]
 1. 지름을 이루는 두 점은 모두 리프 노드
 2. 임의의 한 노드에서 가장 멀리 있는 노드(리프 노드)는 지름을 이루는 노드 중 하나
 3. 지름을 이루는 노드에서 가장 멀리 있는 노드는 지름을 이루는 다른 노드
 부모->자식의 방향만 저장하면 리프 노드에서 다른 리프 노드로 탐색할 수 없으므로 무방향 그래프로 저장
"""


def dfs(node, parent, graph): #dfs 함수
    pos = node #pos는 node
    dist = 0 #dist는 0으로 초기화
    for next, weight in graph[node]: #반복문
        if next == parent: #다음은 부모 노드
            continue #계속

        child_node, child_dist = dfs(next, node, graph) #자식 노드는 dfs 찾기

        if weight + child_dist > dist: #지름 보다 작을때
            dist = weight + child_dist #지름 은 무게 + 자식 지름
            pos = child_node #pos는 자식노드

    return pos, dist #리턴 


# 입력
n = int(input()) #입력

graph = [list() for _ in range(n + 1)] #그래프 리스트

for _ in range(n - 1): #반복문
    p, c, w = map(int, input().split()) #p, c, w에 입력
    # 무방향 그래프로 만들기
    graph[p].append((c, w)) #무방향 그래프로 만들기
    graph[c].append((p, w)) #그래프 만들기

# 연산
first_node, _ = dfs(1, -1, graph) #첫 노드 연산 
_, radius = dfs(first_node, -1, graph) #반지름 연산

print(radius) #출력