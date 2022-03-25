import sys #변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline #입력받기

"""
[백대열]
- n과 m의 최대공약수를 찾아서 나눠준다.
"""

def calc_gcd(a, b): #최대공약수 함수
    # a > b일 때, a와 b의 최대공약수를 리턴
    if b == 0: #b가 0이면
        return a #그냥 a리턴
    return calc_gcd(b, a % b) #다시 자기자신 함수 호출

# 입력
n, m = map(int, input().split(':')) # ':' 기준으로 나누기

# 연산 + 출력
gcd = calc_gcd(max(n, m), min(n, m)) #입력 값중 최대를 a, 최소를 b
# / 로 계산하면 1.0 과 같이 소수점이 표기되므로 주의
print(n // gcd, ':', m // gcd, sep='') #결과 값 출력