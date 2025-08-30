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

