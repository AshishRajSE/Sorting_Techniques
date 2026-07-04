# minimum element dhoondo aur usse sahi jagah pe swap karo.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        low = i
        for j in range(i,n):
            if(arr[j]<arr[low]):
                low = j
        arr[low], arr[i] = arr[i], arr[low]
    return arr
arr = [5,2,8,11,0,2]
print(selection_sort(arr))

# Method 2

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if(arr[j]<arr[i]):
                arr[j], arr[i] = arr[i], arr[j]
    return arr
arr = [5,2,8,11,0,2]
print(selection_sort(arr))

'''
Time Complexity: O(n²)
Space Complexity: O(1)
Best/Worst Case: Hamesha O(n²)'''