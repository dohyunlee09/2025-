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

#함수 호출 방법
#repeat_function()
def print_arr_type():
    arr =  ['blue valentine','all day project','take me to the moon','piano man']

    for i in arr:
        print(i)
#arr타입 함수호출로 주석 대체

#수학
test = [
    {
        'name': 'aaa',
        'number': 10101,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'bbb',
        'number': 10102,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ccc',
        'number': 10103,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },  {
        'name': 'ddd',
        'number': 10104,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'eee',
        'number': 10105,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    }
]



student_answer =         [1 , 3, 2 ,4, 5 , 3, 1, 2, 3,4]
correct_answer = correct_answer = {
    'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
}
def print_fortype(student_answer,correct_answer):
    first_score = 0
    for (student,correct) in zip(student_answer,correct_answer):
        #print(student , '/' , correct)
        if student == correct:
            first_score = first_score+10 #여기에 있어요

    #print(first_score)
    return first_score
def print_fortype2():
    first_score = 100
    for (student,correct) in zip(student_answer,correct_answer):
        #print(student , '/' , correct)
        if student != correct:
            first_score = first_score - 10

    #print(first_score)
    #100에서 10씩 뺴는방법


for student in test:
    #if student['name'] =='ccc':
     #continue


    print("학생", student['name'], "==================")

# 답안의 key 기준으로 반복하는 방법
#for key in student.keys():
#score = get_score(student[key], correct_answer[key])
#print(key, ": ", score)


# student key 기준으로 반복하는 방법
# for key in student.keys():
#     if key == 'name' or key == 'number':
#         continue
#     score = get_score(student[key], correct_answer[key])
#     print(key, ": ",score)



#math_score = print_fortype(student['math'], correct_answer['math'])
#korean_score = print_fortype(student['korean'], correct_answer['korean'])
#english_score = print_fortype(student['english'], correct_answer['english'])
#science_score = print_fortype(student['science'], correct_answer['science'])

#print("수학점수:", math_score)
#print("국어점수:", korean_score)
#print("영어점수:", english_score)
#print("과학점수:", science_score)








