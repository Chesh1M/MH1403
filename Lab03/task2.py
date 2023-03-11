'''
Lab 3 Task 2 
'''
    
from gettext import find


class BST:   
    def __init__(self, data): 
        self.data = data
        self.leftChild = None
        self.rightChild = None 

    # "insertNode" method to insert a new node
    def insertNode(self,data):
        # check if root node is empty  
        if self.data == None: 
            self.data = data
            return

        # ignore duplicate word
        if self.data == data: 
            return

        # if the word in the curernt node is bigger than the input word (based on ascii values, i.e. a < b < c)
        if self.data > data: 
            if self.leftChild: # if left child is not empty,
                self.leftChild.insertNode(data) # call insertNode method again
            else:
                self.leftChild = BST(data) # else create a new node right there

        # if the word in the current node is smaller than the input word
        if self.data < data: 
            if self.rightChild: 
                self.rightChild.insertNode(data)
            else:
                self.rightChild = BST(data)          

    # "find" method to find corresponding node
    def find(self, malayWord):
        # if root is the word itself
        if self.data[0] == malayWord: # [0] element represents the malay word, [1] element represents the english translation 
            return self.data[1]

        # if root is > word user is trying to find
        elif self.data[0] > malayWord: 
            if self.leftChild == None: # if leftChild == None, means no more nodes to its left anymore (its the final node)
                return self.leftChild # so return None, aka unable to find the word
            else:
                return self.leftChild.find(malayWord)
        # if root is < word user is trying to find
        elif self.data[0] < malayWord:
            if self.rightChild == None:
                return self.rightChild
            else:
                return self.rightChild.find(malayWord) 

        
# =======================================
# read the file malayenglish.txt
# it returns a list called malayEnglishList 
# each element of malayEnglishList is a small list with two elements (2d list): a Malay word and its English translation 
def readFile(fileName):   
    f = open(fileName)  # open the file 
    lines = f.readlines() #lines is a list, each element of lines is one line of the file  
    f.close()           # close the file 
    
    malayEnglishList = []    
    for line in lines: 
        # remove the line break character '\n' at the end of a line
        line = line.rstrip()
        # retrieve the malayWord as the first 27 characters from a line  
        malayWord = line[:27]   
        # remove the extra spaces at the end of a malayword 
        malayWord = malayWord.rstrip()  
        # from a line retrieve the english translation starting from the 28th character  
        englishTranslation = line[27:]    
        
        malayEnglishList.append([malayWord, englishTranslation]) 
        
    return malayEnglishList  


# driver code       
if __name__=='__main__': 
    # Read the file 
    # each element of malayEnglishList is a small list with two elements (list of lists): a Malay word (corr index: [0]) and its English translation (corr index: [1])      
    malayEnglishList = readFile("malayenglish.txt")   
         
    mybst = BST(None)   
    # insert every element of malayEnglishList into mybst  
    for x in malayEnglishList: 
        mybst.insertNode(x)   

    # ask user to input a Malay word, 
    # then lookup the dictionary (stored in the binary search tree)
    while True:     
        malayWord = input('Enter a Malay word, or enter exit: ')
        if (malayWord == "exit"):
            print('Program exits.') 
            break  
        else:
            englishTranslation = mybst.find(malayWord)  
            if (englishTranslation == None):
                print('Cannot find the Malay word ' + malayWord) 
            else:
                print(malayWord + ': ' + englishTranslation)    
            


    