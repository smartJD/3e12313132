# print("안녕")
# print(abs(5))
# print(round(1.23424))
# print(round(1.60102))
# print(max(10,20,30,40,50))
# print(min(10,20,30,40,50))

# 이름 = input("당신의 이름은?")
# print("당신의 이름은 " + 이름)
# 나이 = input("당신의 나이는?")
# print("당신의 나이는 " + 나이)
# print("그럼 10년뒤에 당신 나이는", int(나이)+10)

# print(type(이름))
# print(type(int(나이)))

### 달력 만들기 ###

# import calendar

# 년 = int(input("보고 싶은 년도는?"))
# 월 = int(input("보고 싶은 월은?"))
# 달력 = calendar.month(년, 월)
# print(달력)

# ### 자판기 거스름돈 시뮬레이션 ###

# 물건값 = int(input("물건값은 얼마입니까?"))
# 천원 = int(input("1000원 지폐의 개수는?"))
# 오백원 = int(input("오백원 동전의 개수는?"))
# 백원 = int(input("백원 동전의 개수는?")) 

# 거스름돈 = 천원 * 1000 + 오백원 * 500 + 백원 * 100 - 물건값

# # 거스를 오백원 동전 갯수 확인
# 오백동전 = 거스름돈 // 500
# 거스름돈 = 거스름돈 % 500

# # 거스를 백원 동전 갯수 확인
# 백원동전 = 거스름돈 // 100
# 거스름돈 = 거스름돈 % 100

# print("반환된 오백원 동전 갯수:", 오백동전)
# print("반환된 백원 동전 갯수:", 백원동전)

### 문자열 \ 역슬래시 사용법 ###
# print("안녕\n나는 \t홍길동\"이야")
# print("반가워")

### 문자열 출력법 ###

# 수 = "10000"

# print("당신이 가진 전재산은 %s원 이군요."% 수)

### 문자열 포맷팅 ###

# 수 = 10000
# 이름 = "덕"

# print("%s씨, 당신은 %d원을 값으셔야 합니다."%(이름, 수))
# print("{}씨, 당신은 {}원을 값으셔야 합니다.".format(이름, 수))
# print(f"{이름}씨, 당신은 {수}원을 값으셔야 합니다.")

### 문자열 인덱싱 ###

# 걸그룹 = "만나서 반갑습니다."

# print(걸그룹[:5])





