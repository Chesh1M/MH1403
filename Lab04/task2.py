'''
Lab 4 Task 2 
'''

#=========================================  
# Binary Search Function  
# Implement your binary search function below. 


def binarySearch(dictionary, malayWord):
    # set left/right vars to first and last index of dictionary
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        # if middle ele is target word
        if dictionary[mid][0] == malayWord:
            return dictionary[mid][1] # return corresponding translated word
        
        # if target word is bigger than middle word
        elif dictionary[mid][0] < malayWord:
            left = mid + 1 # shift the left marker to the right of mid point
        
        # if target word is smaller than middle word
        else:
            right = mid - 1 # shift right marker to left of mid point
    
    return None


# =======================================
# read the file malayenglish.txt
# it returns a list called malayEnglishList 
# each element of malayEnglishList is a small list with two elements: a Malay word and its English translation 
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
    malayEnglishList = readFile("malayenglish.txt")  
    
    # sort malayEnglishList using the embedded Python sorting method/function       
    malayEnglishList.sort() 
    
    '''
    # Print dictionary
    for index, item in enumerate(malayEnglishList, 1):
        print(f"{index}: {item}", end='\n') 
    '''

    while True:     
        malayWord = input('Enter a Malay word, or enter exit: ')
        if (malayWord == "exit"):
            print('Program exits.') 
            break  
        else:  
            englishTranslation = binarySearch(malayEnglishList, malayWord)  
            if (englishTranslation == None):
                print('Cannot find the Malay word ' + malayWord) 
            else:
                print(malayWord + ': ' + englishTranslation)    
#===========================================
    