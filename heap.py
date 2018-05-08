#! /usr/bin/python3
''' Min binary Heap is binary tree represented in an array where parent is lesser than or equal to child ,
     if parent in in index  i then its left child is at i*2 and right child is in (i*2)+1 for 1 indexed-array
     if parent in in index  i then its left child is at (i*2)+1 and right child is in (i*2)+2 for 0 indexed-array
     '''

class BinHeap:
    ''' Binary min-Heap List with 1 indexed-array , Almost complete binary tree'''
    def __init__(self):
        #You will notice that an empty binary heap has a single zero as the first element of heapList and that this zero is not used,
        #but is there so that simple integer division can be used in later methods.
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        ''' insert k into heap array & still maintain heap order'''
        self.heapList.append(k) # insert at end
        self.currentSize += 1
        self.perUp(self.currentSize) # percolate it up

    def perUp(self, i):
        ''' percolate up the value in i to appropriate position in heap'''
        while i//2 > 0: # go till 1 , i//2 returns parent
            if self.heapList[i] < self.heapList[i//2]:
                # swap parent & child if child is smaller than parent, min heap( h[0] is min)
                self.heapList[i] , self.heapList[i//2] = self.heapList[i//2] , self.heapList[i]
            i = i//2  # since you moved till parent , now check with next parent

    def delMin(self):
        ''' delete min in heap & return , & still maintain heap'''
        min_value = self.heapList[1] # min in heap
        self.heapList[1] = self.heapList[self.currentSize] # put last element to root
        self.currentSize -= 1
        self.heapList.pop()  # del last element, because u stored it in [1]
        self.perDown(1)  # percolate it down from root to down , just to rebuild heap after delMin
        return min_value

    def perDown(self, i):
        ''' percolate down the value in i '''
        while (i*2) <= self.currentSize: # go till size , i*2 gives left child
            min_child = self.minChild(i)
            if self.heapList[i] > self.heapList[min_child]:
                #swap parent and min child
                self.heapList[i] , self.heapList[min_child] = self.heapList[min_child] , self.heapList[i]
            i = min_child # since you moved till minChild , now check with next children

    def minChild(self, i):
        ''' find minimum of two children and return index'''
        if (i*2)+1 > self.currentSize: #if there is only one child
            return i*2 #return left one (almost complete binary tree)
        else : # decide b/w two children
            if self.heapList[i*2] > self.heapList[(i*2)+1] :
                return (i*2)+1
            else:
                return i*2

    def buildHeap(self, alist):
        ''' return a heapified list O(nlogn) or O(logn)'''
        i = len(alist)//2
        self.currentSize = len(alist) # putting currentsize value
        self.heapList = [0] + alist[:] # making heap list from index 1 , easy for our method of p -> 2*p & (2*p)+1
        while i > 0: # go till 1 & heapify , going for log n deep for all n elements. so O(nlogn)
            self.perDown(i)
            i -= 1

    # Although we start out in the middle of the tree and work our way back toward the root,
    #the percDown method ensures that the largest child is always moved down the tree.
    #Because the heap is a complete binary tree,any nodes past the halfway point will be leaves and therefore have no children

alist = [9,5,6,2,3]
bh = BinHeap()
bh.buildHeap(alist)

print(bh.heapList)
bh.insert(4)
print(bh.heapList)
print(bh.delMin())
'''The assertion that we can build the heap in O(n) may seem a bit mysterious at first, and a proof is beyond the scope of this book.
 However, the key to understanding that you can build the heap in O(n) is to remember that the logn factor is derived from the height
 of the tree.For most of the work in buildHeap, the tree is shorter than logn.'''
