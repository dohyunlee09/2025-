

#def print_times_table(number):
   # print(number, "*", 1, "=", number * 1)

    #print(number, "*", 2, "=", number * 2)

    #print(number, "*", 3, "=", number * 3)

    #print(number, "*", 4, "=", number * 4)

    #print(number, "*", 5, "=", number * 5)

    #print(number, "*", 6, "=", number * 6)

    #print(number, "*", 7, "=", number * 7)

    #print(number, "*", 8, "=", number * 8)

    #print(number, "*", 9, "=", number * 9)


#while True:

    #user_input = input("값을 입력하세요 : ")

    #if user_input.lower() == "z":
        #break

    #print_times_table(int(user_input))
#test
import time
import random


def updown():
    # random.randrange ( n, m )   n <= result < m
    print("WELCOME TO UP DOWN")
    result = random.randrange(1, 100)
    while True:
            user_input = input("답을 입력하세요:")
            x = int(user_input)

            if x > result:
                print("down")

            if x < result:
                print("up")

            elif x == result:
                print("종료합니다.")
                break


def quiz():
    print("WELCOME TO QUIZ!")

def stop_watch():
    print("WELCOME TO UP STOPWATCH")
    # random 초를 제공하면 ex) 7초
    start = time.time()
    print(start)
    end = time.time()
    if user_input("5"):
        print(end)

    if  6.7<= str(end - start) <=7.3:
        print("성공입니다!!!")







while True:
    print('''
    ================메뉴================
    A. Up & Down 게임
    B. 영어 낱말 맞추기
    C. Stop watch 게임
    Z. 프로그램 종료
    ====================================
    ''')
    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "a":
        updown()

    elif user_input.lower() == "b":
        quiz()
    elif user_input.lower() == "c":
        stop_watch()
    elif user_input.lower() == "z":
        break

