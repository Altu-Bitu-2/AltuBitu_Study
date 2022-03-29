import sys

input = sys.stdin.readline

"""
[그룹 단어 체커] - 단순 구현 문제
- 이미 등장한 알파벳 저장할 set() 선언 (탐색 O(1))
- 처음 등장하는 알파벳은 set에 추가하고, 무리에서 떨어졌는데 이미 등장한 알파벳이면 그룹 단어가 아니다.
"""


def is_group_word(word):#그룹 단어인지 보는 함수
    checked = set() #체크하는 변수는 set
    prev = None #prec 변수는 None 

    for c in word: #word인 동안
        if c == prev: #c와 prev가 같다면
            continue # 계속

        if c in checked: #c가 checked라면
            return False #False 리턴

        checked.add(c) #c 추가
        prev = c #prev는 c

    return True #True 리턴


# 입력
n = int(input())# 입력

# 입력 + 연산
count = 0# count 0으로 초기화

for _ in range(n): #n인 동안
    word = input().rstrip() #word에 추가
    if is_group_word(word): #함수 호출
        count += 1 #횟수 증가

# 출력
print(count)# 출력