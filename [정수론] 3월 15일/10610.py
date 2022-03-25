import sys #변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline #입력받기

"""
[30]
30의 배수 = 10의 배수 && 3의 배수
1. 10의 배수 -> 입력된 수에 0이 포함되어 있는지 확인
2. 3의 배수 -> 모든 자리수의 합이 3의 배수인지 확인
30의 배수임이 확인 되었으면,
가장 큰 수를 만들기 위해 9부터 0까지 역순으로 나열한다.
"""


def find_number(n): #함수 만들기
    digits = list(n) #리스트 생성
    digits.sort(reverse=True)  # 가장 큰 수를 만들기 위해 역순으로 정렬

    # 0이 존재하지 않으면, return -1
    if digits[-1] != '0': #0이 존재하지 않다면
        return -1 # -1리턴

    total = 0  # 3의 배수인지 확인하기 위해 모든 자리수를 더함

    for i in digits: # 리스트 값을 i에 하나씩 대입
        total += int(i) #정수로 바꿔 total에 합한다

    # 3의 배수임을 확인
    if total % 3 == 0: # 3의 배수이면 나머지 0
        return ''.join(digits) #'구분자'.join(리스트) 데이터 합쳐서 리턴
    else: #그렇지 않다면
        return -1 #-1을 리턴


n = input().rstrip() # 입력

print(find_number(n)) # 연산 + 출력