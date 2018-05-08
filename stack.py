# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
# what did i learn
# stack , check for all possibilties ,
# whenever using index of list see that you check b4 access  or handle IndexError exception
class MyStack:
    def __init__(self):
        self.stack=[]
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else :
            return False
   
    def push(self,x):
        self.stack.append(x)
        
    def pop(self):
        self.stack.pop()
        

def is_matched(expression):
    stack1 = MyStack()
    for sym in expression:
        if sym in ['{','[','(']:
            stack1.push(sym)
        else:
            if not stack1.isEmpty():
                if (sym == '}' and stack1.stack[-1] == '{') or (sym == ']' and stack1.stack[-1] == '[') or (sym == ')' and stack1.stack[-1] == '('):
                    stack1.pop()
                else :
                    return False
            else :
                return False
                        
    return stack1.isEmpty()
      
    
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

