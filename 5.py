### 함수 만들기 ###
# def 인사(사람명):
#     print("안녕!!", 사람명)

# print()
# 인사("혜리")
# 인사("펭수")

### 합계 구하는 함수 만들기 ###

# def 합계(x, y):
#     합 = 0
#     for i in range(x, y+1):
#         합 = 합 + i
#     return 합

# 합 = 합계(1, 100)
# print(합)
# def 빼기(수):
#     return 수-5
# print(빼기(10))

### 최대값 구하는 함수 만들기 ###

# def 최대값(x, y):
#     if x > y :
#         return x
#     else:
#         return y
# print(최대값(10, 2))
# print(최대값(5, 8))

# def 소수판별(수):
#     for i in range(2, 수):
#         if 수 % i == 0:
#             return False
#     return True
# 수 = int(input("수를 입력하세요."))
# if 소수판별(수) == True:
#     print("소수가 맞습니다.")
# else:
#     print("소수가 아닙니다.")

# from random import randrange

# def 암호생성기():
#     재료 = "abcdefghijklmnopqrstuvwxyz0123456789"
#     암호 = ""
#     for i in range(6):
#         인덱스 = randrange(len(재료))
#         암호 = 암호 + 재료[인덱스]
#     return 암호
# print(암호생성기())

# def 인사(이름, 메세지 = "심심해서 보냈어요"):
#     print(이름, 메세지)
# 인사("배트맨")  
# 인사("배트맨","살려줘요")

import turtle as t

def 오른쪽():
    t.setheading(0)
    t.forward(10)
def 위쪽():
    t.setheading(90)
    t.forward(10)    
def 왼쪽():
    t.setheading(180)
    t.forward(10)
def 아래쪽():
    t.setheading(270)
    t.forward(10)   
def 초기화():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)

t.shape("turtle")
t.onkeypress(오른쪽, "Right")
t.onkeypress(위쪽, "Up")
t.onkeypress(왼쪽, "Left")
t.onkeypress(아래쪽, "Down")
t.onkeypress(초기화, "Escape")

t.listen()

t.mainloop()

