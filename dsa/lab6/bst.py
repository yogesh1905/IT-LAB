#BST Dict

class TreeNode:
    def __init__(self, key = None, value = None, parent = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.insertHelper(key, value, self.root)

    def insertHelper(self, key, value, root):
        if  key < root.key:
            if root.left is None:
                root.left = TreeNode(key, value, root)
            else:
                self.insertHelper(key, value, root.left)
        elif  key > root.key :
            if root.right is None:
                root.right = TreeNode(key, value, root)
            else:
                self.insertHelper(key, value, root.right)
        else:
            return

    def search(self, key):
        return self.searchHelper(key, self.root)
    def searchHelper(self, key, root):
        if root is None:
            print("none")
            return None
        else:
            if key < root.key:
                print("left")
                return self.searchHelper(key, root.left)
            elif key > root.key:
                print("right")
                return self.searchHelper(key, root.right)
            else:
                print("ret")
                return root
    def minimum(self, node):
        root = node
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root
    def maximum(self, node):
        root = node
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root

    def successor(self, key):
        t = self.search(key)
        print("t=", t.key, " t,r ", t.right.key)
        if t is None:
            return False
        else:
            if t.right != None:
                return self.minimum(t.right)
            else:
                y = t.parent
                while(y != None and t == y.right):
                    t = y
                    y = t.parent
                if y == None:
                    return None
                else:
                    return t
def inorder(root):
    if root is not None:
        print(root.key, end = " ")
        inorder(root.left)
        
        inorder(root.right)

def main():
    Tree = BST()
    for i in range(10, -1, -1):
        Tree.insert(i, chr(i+ord('a')))
    inorder(Tree.root)
    print()
    print(Tree.search(10))
    #print(Tree.search(-1))
    #print(Tree.successor(5).key)
if __name__ == "__main__":
    main()
            