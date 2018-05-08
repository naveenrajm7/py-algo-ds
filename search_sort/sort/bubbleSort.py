#! /usr/bin/python3

def bubbleSort(alist):
    ''' bubble sort:   ,time Complexity: O(n^2) '''
    for passnum in range(len(alist)-1,0,-1):
        for j in range(passnum):
            if alist[j]>alist[j+1]:     #carrying large element to last position
                alist[j], alist[j+1] = alist[j+1], alist[j]
    

def bubbleSortO(alist):
    ''' bubble sort Optimized: stops once no more swaps required  ,time Complexity: O(log(n)) '''
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges: #if no excahnge required in some pass then no exchange occurs in next pass
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1
                
testlist = [1 ,2, 8, 5, 21, 30, 42]
testlist1 = [1, 0, 23, 12, 5, 7]

bubbleSort(testlist) # general
print(testlist) 

bubbleSortO(testlist1) #optimized
print(testlist1)
