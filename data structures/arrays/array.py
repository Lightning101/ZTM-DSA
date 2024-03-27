
class Node:
    first = None
    last = None
    data = None

    def __init__(self, data, first) -> None:
        self.data = data
        self.first = first
        

class MyArray:
    length = 0
    firstNode = None

    def __init__(self):
        pass


    def __getNode(self, index):
        item = self.firstNode
        for x in range(index):
            if(item.last == None):
                return None
            else:
                item = item.last
        return  item
    
    def __changeLength(self,op):
        if(op == '+'):
            self.length +=1
        else:
            self.length -=1

    def __getLast(self):
        if(self.firstNode == None):
            None
        else:
            lastNode = self.firstNode
            while( lastNode.last != None):
                lastNode = lastNode.last
            return lastNode
    def get(self,index):
        item = self.__getNode(index)
        if(item == None):
            return None
        return   item.data
    

    
    def push(self,data):
        self.__changeLength("+")
        if(self.firstNode == None):
            self.firstNode = Node(data, None)
        else:
            lastNode = self.__getLast()
            newItem = Node(data, lastNode)
            lastNode.last = newItem

    def pop(self):
        lastNode = self.__getLast()
        if(lastNode != None):
            first = lastNode.first
            last = lastNode.last
            if(first == None and last == None):
                self.firstNode = None
            elif(first != None and last == None):
                first.last = None
            elif(first == None and last != None):
                self.firstNode = lastNode.last
            self.__changeLength("-")
            return lastNode.data
            
        else:
            return None
    
    def splice(self,index):
        item = self.__getNode(index)
        if(item == None):
            return None
        
        first = item.first
        last = item.last
        if(first == None and last == None):
            self.firstNode = None
        elif(first != None and last == None):
            first.last = None
        elif(first == None and last != None):
            self.firstNode = item.last
        else:
            first.last = last
            last.first = first
        
        self.__changeLength("-")
        return item.data
        
    
# test = MyArray()
# test.push("a")
# test.push("b")
# test.push("c")

# print(test.length)
# print(test.get(2))
# test.pop()

# print(test.length)

# print(test.splice(1))
# print(test.splice(0))
# print(test.get(0))
# print(test.get(1))
# print(test.length)
# print(test.pop())
# print(test.pop())
# print(test.pop())
# print(test.pop())
# print(test.length)


def reverseStr(strValue):
    # return str[::-1]
    if(not type(strValue) is str):
        return ""
    
    length = len(strValue)
    if(length <2):
        return strValue

    strArray = list(strValue)
    for x in range(int(length/2)):
        a = strArray[x]
        strArray[x] = strArray[(length - 1) - x]
        strArray[(length - 1) - x] = a
    return ''.join(strArray)

# print(reverseStr("Test"))


def mergeSortedArray(arr1, arr2):
    finalArr = []
    while(True):

        try:
            v1 = arr1[0]
        except IndexError:
            return finalArr + arr2

        try:
            v2 =arr2[0]
        except IndexError:
            return finalArr + arr1
        
        if( v1> v2):
            finalArr.append(arr2.pop(0))
        else:
            finalArr.append(arr1.pop(0))

print(mergeSortedArray([-5,0,3,4], [-19,4,6,30]))
                







        
    





