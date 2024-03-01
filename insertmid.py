# array to list
#insert value at middle of linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def insertAtMid(head, x):
    if head == None:
        head = Node(x)
    else:
        temp = head
        len = 0
        while(temp):
            len += 1
            temp = temp.next
            
        count = 0
        if len%2 == 0:
            count = len/2
        else:
            count = (len+1)/2
        ptr = head
        while count>1:
            count -= 1
            ptr = ptr.next
        newnode = Node(x)
        newnode.next = ptr.next
        ptr.next = newnode

def display(head):
    if head == None:
        return None
    temp = head
    while (temp!=None):
        print(str(temp.data), end = " ") 
        temp = temp.next
    print('\n')

def insert(head, x):
    if head == None:
        head = Node(x)
    else:    
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(x)
    return head




arr = [1,2,3,4,5]
head = None
for i in range(len(arr)):
    head = insert(head, arr[i])
print(head)
display(head)
insertAtMid(head, 9)
display(head)