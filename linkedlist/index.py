class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " -> ".join(values)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return self

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
    
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    
    def set_value(self, index, value):
        temp = self.get(index)
    
        if temp:
            temp.value = value
            return True
    
        return False
    
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
    
        if index == 0:
            self.prepend(value)
        return True
    
        if index == self.length:
            self.append(value)
            return True
    
            new_node = Node(value)
            pre = self.get(index - 1)
            new_node.next = pre.next
            pre.next = new_node
        
        self.length += 1
        return True
    
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
    
        if index == 0:
            return self.pop_first()
    
        if index == self.length - 1:
            return self.pop()
    
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
    
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

ll = LinkedList(10)
ll.print_list()
ll.append(20)
ll.print_list()
ll.pop()
ll.prepend(30)
ll.print_list()
ll.pop_first()
ll.prepend(40)
ll.prepend(50)
ll.prepend(60)
print("----")
ll.print_list()
print(ll.get(2).value)
ll.set_value(2, 100)
print("----")
ll.print_list()
ll.insert(2, 500)
print("----")
ll.print_list()
ll.remove(2)
print("----")
ll.print_list()
ll.reverse()
print("----")
ll.print_list()
