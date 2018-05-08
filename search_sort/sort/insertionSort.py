#! /usr/bin/python3

''' The insertion sort, although still O(n2), works in a slightly different way. It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger. '''

def insertionSort(alist):
    ''' insertion sort:   ,time Complexity: O(n^2)'''
    for unsorted in range(1,len(alist)): #for each element in unsorted list
        current_value = alist[unsorted]
        sorted_i = unsorted-1
        while sorted_i >= 0 and alist[sorted_i] > current_value:#for each element in sorted list
            alist[sorted_i+1] = alist[sorted_i]     #move sorted element to right if the current value is large
            sorted_i -= 1 #move current sorted pos to left
        alist[sorted_i+1] = current_value #the swap position
                
testlist = [1 ,2, 8, 5, 21, 30, 42]
testlist1 = [1, 0, 23, 12, 5, 7]

insertionSort(testlist) 
print(testlist) 
insertionSort(testlist1) 
print(testlist1)
