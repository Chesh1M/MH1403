'''
Lab 4 Task 1   
'''

# ========================================
# Implement you merge sort function below. 

def mergeSort(txt_to_sort):
    if len(txt_to_sort) > 1:
        mid = len(txt_to_sort) // 2 # get index of middle of list
        left_half = txt_to_sort[:mid] # create list "left" to store all the elements of "txt_to_sort" up till mid point
        right_half = txt_to_sort[mid:] # create list "right" to store all the elements of "txt_to_sort" from mid point till end

        # keep on calling until the list has been broken down into size len = 1, after which code below will run to merge the lists back piece by piece
        mergeSort(left_half)
        mergeSort(right_half)

        # initialize variables a,b to keep track of the position inside each left/right list and 
        # var c to track position in original txt_to_sort list
        a = b = c = 0

        # continue to loop while a or b havent reach the end of the left/right list
        while a < len(left_half) and b < len(right_half):
            if left_half[a] <= right_half[b]: # if ele in left list is smaller
                txt_to_sort[c] = left_half[a] # overwrite the element in txt_to_sort in the respective index
                a += 1 # increment counter by 1
            else:
                txt_to_sort[c] = right_half[b]
                b += 1
            c += 1
        
        # in case one side still has elements not added while the other side already reached the end
        while a < len(left_half):
            txt_to_sort[c] = left_half[a]
            a += 1
            c += 1
            
        while b < len(right_half):
            txt_to_sort[c] = right_half[b]
            b += 1
            c += 1
    
    return txt_to_sort


#=======================================
# read the file malayenglish.txt
# it returns a list called malayEnglishList 
# each element of malayEnglishList is a string consists of a Malay word and its English translation 
def readFile(fileName):  
    f = open(fileName)  
    lines = f.readlines() #data is a list, each element of data is one line of the file  
    f.close()  
    
    malayEnglishList = []  
    for line in lines: 
        #remove the line break character '\n' at the end of a line
        line = line.rstrip()
        malayEnglishList.append(line)  

    return malayEnglishList  



# driver code       
if __name__=='__main__': 
    #=========================================
    # each element of malayenglishlist is a string consists of a Malay word and its English translation     
    malayEnglishList = readFile("malayenglish.txt")  

    # perform merge sort 
    malayEnglishList = mergeSort(malayEnglishList)  

    f = open("malayenglish_sorted.txt", "w")  # open file for write 
    for i in range(len(malayEnglishList)):  
        f.write(malayEnglishList[i]) 
        # write the character "\n" at the end of each line to start a new line 
        # "\n" is not needed for the last line 
        if i != len(malayEnglishList)-1: 
            f.write("\n") 
    f.close()     # close the file 

     
    """
    # print dictionary
    for index, item in enumerate(malayEnglishList, 1):
        print(f"{index}: {item}", end='\n') 
    """

    
        