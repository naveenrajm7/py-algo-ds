#! /usr/bin/python3
''' To analyze the quickSort function, note that for a list of length n, if the partition always occurs in the middle of the list, there will again be logn divisions. In order to find the split point, each of the n items needs to be checked against the pivot value. The result is nlogn

. In addition, there is no need for additional memory as in the merge sort process.

Unfortunately, in the worst case, the split points may not be in the middle and can be very skewed to the left or the right, leaving a very uneven division. In this case, sorting a list of n items divides into sorting a list of 0 items and a list of n−1
items. Then sorting a list of n−1 divides into a list of size 0 and a list of size n−2, and so on. The result is an O(n2) sort with all of the overhead that recursion requires.'''


def quickSort(alist):
        ''' quick sort: O(nlogn) best case , but O(n^2) worst case'''
        quickSortHelper(alist, 0, len(alist)-1)
        
        
def quickSortHelper(alist, first, last):
        ''' quick sort by recursive '''
        if first<last:
                split_point = partition(alist, first, last)

                quickSortHelper(alist, first, split_point-1)
                quickSortHelper(alist, split_point+1, last)


def partition(alist, first, last):
        ''' to find split_point '''
        pivot_value = alist[first]

        left_mark = first + 1
        right_mark = last

        done = False

        while not done:

                while alist[left_mark] <= pivot_value and left_mark <= right_mark :
                        left_mark += 1

                while alist[right_mark] >= pivot_value and left_mark <= right_mark :
                        right_mark -= 1

                if left_mark > right_mark :
                        done = True
                else:
                        alist[left_mark],alist[right_mark] =  alist[right_mark],alist[left_mark] #sawpping left & right

        alist[first],alist[right_mark] =  alist[right_mark],alist[first] #swapping pivot from first to where it belongs

        return right_mark

alist = [23, 12, 3, 34, 41, 56, 18]
quickSort(alist)
print(alist)
