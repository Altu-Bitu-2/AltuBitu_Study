import sys
# 로컬에서 코드를 확인하기 위해, 파일로 입력을 전달합니다.
# sys.stdin = open('input.txt 파일경로', 'r') # 이 부분은 백준에 올릴 때는 주석처리합니다.
input = sys.stdin.readline #입력 받기


s, e, q = input().split() #입력받은 값을 나누어 저장.
attendance = set() #순서가 없고 집합 안에서는 유니크한 값을 가지는 set 함수
answer = 0  # 출석 확인된 회원 수

# 이 문제는 파일의 끝 (EOF, End Of File)까지 입력을 받아야 하는 문제 입니다.
# try, except 문을 통해 입력이 들어오지 않는 경우에 대한 예외 처리를 해줍니다.
while (True): # while 무한루프
    try: # try문
        time, name = input().rstrip().split() #time과 name에 시간과 학회원명 저장
        # 입장 확인
        if time <= s: #개총 시작 전에 입장
            attendance.add(name) #입장했다면 추가
        # 퇴장 확인
        elif e <= time <= q: #개강 총회 스트리밍 사이
            if name in attendance: #만약 이름이 존대한다면
                answer += 1 #회원수 카운트
                attendance.remove(name) # 중복 체크를 방지하기 위해 이름을 제거한다.

    except: # 예외문
        # 입력이 끝났으므로, 출석 인원 출력
        print(answer) #출석 인원 출력
        break #끝