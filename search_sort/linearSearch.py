#! /usr/bin/python3

def linearSearch(alist, key):
    ''' Linear search: searches sequential  ,time Complexity: O(n) '''
    found = False
    pos = 0
    
    while pos < len(alist) and not found:
        if alist[pos] == key:
            found = True
        else:
            pos += 1
        
    return found        

testlist = [1 ,2, 32, 8, 19, 42, 13, 0]

print(linearSearch(testlist, 3))
print(linearSearch(testlist, 13)) 
