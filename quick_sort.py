'''Ek pivot choose karo, usse chhote left side aur bade right side me bhejo.
Recursively left aur right sort karo.'''

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if(low<high):
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

arr = [5,2,8,11,0,2]
quick_sort(arr,0,5)
print(arr)

'''Time Complexity:
Average: O(n log n)
Worst: O(n²) (agar pivot galat choose ho jaye, e.g., already sorted array me last element)
Space Complexity: O(log n) (recursive stack)'''