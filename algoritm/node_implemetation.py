import data_structure as ds
from random import *
# import importlib 
# importlib.reload(ds) # 수정한 모튤 다시 로드

a = ds.Node(2)
b = ds.Node(52)
c = ds.Node(18)

a.next = b
b.next = c
b = None
c = None

print(a.next.data)
print(a)
print(b)
print(c)

print(a.__doc__) # 데이터 타입의 여러 정보 출력
print(a.__dict__)

node_list = []
for a in range(1000):
    node_list.append(ds.Node(randint(1, 10000)))

# link 연결 작업
for idx in range(1, len(node_list)):
    node_list[idx -1] + node_list[idx]

print(node_list[0])
print(node_list[:5])
print(node_list[0].data)
print(node_list[0].next.data)

# PEP 257: 파이썬의 Docstring 정의 프로포절
# 클래스, 함수, 변수 등에 대한 정보를 서술함
# __doc__ 또는 docstring 바로 보기 기능등을 통해 확인
# 내가 만든 코드는 남이 본다!

# PEP 484 : 파이썬의 Type 사전 정의 프로포절
# Dynamic typing의 파이썬이지만 in/out 파라메터의 타입에 대한 정보를 사전에
# 정의해서 사용함(Python 3.5이상)
# 반드시 강제하지 않음 : 내 코드는 나만보지 않는다.

# Special Method for Python Class
# 파이썬의 Class 정의시 공통적으로 정의되는 method
# __str__, __init__, __len__, __add__ 등 사전 정의된 함수로 다양한
# operation과 매칭됨
# 자신의 class의 특징을 고려하자!