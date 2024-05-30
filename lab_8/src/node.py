class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.__parent = parent
        self.__value = value
        self.__left = left
        self.__right = right
    
    @property
    def value(self):
        return self.__value 
    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, value):
        self.__right = value
    
    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, value):
        self.__parent = value  

    def __repr__(self) -> str:
        return str(self.value)
