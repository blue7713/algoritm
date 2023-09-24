from typing import Any

class Node:
    """
    A class to represent a Node for an explanation of data structure.
    '''
    Attribute
    -----------
    data : Any
        data that user store on Node instance
    next : Node
        object conneted to the next node in a linked list.

    """
    def __init__(self, data : Any = None, next : 'Node' = None) -> None:
        """
        Args :
            data (Any, optional) : data that user store on Node instance
            next (Node, optional) : object conneted to the next node to a linked list.

        Returns:
            None

        """
        self._data = data # self._ 는 외부에서 접근을 막는 것(information hiding)
        self._next = None

    @property
    def data(self):
        ''' data that user store on Node instance'''
        return self._data
    
    @property
    def next(self):
        '''object conneted to the next node int a linked list'''
        return self._next
    
    @data.setter # information hiding을 하면 해주어야하는 정의
    def data(self, value : Any) -> None:
        self._data = value

    @next.setter
    def next(self, node : 'Node') -> None:
        self._next = node

    def __str__(self) -> str: # print문으로 출력 시 보여지는 부분
        return_str = f"I love a data : {self._data}\n" \
                    + f"I love a next node : {id(self._next)}"
        return return_str
        
    def __repr__(self) -> str: # 주피터 등으로 print구문 없이 보여지는 부분
        return_str = f"Node({self._data})\n"
        return return_str
            
    def __add__(self, other) -> None:
        self._next = other