#! /usr/bin/python3

def binarySearch(alist, key):
    ''' Binary search: searches ordered list by divide and conquer  ,time Complexity: O(log(n)) '''
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        mid = (first + last)//2

        if key == alist[mid]:
            found = True
        elif key < alist[mid]:
            last = mid-1
        else:
            first = mid+1

    return found


def binarySearchR(alist, key):
    ''' Binary search recursive: searches ordered list by divide and conquer  ,time Complexity: O(log(n)) '''
    if len(alist) == 0:
        return False
    mid = len(alist)//2
    if alist[mid] == key:
        return True
    elif key < alist[mid]:
        return binarySearchR(alist[:mid], key)
    else:
        return binarySearchR(alist[mid+1:], key)

testlist = [1 ,2, 8, 19, 21, 30, 42]

print(binarySearch(testlist, 1)) #iterative
print(binarySearchR(testlist, 42)) #recursive
