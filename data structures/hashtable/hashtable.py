


class HashTable:

    buckets = None
    size = None
    def __init__(self, size = 20) -> None:
        self.size = size
        self.buckets = [[] for _ in range(size)] 


    def __hash(self,key) -> str: 
        keyChars = [*key]
        hash = 0

        for char in keyChars:
            hash += abs(ord(char)) % self.size
        return hash
    

    def set(self, key, value):
        hash = self.__hash(key)
        print('Hash: ',hash)
        self.buckets[hash].append([key,value])

    def get(self, key):
        hash = self.__hash(key)
        if(len(self.buckets[hash]) > 0):
            for pair in self.buckets[hash]:
                if(pair[0] == key):
                    return pair[1]
        return None
        
    
    def delete(self, key):
        hash = self.__hash(key)
        bucketLen = len(self.buckets[hash])
        if( bucketLen> 0):
            for i in range(bucketLen):
                pair = self.buckets[hash][i]
                if(pair[0] == key):
                    del self.buckets[hash][i]
                    break
    
    def keys(self):
        keys = []
        for bucket in self.buckets:
            keys += [x[0] for x in bucket]        
        return keys
    
    def values(self):
        values = []
        for bucket in self.buckets:
            values += [x[1] for x in bucket]        
        return values

    

# test = HashTable(2)

# test.set('a', 'apple')
# print(test.get('a'))
# test.delete('a')

# print(test.get('a'))
# test.set('b','ball')
# test.set('c', 'cat')

# print(len(test.buckets))

# for bucket in test.buckets:
#     print(bucket)

# print(test.keys())
# print(test.values())
    

def firstRecurringCharacter(arr):
    chrMap = {}

    for ele in arr:
        print(chrMap)
        if(chrMap.get(ele)):
           return ele
        chrMap[ele] = True
    return None


def firstRecurringCharacter2(arr):
    arrLen = len(arr)
    pairs = []
    for i in range(arrLen):
        for j in range(i+1,arrLen):
            if(arr[i] == arr[j]):
                pairs.append([i,j])
    print(pairs)
    if(len(pairs)> 0):
        pairs.sort(key=lambda a: a[1] - a[0])
        return arr[pairs[0][0]]
    return None

def firstRecurringCharacter3(arr):
    arrLen = len(arr)
    found = []
    for i in range(arrLen):
        if( arr[i] in found):
            return arr[i]
        found.append(arr[i])
    return None

print(firstRecurringCharacter3('abbadefghi'))
