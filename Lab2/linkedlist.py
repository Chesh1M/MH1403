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


mylinkedlist = LinkedList()

for i in range(5):
    mylinkedlist.addNode(2*i)

mylinkedlist.printNode()  
