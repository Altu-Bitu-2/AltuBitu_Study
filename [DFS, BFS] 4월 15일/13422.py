import sys

input = sys.stdin.readline

"""
 [도둑]
 1. 연속해서 훔쳐야 할 집이 m으로 고정됐기 때문에 슬라이딩 윈도우
 2. 직선이 아니라 원 형태의 배열! 모듈러 연산을 통해 윈도우의 양 끝 위치 조절하기
 !주의! 마을에 있는 집의 개수와 도둑이 훔칠 집의 개수가 같을 때(n==m) 도둑이 훔칠 수 있는 경우의 수 1개!
    => 예를 들어, n = m = 3, k = 4, house = [1, 1, 1] 일 때, 실제 방법의 수는 1번, 2번, 3번 집을 택하는 경우밖에 없지만
       예외 처리를 안해줄 경우, 원형으로 돌며 3을 출력하게 됨!
"""


def steal(n, m, k, house): #집을 훔치는 함수
    # 윈도우 초기화
    money = sum(house[:m]) #돈 초기화
    count = 0 #개수 초기화

    if money < k: #돈이 k보다 적으면
        count += 1 #더 훔침

    if n == m: #집 개수와 훔칠 개수가 같으면
        return count # 개수 리턴

    for i in range(m, n + m - 1): #반복
        money -= house[i - m] #원형으로 돌기
        money += house[i % n] #돌기

        if money < k: #돈이 k보다 작으면
            count += 1 #더 훔침

    return count #개수 리턴


# 입력
t = int(input()) #입력

for _ in range(t): #반복문
    # 입력
    n, m, k = map(int, input().split()) #입력
    house = list(map(int, input().split())) #집 리스트 만들기
    # 연산 + 출력
    print(steal(n, m, k, house)) #출력