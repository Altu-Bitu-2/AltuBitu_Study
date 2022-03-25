import sys #변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline #입력받기

"""
[공약수]
최대공약수: gcd, 최소공배수: lcm
gcd * lcm = A * B이고,
A = gcd * a, B = gcd * b로 나타낼 수 있다. (이때, a와 b는 서로소)
따라서 gcd * lcm = A * B = gcd * gcd * a * b,
lcm / gcd = a * b
A+B의 최소 -> a+b의 최소 -> a, b의 차가 최소가 되도록
"""


def calc_gcd(a, b): #최대공약수 함수
    # a > b일 때, a와 b의 최대공약수를 리턴
    if b == 0: #b가 0이면
        return a #그냥 a리턴
    return calc_gcd(b, a % b) #다시 자기자신 함수 호출


gcd, lcm = map(int, input().split()) #최대공약수와 최소공배수

ab = lcm // gcd #a와 b 곱은 최소공배수
root_ab = ab ** (1 / 2) #루트 a,b 구하기

for i in range(int(root_ab), 0, -1): # root(ab)부터 1까지
    if ab % i > 0: #나머지가 양수면
        continue #계속함

    a = i #끝나면 i는 a
    b = ab // i #b는 ab//i

    if calc_gcd(b, a) == 1: # a와 b가 서로소인지 확인 - a는 항상 b보다 작다
        break #끝

print(a * gcd, b * gcd) #결과값 출력