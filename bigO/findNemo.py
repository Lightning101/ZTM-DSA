import cProfile


nemo = ["Nemo"]
everyone = ["Nemo" for element in range(100000)]


def findNemo(arr, find):  # O(n)
    print("Running")
    for name in arr:
        if name in find:
            print("Found Nemo")
            break


# cProfile.run('findNemo(nemo,"Nemo")')
cProfile.run('findNemo(everyone,"nemo")')


boxs = [element for element in range(100000)]


def logFirstBox(arr):
    print(arr[0])


def logTwoBox(arr):
    print(arr[0])
    print(arr[1])


cProfile.run("logFirstBox(boxs)")
cProfile.run("logTwoBox(boxs)")

# Spatial complexity.
def boooo(n):
    for i in range(len(n)):
        print("booooo")


def arrayOfHiNTimes(n):
    hiArray = []
    for i in range(len(n)):
        hiArray[i] = "hi"
    return hiArray


arrayOfHiNTimes(6)
