
import random as rd


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.answers = SingleLinkedList()
        self.score = 0
    
    def answer(self, question, real_answer):
        # imagine, that student reads question and answers it.
        answer = rd.choice( [True, False])
        self.answers.append(answer)
        if answer == real_answer:
            self.score += 1
        return answer

    def __repr__(self) -> str:
        return f"Node({self.value})"

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(value)

    def prepend(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next_node
        return None

    def index_of(self, func):
        current = self.head
        index = 0
        while current:
            if func(current):
                return index
            index += 1
            current = current.next_node
        return -1
        

    def from_list(self, values):
        for value in values:
            self.append(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    def __add__(self, other_list):
        new_list = SingleLinkedList()
        for value in self:
            new_list.append(value)
        for value in other_list:
            new_list.append(value)
        return new_list

    def __slice__(self, start, end):
        new_list = SingleLinkedList()
        current_index = 0
        current = self.head
        while current_index < start:
            current = current.next_node
            current_index += 1
        while current_index < end:
            new_list.append(current.value)
            current = current.next_node
            current_index += 1
        return new_list

    def __getitem__(self, index):
        current_index = 0
        current = self.head
        while current_index < index:
            if current is None:
                raise IndexError("Index out of range")
            current = current.next_node
            current_index += 1
        if current is None:
            raise IndexError("Index out of range")
        return current

    def __repr__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next_node
        return "[" + " -> ".join(elements) + "]"

    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next_node
        return length