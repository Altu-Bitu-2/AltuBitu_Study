import sys
input = sys.stdin.readline

"""
 [다이어트]
 left: 성원이가 기억하고 있던 몸무게
 right: 성원이의 현재 몸무게
 같은 위치에서 시작해서 점점 증가하는 투 포인터로 풀이
 대신, left ~ right를 모두 고려하는 것이 아니라 left, right 포인터 값 자체만 고려
 !주의! 몸무게의 범위가 딱히 정해져 있지 않으므로, 종료 조건을 잘 세우는 것이 중요!
       -> 두 몸무게가 같아지는 순간 종료!
       -> left가 right와 같은 값을 가진다면, 직전 상황은 두 몸무게가 1차이 나는 상황
       -> 이 때 몸무게 차이가 g 이상이었다는 것은 이후로 나올 수 있는 차이는 무조건 g 이상이 된다. (제곱수의 간격은 수가 커질 수록 늘어나기 때문)
"""

def get_possible_weight(g): #몸무게 구하는 함수
    left = 1 #기억하고 있던 몸무게
    right = 2 #현재 몸무게
    ans = [] #답 넣을 변수
    while left < right: #기억 < 현재일때
        diff = right ** 2 - left ** 2 #차이
        if diff > g: #차이가 g보다 크면
            left += 1 #기억에서 1 증가
        else: #차이가 g보다 작거나 같으면
            if diff == g: #같을때
                ans.append(right) #값 추가
            right += 1 #작을때 현재 몸무게 1 증가
    return ans #답 리턴

# 입력
g = int(input()) #입력

# 연산
ans = get_possible_weight(g) #연산

# 출력
if ans: #답일때
    print(*ans, sep='\n') #출력
else: #아니면 끝
    print(-1)