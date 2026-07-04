# Har pass me adjacent elements compare karo aur bade wale ko right side bhejo.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [5,2,8,11,0,2]
print(bubble_sort(arr))

'''
Time Complexity: O(n²)
Space Complexity: O(1)
Best Case (already sorted): O(n)
'''