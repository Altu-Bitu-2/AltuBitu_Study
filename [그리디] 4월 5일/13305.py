import sys
input = sys.stdin.readline

"""
[주유소]
최대한 가격이 싼 곳에서 많은 기름을 넣어야 한다.
따라서 첫번째 도시부터 현재까지 가장 싼 가격을 저장하고, 이동에 필요한만큼만 기름을 채운다.
이렇게 하면 지금까지 지나 온 도시 중 가장 싼 곳에서 최대한 많이 살 수 있다.
"""

def calc_min_cost(n, road, price): #가격 싼 방법 출력
    cost = 0 #비용 0으로 초기화
    min_price = price[0] #가격도 초기화
    dist = 0

    for city in range(n - 1): #도시 반복문
        cost += min_price * road[city] #가장 싼 가격 계산
        if price[city + 1] < min_price: #만약 최소 가격 넘으면
            min_price = price[city + 1] #최소 가격은 지금까지 계산한 가격

    return cost #비용 리턴

# 입력
n = int(input()) #개수 입력
road = list(map(int, input().split())) #길 입력
price = list(map(int, input().split()))# 가격 입력
# 연산 + 출력
print(calc_min_cost(n, road, price)) #정답 출력