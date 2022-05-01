import sys
input = sys.stdin.readline

"""
 [좋다]
 1. 각 수마다 양 쪽 끝에서 포인터를 시작해서 좁혀오면서 어떤 '다른 두 수'가 현재 수를 만들 수 있는지 검사
 2. 포인터를 차례로 옮기며 검사하기 위해 미리 수를 오름차순 정렬함
 3. 현재 만드려는 수의 위치와 left, right 포인터 위치가 겹칠 경우 처리 주의
 4. left와 right의 초기화 주의 -> 음수가 존재하므로, 지금 검사하는 수 보다 큰 수도 포함될 수 있음
"""

def count_good_numbers(n, nums): # 좋은 수의 개수를 세는 함수(투 포인터)
    count = 0 #개수 변수 0으로 초기화

    for i in range(n): #반복문
        p1 = 0 #인덱스(앞)
        p2 = n - 1 #인덱스(뒤)

        while p1 < p2: #앞, 뒤 순서 지켜질때까지
            if p1 == i: #p1
                p1 += 1 #1 앞으로
                continue #계속
            if p2 == i: #p2
                p2 -= 1 #-1 앞으로
                continue #계속

            if nums[p1] + nums[p2] == nums[i]: #좋은 수
                count += 1 #카운트
                break #끝
            if nums[p1] + nums[p2] < nums[i]: #합이 같지 않으면(작)
                p1 += 1 #p1 1 앞으로
            else: #합이 같지 않으면(큼)
                p2 -= 1 #p2 -1 앞으로

    return count #개수 리턴

# 입력
n = int(input()) #입력
nums = list(map(int, input().split())) #num에 넣기
nums.sort() # 오름차순 정렬

# 연산 + 출력
print(count_good_numbers(n, nums))# 연산 + 출력