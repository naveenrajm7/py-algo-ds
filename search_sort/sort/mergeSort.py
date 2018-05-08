#! /usr/bin/python3

''' Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single  '''

def mergeSort(alist):
    ''' merge sort:   ,time Complexity: O(nlogn)'''
    print('spliting',alist)
    if len(alist) > 1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        
        mergeSort(left_half)
        mergeSort(right_half)
        
        i=0
        j=0
        k=0
        
        #comparing and merging
        while i<len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i+ 1
            else:
                alist[k] = right_half[j]
                j = j+ 1
            k =k+ 1
        #filling remaing elements
        while i<len(left_half):
            alist[k] = left_half[i]
            i =i+ 1
            k =k+ 1
            
        while j<len(right_half):
            alist[k] = right_half[j]
            j =j+ 1
            k =k+ 1         
    print('merging',alist)
        
testlist = [54 ,26, 96, 17, 77, 31, 44, 55, 20]
testlist1 = [1, 0, 23, 12, 5, 7]

mergeSort(testlist) 
print(testlist) 
#mergeSort(testlist1) 
#print(testlist1)
