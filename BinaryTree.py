class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def inorder(self):
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder())
        return result

    def preorder(self):
        result = []
        result.append(self.value)
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result

    def postorder(self):
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.value)
        return result

    def map_tree(self, func):
        new_left = self.left.map_tree(func) if self.left else None
        new_right = self.right.map_tree(func) if self.right else None
        return BinaryTree(func(self.value), new_left, new_right)

    @staticmethod
    def from_list(data, index=0):
        if index >= len(data) or data[index] is None:
            return None
        tree = BinaryTree(data[index])
        tree.left = BinaryTree.from_list(data, 2*index + 1)
        tree.right = BinaryTree.from_list(data, 2*index + 2)
        return tree

    def __str__(self):
        return f"BinaryTree: {self.value}, {self.left}, {self.right}"

    def __repr__(self):
        return f"BinaryTree({self.value}, {self.left}, {self.right})"


tree = BinaryTree(1,
                  BinaryTree(2, BinaryTree(4), BinaryTree(5)),
                  BinaryTree(3, BinaryTree(6))
                  )

print(f"Inorder: {tree.inorder()}")
print(f"Preorder: {tree.preorder()}")
print(f"Postorder: {tree.postorder()}")

doubled = tree.map_tree(lambda x: x * 2)
print(f"Удвоенные значения: {doubled.inorder()}")

# Создание из списка
lst = [1, 2, 3, 4, 5, 6, 7]
tree2 = BinaryTree.from_list(lst)
print(f"Создано из списка, inorder: {tree2.inorder()}")
