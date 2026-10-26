class TreeNode:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def InOrderTraversal(root):
    if root:
        if root.left:
            InOrderTraversal(root.left)
        print(root.data)
        if root.right:
            InOrderTraversal(root.right)

def Insert(root,n):
    if root == None:
        return TreeNode(n)

    if n < root.data:
        root.left = Insert(root.left,n)
    else:
        root.right = Insert(root.right,n)
    return root

def SearchandDelete(root,key):
    if root is None:
        return root

    if key < root.data:
        root.left = SearchandDelete(root.left,key)

    elif key > root.data:
        root.right = SearchandDelete(root.right,key)\

    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValue(root.right)
        root.data = temp.data
        root.right = SearchandDelete(root.right,temp.data)

        root = SearchandDelete(root,key)
    return root

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

a = int(input("Enter the number of nodes: "))
root = None

for i in range(a):
    n = int(input("Enter the value of the nodes: "))
    root = Insert(root,n)

print("BST before deletion: ")
InOrderTraversal(root)
d = int(input("Enter the number you want to delete: "))
root = SearchandDelete(root,d)
print("BST after deletion: ")
InOrderTraversal(root)
    
