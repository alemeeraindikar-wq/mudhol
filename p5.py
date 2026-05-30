import time
import matplotlib.pyplot as plt
def linearsearch (a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return i
        return -1
a=[13,14,20,25,50,100]
start=time.time()
print("the array elements are:",a)
key=int(input("enter the key elements to search:"))
result=linearsearch(a,key)
if (result==-1):
    print("search unsuccessful")
else:
    print("search successful at the location", result+1)
end=time.time()
print("run time is",end-start)
x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("linear search time complexity is O(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
