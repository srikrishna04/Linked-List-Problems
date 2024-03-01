class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(1)
head.next.next.next.next = Node(5)


def removeDuplicates(head):
    ptr1 = head
    while(ptr1) and (ptr1.next):
        ptr2 = ptr1
        while(ptr2.next):
            if ptr1.data == ptr2.next.data:
                ptr2.next = ptr2.next.next
            else:
                ptr2 = ptr2.next
        ptr1 = ptr1.next
    return head
    
def display(root):
    if root == None:
        return None
    temp = root
    while(temp):
        print(temp.data)
        temp = temp.next
x = removeDuplicates(head)
display(x)