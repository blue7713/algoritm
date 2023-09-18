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
    def __init__(self, data : Any - None, next : 'Node' - None) -> None:
        """
        Args :
            data (Any, optional) : data that user store on Node instance
            next (Node, optional) : object conneted to the next node to a linked list.

        Returns:
            None

        """
        self.data = data
        self.next = None