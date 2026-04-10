# Linked Listでの実装

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 1


    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

    def peek(self):
        return self.top.value if self.top else None


            


my_stack = Stack(4)
my_stack.push(5)
my_stack.push(6)

"""
| 6 |
| 5 |
| 4 |
"""

my_stack.pop()
"""
| 5 |
| 4 |
"""

my_stack.print_stack()
        
    

