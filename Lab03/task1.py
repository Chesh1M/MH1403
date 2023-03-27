'''
Lab 3 Task 1 
'''

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
    
    # 'insertNode' method to insert a new node into binary tree
    def insertNode(self, data):
        if self.data == None: # if root node is empty
            self.data = data
            return

        if self.data > data: # if root node is bigger than the input data
            if self.left: # if left child node of root is not empty
                self.left.insertNode(data) # perform insertNode again
            else: # if left child node of root is empty
                self.left = BST(data) # create a node there containing the input data
        
        if self.data < data: # if root node is smaller than the input data
            if self.right:
                self.right.insertNode(data)
            else:
                self.right = BST(data)
        
        if self.data == data: # if duplicate data
            return


    # preorderTraversal
    def preorderTraversal(self):
        preorder_list.append(self.data)
        # to print as data itself instead of storing as list
        # print(self.data)
                
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()            

        return preorder_list

    # inorderTraversal
    def inorderTraversal(self):                
        if self.left:
            self.left.inorderTraversal()
        
        inorder_list.append(self.data)
        # to print as data itself instead of storing as list
        # print(self.data)
        
        if self.right:
            self.right.inorderTraversal()            

        return inorder_list

    # postorderTraversal
    def postorderTraversal(self):                
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()            
        
        postorder_list.append(self.data)
        # to print as data itself instead of storing as list
        # print(self.data)

        return postorder_list


    # 'findNode' method to find a given value
    def findNode(self, name):
        if self.data[0] == name:
            return self.data[1]
        elif self.data[0] < name:
            # go right
            if self.right == None:
                return None
            else:
                return self.right.findNode(name)
        elif self.data[0] > name:
            # go left
            if self.left == None:
                return None
            else:
                return self.left.findNode(name)

    # 'deleteNode' method to delete a node
    def deleteNode(self, value):
        pass


mybst = BST(None)
for i in range(0,7):
    mybst.insertNode((i*17 + 3)%37)

# Create lists for 3 traversals
preorder_list = []
inorder_list = []
postorder_list = []

# Populate lists with corresponding data
preorder_list = mybst.preorderTraversal()
inorder_list = mybst.inorderTraversal()
postorder_list = mybst.postorderTraversal()

# Print lists of different traversals
print("This is a preorder list: ", preorder_list)
print("This is an inorder list: ", inorder_list)
print("This is a postorder list: ", postorder_list)


# Binary Tree for students grades records
class_4E2 = BST(None)

class_4E2.insertNode(['John', 86]) # 3
class_4E2.insertNode(['Felix', 76]) # 1
class_4E2.insertNode(['Tom', 56]) # 4
class_4E2.insertNode(['Hanks', 88]) # 2
class_4E2.insertNode(['Wick', 93]) # 5

while True:
    userinput = input("\nEnter name of student to check his score, else type 'exit' to quit: ")
    userinput = userinput.capitalize()

    if userinput == "Exit":
        print("You have quit the program\n")
        break
    
    score = class_4E2.findNode(userinput)
    if score:
        print(f"{userinput} has scored {score}!")
    elif score == None:
        print("The name is not in the list!")
    
