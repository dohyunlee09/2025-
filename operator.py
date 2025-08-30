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
z = x  /y #나눗셈
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


