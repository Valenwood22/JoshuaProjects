#Binary Search Tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.rightNode = right
        self.leftNode = left


class BinaryTree(object):
    def __init__(self):
        self.root=None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return True

        self._insert(data,self.root)

    def _insert(self,data,curr):
        if data<curr.value:
            if curr.leftNode==None:
                curr.leftNode=Node(data)
            else:
                self._insert(data,curr.leftNode)

        elif data>curr.value:
            if curr.rightNode==None:
                curr.rightNode=Node(data)
            else:
                self._insert(data,curr.rightNode)
        else:
            print("Already in tree")


    def inOrder(self, start, arr):
        if start:
            self.inOrder(start.leftNode, arr)
            arr.append(start.value)
            self.inOrder(start.rightNode, arr)
        return arr


    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i)

    def printGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print ("%d" %(root.value),)
        elif level > 1:
            self.printGivenLevel(root.leftNode, level - 1)
            self.printGivenLevel(root.rightNode, level - 1)

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.leftNode)
            rheight = self.height(node.rightNode)

            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1


if __name__ == "__main__":

    Tree = BinaryTree()
    Tree.insert(20)
    Tree.insert(8)
    Tree.insert(22)
    Tree.insert(4)
    Tree.insert(12)
    Tree.insert(10)
    Tree.insert(14)

    Tree2 = BinaryTree()
    Tree2.insert(20)
    Tree2.insert(8)
    Tree2.insert(4)
    Tree2.insert(12)
    Tree2.insert(10)
    Tree2.insert(14)

    print(Tree.inOrder(Tree.root, []))
    print(Tree.height(Tree.root))
    Tree.printLevelOrder(Tree.root)


