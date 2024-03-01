class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next = Node(5)

def delOccuranceOfKey(head, key):
    temp = head
    prev = None
    while (temp!= None) and (temp.data == key):
        head = temp.next
        temp = head

    while(temp!= None):
        if (temp.data != key) :
            prev = temp
            temp = temp.next
        else:
            prev.next = temp.next
            temp = prev.next
    return head
def display(root):
    if root == None:
        return None
    temp = root
    while(temp):
        print(temp.data)
        temp = temp.next
x =  delOccuranceOfKey(head, 2)
print(display(x))
            