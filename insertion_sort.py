# Har element ko uthao aur usse pehle ke sorted part me sahi jagah insert karo.

def insetion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [5,2,8,11,0,2]
print(insetion_sort(arr))    

'''Time Complexity: O(n²)
Space Complexity: O(1)
Best Case (already sorted): O(n)'''