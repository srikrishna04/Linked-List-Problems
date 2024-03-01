class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
 
    def push(self, x):
        newnode = Node(x)
        newnode.next = self.head
        self.head = newnode
 
    # Utility function to print the LinkedList
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
 
 
# Driver code
llist = LinkedList()
llist.push(10)
llist.push(40)
llist.push(15)
llist.push(35)
 
print ("Given linked list")
llist.display()
llist.reverse()
print ("\nReversed linked list\n")
print(llist.display())
 