# print("환영합니다.")
# print("환영합니다.")
# print("환영합니다.")
# print("환영합니다.")
# print("환영합니다.")

# for x in range(1000) :
#     print(x,"번 환영합니다.")

# for 이름 in ["배트맨", "슈퍼맨", "스파이더맨", "앤트맨"] :
#     print("안녕! ", 이름)

# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x, end="＠ ")

### 1부터 10까지의 합을 구하기 ###

# 합 = 0
# for i in range(6, 101, 3) :
#     합 = 합 + i
# print(합)

### 문자열 반복 ###

# 인사 = "반갑습니다."

# for c in 인사 :
#     print(c , end="*")

### 정수합 만들기 ###

# 합 = 0

# 수 = int(input("어디까지 계산할까요?"))

# for i in range(1, 수 + 1):
#     # 합 = 합 + i
#     합 += i
# print(f"1부터 {수}까지의 합은 {합}입니다.")

### 별 그리기 ###
# import turtle

# 별 = turtle.Turtle()

# for i in range(5) :
#     별.forward(100)
#     별.right(144)
# a = input()
# import os
# os.system("pause")
# import time
# time.sleep(5)  # 5초 기다리기

### 다각형 그리기 ###

# import turtle

# 다각형 = turtle.Turtle()

# 변_수 = int(input("변의 갯수는?"))
# 변_길이 = int(input("변의 길이는?"))

# 각도 = 360.0 / 변_수

# for i in range(변_수) :
#     다각형.forward(변_길이)
#     다각형.right(각도)
# a = input()

### 이중 for 문 ###

# import turtle

# t = turtle.Turtle()

# for x in range(3) :  # 3개의 4각형 그리는 코드
#     t.left(20)
#     for y in range(4) :  # 사각형 그리는 코드
#         t.forward(50)
#         t.left(90)

# import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.color("red")

# for x in range(360) :  # 360개의 4각형 그리는 코드
#     t.left(1)
#     for y in range(3) :  # 사각형 그리는 코드
#         t.forward(200)
#         t.left(120)

# import turtle as t

# t.bgcolor("pink")
# t.color("yellow")
# t.speed(0)

# 갯수 = int(input("갯수를 입력해주세요."))

# for i in range(갯수):
#     t.circle(100)
#     t.left(360.0/갯수)

# import turtle as t

# 각도 = 80
# t.pensize(3)
# t.speed(0)

# for i in range(500):
#     if i % 2 == 0 :
#         t.color("red")
#     else :
#         t.color("blue")
#     t.forward(i)
#     t.left(각도)

# i = 0

# while i < 10 :
#     print(i, end="★")
#     #i = i + 1
#     i += 1 

### while로 1부터 10까지의 합 구하기 ###

# i = 1
# 합 = 0
# while i < 1001 :
#     합 = 합 + i # 합 += i
#     i = i + 1
# print(합)
# 합 = 0
# i = 1
# while i < 101 :
#     if i % 5 == 0 :
#         합 = 합 + i
#     i = i + 1
# print(합)


# 과목수 = 0
# 합계 = 0
# 점수 = 0
# 평균 = 0

# print("종료를 할려면 음수를 입력하시오")

# while 점수 >= 0 :
#     점수 = int(input("과목 점수를 입력하세요."))
#     if 점수 >= 0 :
#         합계 = 합계 + 점수
#         과목수 = 과목수 + 1

# # 음수를 입력한 다음
# if 과목수 > 0:
#     평균 = 합계 / 과목수

# print(과목수, "과목의 평균은", 평균,"입니다.")

# from random import randint

# 시도수 = 0
# 정답 = randint(1, 100)

# while 수 < 0 :
#     수 = int(input("추측한 수를 입력하세요."))
#     시도수 = 시도수 + 1
#     if 정답 < 수 :
#         print("입력한 값이 큽니다.")
#     elif 정답 > 수 :
#         print("입력한 값이 작습니다.")
#     else :
#         print("정답입니다.")
#         break

# if 정답 == 수 :
#     print("축하합니다. 잘 맞추셨습니다.")
# else :
#     print("틀리셨습니다. 정답은", 정답)
# print("시도 횟수는 ", 시도수, "번")

# import turtle as t

# try:
#     계산 = "계산" + 3

# except :
#     print("오류가 뜨면 이게 실행됨")
    
# t.bgcolor("black")
# t.color("red")
# t.pensize(4)
# t.shape("turtle")

# s = t.Screen()
# s.setup(400, 400)

# 시도 = 0
# while 시도 < 10 :
#     시도 = 시도 + 1
#     t.penup()
#     t.setpos(0, -1 * 시도 *10)
#     t.pendown()
#     t.circle(시도 * 10)

# a = input()

### 중첩 for문으로 별 그리기 ###

# for y in range(10) :
#     for x in range(5) :
#         if x % 2 == 1:
#             print("*", end=" ")
#     print("")

# import turtle as t

# t.speed(0)
# t.color("pink")

# for i in range(360) :
#     for x in range(5):
#         t.left(144)
#         t.forward(200)
#     t.left(1)

# 그룹 = "여자친구"

# for i in 그룹:
#     print(i)


# 문자 = input("원하는 글자를 입력하세요.")

# 모음 = "볼드모트"
# 완성 = ""

# for i in 문자 :
#     if i not in 모음 :
#         완성 =  완성 + i

# print(완성)

# 문자 = input("원하는 글자를 입력하세요.")
# 모음 = 0
# 자음 = 0
# # 문자 = 문자.lower()
# print(문자)

# for i in 문자 :
#     if i in "aeiouAEIOU" :
#         모음 = 모음 + 1
#     else:
#         자음 = 자음 + 1
# print("모음의 갯수", 모음, "자음의 갯수", 자음)

문자 = input("원하는 계좌번호를 입력하세요.")

완성 = ""
for i in 문자 :
    if i not in "-":
        완성 = 완성 + i
print(완성)