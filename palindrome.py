class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next = Node(5)

def palindrome(head):
    if head == None:
        return True
    stack = []
    temp = head
    while(temp):
        stack.append(temp.data)
        temp = temp.next
    ptr = head
    while (ptr):
        i =stack.pop()
        if i == ptr.data:
            palin =True
        else:
            return False
            break
        ptr= ptr.next
    if palin == True:
        return True
print(palindrome(head))
