import cProfile


# nemo = ["Nemo"]
# everyone = ["Nemo" for element in range(100000)]


# def findNemo(arr, find):  # O(n)
#     print("Running")
#     for name in arr:
#         if name in find:
#             print("Found Nemo")
#             break


# # cProfile.run('findNemo(nemo,"Nemo")')
# cProfile.run('findNemo(everyone,"nemo")')


# boxs = [element for element in range(100000)]


# def logFirstBox(arr):
#     print(arr[0])


# def logTwoBox(arr):
#     print(arr[0])
#     print(arr[1])


# cProfile.run("logFirstBox(boxs)")
# cProfile.run("logTwoBox(boxs)")

# # Spatial complexity.
# def boooo(n):
#     for i in range(len(n)):
#         print("booooo")


# def arrayOfHiNTimes(n):
#     hiArray = []
#     for i in range(len(n)):
#         hiArray[i] = "hi"
#     return hiArray


# arrayOfHiNTimes(6)

def containsCommonElement(arr1, arr2) -> bool:
    for v1 in arr1:
        for v2 in arr2:
            if(v1 == v2):
                return True
    return False

def containsCommonElementV2(arr1, arr2) -> bool:
    joinedStr = ''.join(arr2)
    for v1 in arr1:
        if v1.lower() in joinedStr.lower():
            return True
    return False

def containsCommonElementV3(arr1, arr2) -> bool:
    obj = {}
    targetArr = None
    if(arr1> arr2):
        for val in arr2:
            obj[val] = True
        targetArr = arr1
    else:
        for val in arr1:
            obj[val] = True 
        targetArr = arr2
    
    for key in targetArr:
        if  key in obj:
            return True
    return False

arr1 = ['a','b','c','d']
arr2 = ['e','f','g','h']
arr3 = ['e','f','g','h','d']


# cProfile.run("logFirstBox(boxs)")
# print(containsCommonElement(arr1, arr2))
# print(containsCommonElement(arr1, arr3))
# print(containsCommonElementV2(arr1, arr2))
# print(containsCommonElementV2(arr1, arr3))
# print(containsCommonElementV3(arr1, arr2))
# print(containsCommonElementV3(arr1, arr3))

cProfile.run("containsCommonElement(arr1, arr2)")
cProfile.run("containsCommonElement(arr1, arr3)")
cProfile.run("containsCommonElementV2(arr1, arr2)")
cProfile.run("containsCommonElementV2(arr1, arr3)")
cProfile.run("containsCommonElementV3(arr1, arr2)")
cProfile.run("containsCommonElementV3(arr1, arr3)")


