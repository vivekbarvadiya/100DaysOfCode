class MinStack(object):

    def __init__(self):
        self.arr=[]
        self.min_stack=[]

    def push(self, val):
        self.arr.append(val)
        if self.min_stack==[] or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.arr==[]:
            return -1
        if self.arr[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.arr.pop()
        

    def top(self):
        if self.arr==[]:
            return -1
        return self.arr[-1]
        

    def getMin(self):
        if self.min_stack==[]:
            return -1
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()