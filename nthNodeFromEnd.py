# display nth node from end
# delete nth node from end

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next = Node(5)


def nthNodeFromEnd(head, n):
    if head == None:
        return None
    temp = head
    len = 0
    while(temp):
        len += 1 
        temp =  temp.next
    if n > len:
        return None
    x = len - n +1
    ptr = head
    while(x>1):
        ptr = ptr.next
        x = x-1
    return ptr.data
print(nthNodeFromEnd(head, 4))

def deleteNthNodeFromEnd(head, n):
    if head == None:
        return None
    temp = head
    len = 0
    while(temp):
        len += 1 
        temp =  temp.next
    if n > len:
        return None
    if n == len:
        temp = head
        head = temp.next
        return head
    x = len - n +1
    prev = None
    curr = head
    while (x>1):
        prev = curr
        curr = curr.next
        x = x-1
    prev.next = curr.next
    curr = prev.next
    return head
def display(root):
    if root == None:
        return None
    temp = root
    while(temp):
        print(str(temp.data), end = " ")
        temp = temp.next
x =deleteNthNodeFromEnd(head, 2)
display(x)
        