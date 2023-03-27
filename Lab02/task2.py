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


# def copylinkedlist(current_list):
#     new_list = LinkedList()
#
#     curr = current_list.head # set curr to first node
#     last_node_tracker = None # tracker to None
#
#     while last_node_tracker != curr: #
#         while curr.next != last_node_tracker: # continue loop while next node isn't None
#             curr = curr.next # loop until curr = the node right before the final node
#         last_node_tracker = curr # once curr is at final node, replace tracker with the last node
#         new_list.addNode(last_node_tracker.data) # addNode with the data of the last node
#         curr = current_list.head
#
#     return new_list

# faster method
def copylinkedlist(current_list):
    new_list = LinkedList()

    new_list_data = []
    curr = current_list.head

    while curr != None:
        new_list_data.insert(0, curr.data)
        curr = curr.next

    for x in range(len(new_list_data)):
        new_list.addNode(new_list_data[x])

    return new_list

linkedlistA = LinkedList()
for i in range(1,6):
    linkedlistA.addNode(i)
linkedlistB = copylinkedlist(linkedlistA)
# modify linkedlistA
curr = linkedlistA.head
for i in range(linkedlistA.size):
    curr.data += 10
    curr = curr.next
linkedlistA.printNode()
linkedlistB.printNode()
