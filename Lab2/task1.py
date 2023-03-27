class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0

    # find a node which contains the data matching the input value 
    def findNode(self, value): 
        curr = self.head
        while curr:
            if curr.data == value:
                return curr
            curr = curr.next 
        return curr 

    # add a new node as the first node      
    def addNode(self, data):
        newNode = Node(data)  # create the new node 
        newNode.next = self.head 
        self.head = newNode
        self.size+=1

    # print the data in all the nodes 
    def printNode(self):
        listprint = [] 
        curr = self.head
        while curr:
            listprint.append(curr.data)
            curr = curr.next 
        print(listprint) 
    
    # reverse method
    def reverse(self):
        # Set initial values
        prev = None # previous tracks the previous node
        curr = self.head # current tracks the current node
        tracker = curr.next # tracker tracks the node infront to ensure link doesn't get lost
        
        while curr:
            curr.next = prev # points current node to node behind it
            prev = curr # makes the curr node the new prev node
            curr = tracker # moves curr forward by one node (the one tracker is tracking)
            if tracker: # if still have nodes ahead (not on the NULL node)
                tracker = tracker.next # move tracker forward by one node
            
        self.head = prev # set the new head to the final "prev" node which is the original last node
        
mylinkedlist = LinkedList()

for i in range(5):
    mylinkedlist.addNode(2*i)

mylinkedlist.printNode()  


linkedlistA = LinkedList()
for i in range(1,6):
    linkedlistA.addNode(i)
linkedlistA.printNode()
linkedlistA.reverse()
print("After reversing the linked list, the linked list becomes:")
linkedlistA.printNode()
