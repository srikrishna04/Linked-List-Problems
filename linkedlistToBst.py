class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next = Node(5)


class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bstFromList(n):
    global head
    if n <= 0:
        return None
    left =  bstFromList(int(n/2))
    root = TNode(head.data)
   
    root.left = left
    head = head.next
    root.right =  bstFromList(n - int(n/2) - 1)
    return root
    
def preOrder(root):
    if root == None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
    
# length of list= 5
x =  bstFromList(5)
preOrder(x)
