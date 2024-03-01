class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next = Node(5)

def reorder(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
     
    second = slow.next
    slow.next = None
    prev = None
    while (second):
        next = second.next
        second.next = prev
        prev = second
        second = next
    
    first, second = head, prev
    while (second):
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
    return head
    
def display(root):
    if root == None:
        return None
    temp = root
    while(temp):
        print(str(temp.data), end = " ") 
        temp = temp.next
x =  reorder(head)    
display(x)       
