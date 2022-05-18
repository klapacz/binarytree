from binarytree import Node as OriginalNode


class Node(OriginalNode): 
    def __init__(self, *, value, left=None, right=None, parent=None):
        super().__init__(value, left, right) 
        self.parent = parent

    def add(self, value) -> bool:
        if self.left == None:
            self.left = Node(value=value, parent=self)
            return True

        if self.right == None:
            self.right = Node(value=value, parent=self)
            return True
        
        if self.left.add(value):
            return True

        if self.right.add(value):
            return True

        return False
    
    def find(self, value):
        if self.value == value:
            return self

        if self.left != None and self.left.find(value):
            return self.left.find(value)

        if self.right != None and self.right.find(value):
            return self.right.find(value)

        return False


if __name__ == '__main__':
    root = Node(value=0)

    for i in range(1, 11):
        root.add(i)

    print(root)
