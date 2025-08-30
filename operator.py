x = 10
y = 15
#대입연산자
z= x == y
print("x == y : ", z)
z = x != y  #!는 같지않다
print("x != y : ", z)
z= x > y
print("x > y :" ,z)
z= x >= y
print("x >= y :" ,z)
z= x < y
print("x < y :" ,z)
z= x <= y
print("x <= y :" ,z)

#사칙연산
z = x +y
print("x + y :" ,z)
z = x -y
print("x - y :" ,z)
z = x * y # 곱셈
print("x * y :" ,z)
z = x /y #나눗셈
print("x / y :" ,z)
z = x // y  #나머지
print("x // y :" ,z)
z = x ** y #제곱
print("x ** y :" ,z)

z = x % y #제곱
print("x % y :" ,z)

z =5 + x * 3 #곱셈의 우선순위가 더 높음
print("(5+x * 3 :", z)

str_x = "hello"
str_y = ("python")

str_z =str_x + str_y
print("str_x + str_y:" , str_z)

# unsupported operand type(s) for -: 'str' and 'str'

str_z = str_x * 2
print(str_x * 2:" ,str_z)


delayed_effect_skill_a = "" #snake_case

array_x = [12314,12345]
array_Y = [124344,125355]

array_z = array_x + array_y
print("array_x + array_y :" , array_z)

array_z = array_x * array_y[0] #해당 인덱스에 있는 요소가 정수형일때만 가능
print("array_x * array_y[0] :" , array_z)

report_card = {
    "국어":3 ,
    "수학":2 ,
    "영어":6 ,
    "물리":1 ,
    "화학":2 ,
    "생명과학" 1,
}

can_apply = report_card["국어"] < 3 and report_card["수학"] < 3 and report_card["영어"] < 3
print("지원가능여부 :", can_apply)

#3합 6
total_score = report_card["국어"] +report_card["수학"]+report_card["영어"] <= 6
print("3합 6 :", total_score )

#과학 영재반
can_apply_class_for_the_gifted =report_card["물리"] ==1 or report_card["화학"] == 1 or report_card["수학"]
print("영재반 지원가능여부 :" , can_apply_class_for_the_gifted)

