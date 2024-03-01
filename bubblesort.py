class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(5)
head.next.next.next.next = Node(4)

def swapnodes(head, x,y):
    if x== y:
        return
    currx = head
    prevx = None
    while (currx) and (currx.data!= x):
        prevx = currx
        currx = currx.next
        
    curry = head
    prevy = None
    while (curry) and (curry.data != y):
        prevy = curry
        curry = curry.next
        
    if (currx == None) or (curry == None):
        return
    
    if prevx is not None:
        prevx.next = curry
    else:
        head = curry
        
    if prevy is not None:
        prevy.next = currx
    else:
        head = currx

    temp = curry.next
    curry.next = currx.next
    currx.next = temp
    
    
def bubblesort(head):
    if head == None:
        return
    start= head
    while(start):
        ptr = start.next
        if ptr:
            if start.data > ptr.data:
                swapnodes(head, start.data, ptr.data)
        start = start.next
    return head
def display(root):
    if root == None:
        return None
    temp = root
    while(temp):
        print(str(temp.data), end = " ") 
        temp = temp.next    
    
x = bubblesort(head)
display(x)
    
        
        