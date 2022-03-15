import sys
input = sys.stdin.readline #입력 받기


n = int(input())#파일 개수
extension = dict() # key(확장자) - value(파일 개수) 쌍이 필요하므로 dict() 사용

for _ in range(n): #파일 개수가 있는 동안
    ext = input().rstrip().split('.')[1] # 입력을 '.'을 기준으로 나누어 리스트에 담고 (.split('.')), 두번째 요소(확장자)를 ext에 저장
    if ext in extension: # key 에러가 나지 않도록 ext가 딕셔너리에 있는지 확인
        extension[ext] += 1 #있다면 1증가
    else: #그렇지 않다면
        extension[ext] = 1 #1

answer = sorted(extension.items()) #값들을 정렬

for key, value in answer: #출력
    print(key, value) #확장자, 파일 개수 출력