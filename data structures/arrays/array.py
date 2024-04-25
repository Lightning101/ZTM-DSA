
class DoubleNode:
    head = None
    tail = None
    data = None

    def __init__(self, data, first = None, last = None) -> None:
        self.data = data
        self.head = first
        self.tail = last
class SingleNode:
    tail = None
    data = None

    def __init__(self, data, tail = None) -> None:
        self.data = data
        self.tail = tail

class LinkedList():
    head  = None
    length = 0

    def getNode(self, index):
        item = self.head
        if(item == None):
            return None
        for x in range(index):
            if(item.tail == None):
                return None
            else:
                item = item.tail
        return  item
    
    def changeLength(self,op):
        if(op == '+'):
            self.length +=1
        else:
            self.length -=1


    def getLast(self):
        if(self.head == None):
            None
        else:
            lastNode = self.head
            while( lastNode.tail != None):
                lastNode = lastNode.tail
            return lastNode
        
    def get(self,index):
        item = self.getNode(index)
        if(item == None):
            return None
        return   item.data
    
    def push(self,data):
        pass

    def pop(self):
        pass
    
    def splice(self,index):
        pass
    
    def insert(self,index, value):
        pass
    

class SingleLinkedList(LinkedList):


    def get(self,index):
        item = self.getNode(index)
        if(item == None):
            return None
        return   item.data
    
    def push(self,data):
        newNone = SingleNode(data)
        self.changeLength('+')
        if(self.head == None):
            self.head = newNone
            return True

        item = self.getLast()
        item.tail =  newNone
        
        return True
        

    def pop(self):
        if(self.head == None):
           return None
        elif(self.head.tail == None):
           data = self.head.data
           self.head = None
           return data

        item = self.head
        prev = None
        while(item.tail != None):
            prev = item
            item = item.tail
        prev.tail = None
        self.changeLength('-')
        return item.data
            
    
    def splice(self,index):
        if(index >= self.length or self.head == None):
            return None
        self.changeLength('-')
        item = self.head
        prev = self.head.tail
        for x in range(index):
            prev = item
            item = item.tail

        if(prev == None and item.tail == None):
            data = self.head.data
            self.head = None
            return data
        
        prev.tail = item.tail
        item.tail = None
        return item.data

        
    
    def insert(self,index, value):
        if(index >= self.length or self.head == None):
            return False
        newNode = SingleNode(value)
        self.changeLength('+')
        if(index == 0):
            newNode.tail = self.head
            self.head = newNode
            return True
        
        item = self.head
        prev = None
        for x in range(index):
            prev = item
            item = item.tail
        
        prev.tail = newNode
        newNode.tail = item
        return True


class DoubleLinkedList(LinkedList):


    def get(self,index):
        item = self.getNode(index)
        if(item == None):
            return None
        return   item.data
    
    def push(self,data):
        newNone = DoubleNode(data)
        self.changeLength('+')
        if(self.head == None):
            self.head = newNone
            return True

        item = self.getLast()
        item.tail =  newNone
        newNone.head = item
        return True
        

    def pop(self):
        if(self.head == None):
           return None
        elif(self.head.tail == None):
           data = self.head.data
           self.head = None
           return data

        item = self.head
        while(item.tail != None):
            item = item.tail

        item.head.tail = None
        self.changeLength('-')
        return item.data
            
    
    def splice(self,index):
        if(index >= self.length or self.head == None):
            return None
        self.changeLength('-')
        item = self.head
        for x in range(index):
            item = item.tail

        if(item.head == None and item.tail == None):
            data = self.head.data
            self.head = None
            return data
        
        item.head.tail = item.tail
        if(item.tail != None):
            item.tail.head = item.head
        return item.data

        
    
    def insert(self,index, value):
        if(index >= self.length or self.head == None):
            return False
        newNode = DoubleNode(value)
        self.changeLength('+')
        if(index == 0):
            newNode.tail = self.head
            self.head.head = newNode
            self.head = newNode
            return True
        
        item = self.head
        for x in range(index):
            item = item.tail
        
        item.head.tail = newNode
        item.head = newNode
        newNode.tail = item
        return True

    
    


    
        
    
test = DoubleLinkedList()
test.push("a")
test.push("b")
test.push("c")

print(test.length)
print(test.get(2))
print(test.pop())

print(test.length)

print(test.splice(1))
print(test.splice(0))
print(test.get(0))
print(test.get(1))
print(test.length)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
print(test.length)
test.push("a")
test.push("b")
test.push("c")
print(test.insert(0,'d'))
print(test.insert(1,'e'))
print(test.insert(4,'f'))
print(test.insert(99,'f'))
print(test.get(0))
print(test.get(1))

print('====== Printing list items =====')

item = test.head
while(item != None):
    print(item.data)
    item = item.tail





# def reverseStr(strValue):
#     # return str[::-1]
#     if(not type(strValue) is str):
#         return ""
    
#     length = len(strValue)
#     if(length <2):
#         return strValue

#     strArray = list(strValue)
#     for x in range(int(length/2)):
#         a = strArray[x]
#         strArray[x] = strArray[(length - 1) - x]
#         strArray[(length - 1) - x] = a
#     return ''.join(strArray)

# # print(reverseStr("Test"))


# def mergeSortedArray(arr1, arr2):
#     finalArr = []
#     while(True):

#         try:
#             v1 = arr1[0]
#         except IndexError:
#             return finalArr + arr2

#         try:
#             v2 =arr2[0]
#         except IndexError:
#             return finalArr + arr1
        
#         if( v1> v2):
#             finalArr.append(arr2.pop(0))
#         else:
#             finalArr.append(arr1.pop(0))

# print(mergeSortedArray([-5,0,3,4], [-19,4,6,30]))
                







        
    





