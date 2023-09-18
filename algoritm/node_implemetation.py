import data_structure as ds
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
print(a.__doc__) # 데이터 타입의 여러 정보 출력

# PEP 257: 파이썬의 Docstring 정의 프로포절
# 클래스, 함수, 변수 등에 대한 정보를 서술함
# __doc__ 또는 docstring 바로 보기 기능등을 통해 확인
# 내가 만든 코드는 남이 본다!

# PEP 484 : 파이썬의 Type 사전 정의 프로포절
# Dynamic typing의 파이썬이지만 in/out 파라메터의 타입에 대한 정보를 사전에
# 정의해서 사용함(Python 3.5이상)
# 반드시 강제하지 않음 : 내 코드는 나만보지 않는다.