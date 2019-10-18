class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.frequency = 0

    def __str__(self):
        return f"value: {self.value}, left: {self.left}, right: {self.right}"

    def insert(self, value):

        if self.value == value:
            self.frequency += 1
            return

        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
                self.right.frequency += 1
            else:
                self.right.insert(value)

        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
                self.left.frequency += 1
            else:
                self.left.insert(value)

    def contains(self, target):

        if self.value == target:
            return True
        if target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)
