

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
import random

def updown():


    result:random.randrange(1 , 100 )


while True:
    user_input=input("답을 입력하세요:")
    x = int(user_input)

    if x > int(result):
        print("down")

    elif x < int(result):
        print("up")

    else:
        print("종료합니다.")
    break
