
class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class binarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root==None:
            self.root=Node(data)
            return True

        self._insert(data, self.root)

    def _insert(self, data, curr):

        if curr.data > data:
            if curr.left == None:
                curr.left = Node(data)
            else:
                self._insert(data, curr.left)

        elif curr.data < data:
            if curr.right == None:
                curr.right = Node(data)
            else:
                self._insert(data, curr.right)

        else:
            print("Already in tree")

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(str(node.data))
            self.inOrder(node.right)
        return True

    def preOrder(self, node):
        if node:
            print(str(node.data))
            self.inOrder(node.left)
            self.inOrder(node.right)
        return True

    def postOrder(self, node):
        if node:
            self.inOrder(node.left)
            self.inOrder(node.right)
            print(str(node.data))
        return True




if __name__ == "__main__":

    myTree = binarySearchTree()
    myTree.insert(12)
    myTree.insert(10)
    myTree.insert(16)
    myTree.insert(2)
    myTree.insert(8)
    myTree.insert(13)
    myTree.insert(18)

    myTree.postOrder(myTree.root)



