
from array import *

class Node:
    value = None
    tail = None

    def __init__(self,value, tail=None) -> None:
        self.value = value
        self.tail = tail
        


class Stack: 
    top = None
    length = 0

    def peek(self):
        pass

    def push(self , value):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        pass


class StackNodeImp(Stack):

    
    def push(self,value):
        newNode = Node(value)
        if(self.top == None):
            self.top = newNode
        else:
            newNode.tail  = self.top
            self.top = newNode
        self.length += 1
            


    def pop(self):
        if(self.length  > 0):
            self.length -= 1

        if(self.top == None):
            return None
        else:
            currentNode = self.top
            self.top = currentNode.tail
            value = currentNode.value
            del currentNode
            return value
        
    def peek(self):
        if(self.top == None):
            return None
        return self.top.value
    
    def isEmpty(self) -> bool:
        if(self.top == None):
            return True
        return False
    

class StackArrayImpl(Stack):

    data = None

    def __init__(self, type) -> None:
        super().__init__()
        self.data = array(type)

    def peek(self):
        try:
            return self.data[len(self.data) - 1]
        except IndexError as e:
            return None
        

    def push(self , value):
        self.length +=1
        return self.data.append(value)

    def pop(self):
        if(self.length  > 0):
            self.length -= 1
        try:
            return self.data.pop()
        except IndexError as e:
            return None

    def isEmpty(self):
        return len(self.data) == 0

        
        
    
        

# testStack = StackNodeImp()
# testStack = StackArrayImpl('i')

# testStack.push(1)
# testStack.push(2)
# testStack.push(3)

# print('isEmpty :',testStack.isEmpty())
# print('Length is :',testStack.length)
# print('Peek :',testStack.peek())
# print(testStack.pop())
# print(testStack.pop())
# print(testStack.pop())
# print(testStack.pop())
# print('Peek :',testStack.peek())
# print('Length is :',testStack.length)
# print('isEmpty :',testStack.isEmpty())



class Queue :
    first = None
    last = None
    length = 0

    def peek(self):
        pass
    def enqueue(self, value):
        pass
    def dequeue(self):
        pass

    def isEmpty(self):
        pass


class QueueNodeImpl(Queue):

    def enqueue(self, value):
        self.length += 1
        newNode = Node(value)
        if(self.first == None):
            self.first = newNode
            self.last = newNode
        elif(self.first == self.last):
            self.last = newNode
            self.first.tail = newNode
        else:
            self.last.tail = newNode
            self.last  = newNode

    def dequeue(self):
        if(self.length  > 0):
            self.length -= 1

        if(self.first == None):
            return None
        elif(self.first == self.last):
            value = self.first.value
            self.last = None
            self.first = None
            return value
        else:
            value = self.first.value
            self.first = self.first.tail
            return value
            
    def peek(self):
        if(self.last != None):
            return self.last.value
        else:
            return None

    def isEmpty(self):
        return self.first == None



myQueue =  QueueNodeImpl()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print('isEmpty :',myQueue.isEmpty())
print('Length is :',myQueue.length)
print('Peek :',myQueue.peek())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print('Peek :',myQueue.peek())
print('Length is :',myQueue.length)
print('isEmpty :',myQueue.isEmpty())



class MyQueue:
    s1  = None
    s2  = None
    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x: int) -> None:
        self.s1.append(x)


    def pop(self) -> int:
        for x in range(len(self.s1) - 1):
            self.s2.append(self.s1.pop())
        
        value = self.s1.pop()

        for x in range(len(self.s2)):
            self.s1.append(self.s2.pop())

        return value
          
        

    def peek(self) -> int:
        for x in range(len(self.s1) - 1):
            self.s2.append(self.s1.pop())
        
        value = self.s1.pop()
        self.s2.append(value)


        for x in range(len(self.s2)):
            self.s1.append(self.s2.pop())

        return value
        

    def empty(self) -> bool:
        return len(self.s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.empty())
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()