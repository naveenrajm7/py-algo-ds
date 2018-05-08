#! /usr/bin/python3

'''    The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.
 the selection sort makes the same number of comparisons as the bubble sort and is therefore also O(n2). However, due to the reduction in the number of exchanges, the selection sort typically executes faster in benchmark studies. '''

def selectionSort(alist):
    ''' selection sort:   ,time Complexity: O(n^2)'''
    for fillslot in range(len(alist)-1,0,-1):
        posOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[posOfMax]:
                posOfMax = location
                
        alist[posOfMax], alist[location] = alist[location], alist[posOfMax]
                          
testlist = [1 ,2, 8, 5, 21, 30, 42]
testlist1 = [1, 0, 23, 12, 5, 7]

selectionSort(testlist) 
print(testlist) 

selectionSort(testlist1) 
print(testlist1)
