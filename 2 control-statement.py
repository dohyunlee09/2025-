def print_usingif():
    score = int(input("점수를 입력하세요."))

    if score > 100 or score < 0:
        print("정상적인 점수 범위가 아닙니다.")
    else :
        if score > 60:
            print("합격입니다.")
        elif score >=60:(
            print("재시험 응시가 필요합니다."))
        else:
            print("불합격입니다.")

        if score <= 100:
            if score >= 0:
                print("진짜 합격입니다.")
#13번 줄부터 15번은 그저 범위안에 드는 숫자에대한 정보를 더 주지 범위를 벗어나는 숫자에게는 할당되는 것이 없다
# while True:
#   user_input = input("답을 입력하세요 : ")
#   if user_input.lower() == "z":
#       break

def print_pibonacci_type2():
    input_number = int(input("숫자를 입력하세요 : "))
    index = 1

    while index <= input_number:
        print(index)
        index = index + 1


    index = 0
    while index <= input_number:
        print(index)
        index = index + 2

    print("피보나치 수열")
    list[int] = [1,1]

    while list[-1] <= input_number:
        print(list[-1])
        list.append(list[-1] + list[-2])

    print("피보나치수열 without list")
    a=1
    b=1
    c=1

    while c <= input_number:
        print(c)
        c= a+b
        a = b
        b = c