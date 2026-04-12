class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def  __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    # Recursive Binary Search Tree
    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node


    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)

    def __r_delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete_node(current_node.right, sub_tree_min)

        return current_node
            
    def r_delete(self, value):
        self.root = self.__r_delete_node(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def max_value(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value


bst = BinarySearchTree()
bst.insert(10)
bst.insert(8)
bst.insert(12)

print(bst.r_contains(12))
print(bst.r_contains(7))
