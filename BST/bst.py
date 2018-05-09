class TreeNode:
    def __init__(self, key, val=None, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChild(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.value = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        currentNode = self
        while currentNode.hasLeftChild():
            currentNode = currentNode.leftChild
        return currentNode

    def spliceOut(self):
        '''successor is guarenteed to have no more than one child'''
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                return self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                return self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        return self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key :
            return currentNode
        elif key < currentNode.key :
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove =  self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error , Key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error , Key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def remove(self, currentNode):
        # The node to be deleted has no children
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren(): # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.value = succ.value
            currentNode.key = succ.key

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # its root node
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.value,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else: # its root node
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.value,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


    def canInsert(self, key, k):
        if self.root:
            return self._canInsert(key, k, self.root)
        else:
            return True

    def _canInsert(self, key, k, currentNode):
        if not currentNode:
            return True
        elif (key == currentNode.key) or (not (currentNode.key <= key-k or currentNode.key >= key+k)):
            return False
        elif key < currentNode.key :
            return self._canInsert(key, k, currentNode.leftChild)
        else:
            return self._canInsert(key, k, currentNode.rightChild)

    def inorder(self, currentNode):
        if not currentNode:
            return None
        self.inorder(currentNode.leftChild)
        print(currentNode.key,end="\t")
        self.inorder(currentNode.rightChild)

    # Agumented BinarySearchTree for getting rank -> no of previous scheduled times (kth smallest element)
    # AVL tree for actual log(n)

if __name__ == "__main__":
    print("Zebra Airlines -\n \t nobody takes you higher")
    print("-"*5,"Welcome to Single Runaway reservation system","-"*5)
    schedule = BinarySearchTree()
    k = int(input("your data structure is ready.. enter k value\n"))
    close = False
    while not close:
        c = int(input("enter choice:\n1.Request time\t2.Print schedule\t3.delete time\t4.Exit\n"))
        if c == 1:
            time = int(input("Enter requesting time:\n"))
            if schedule.canInsert(time, k):
                schedule.put(time, None)
                print("request success")
            else:
                print("request failed")
        elif c == 2:
            print("Currently scheduled timings")
            #schedule.inorder(schedule.root)
            for x in schedule.root:
                print(x,end="\t")
            print("")
        elif c == 3:
            time = int(input("Enter delete time:\n"))
            try :
                del schedule[time]
            except KeyError as e:
                print("Error:", e)
        elif c == 4:
            close = True
        else:
            print("Wrong choice")
