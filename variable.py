x =3
y =x+3

print (y+2)

x=[1,2,3,4,5] #list
print(x)
y=3
print(x[0])
print(x[y])

x = x*2
print("x* 2 :", x)

x=[1,2,3,4,5]
#slicing
print(x[2:5])
print("append========")
x.append(7)
print(x)
print("insert========")
x.insert(1,9)
print(x)
print("remove========")
x.remove(1) #인덱스가 아닌 함수를 지우는 함수
print(x)
print("9->6=======")
x[0] = 6
print(x)

#참조할 수 없는 인덱스 위치를 참조했을때

print("배열의 길이=======")
print(len(x))

print("배열의 마지막 인덱스=====")
print(len(x)-1)
x = { 'a':1, 'b':2} #key;value 탐색같은 느낌
print(x)
print(x['a'])
print(type(x))

x['c'] = 10

print(x)

print(x['c'])


del x['a']
print(x)

print(x.keys()) #특정 키값만 제거하기
print(x.values())
print(x.items())

print(x.clear()) #딕셔너리 전체 지우기
x ={ 'a':[1,2,3],'b':2}
print(x)

example = {
    'python': [True, False, True, True, True, True, True, False, False, True],
    'java': [True, False, False, True, True, True, False, False, False, True],
    'git': [False, False, True, True, False, True, True, True, True, True],
}

python_description = [
    {
        'answer': 1,
        'description': 'python에 대한 설명은 1번이 맞습니다.'
    },
    {
        'answer': "list",
        'description': 'python의 열거형 데이터 타입은 list입니다.'
    },
    {
        'answer': True,
        'description': 'python의 LIST 안에 Dictionary를 사용할 수 있습니다.'
    },
]

list_example = [1, "+", 2, "="]

print(exemple)
#변할 수 있는 데이터는 key 값으로 사용불가능
dict_exemple ={
    1: 'value 1'}
    ['a' :'value a']
print(dict_exemple[1])
