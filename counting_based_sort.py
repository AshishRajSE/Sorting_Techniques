def cyclic_sort(arr):
    n = len(arr)
    result = [0]*n

    for i in range(n):
        count = 0
        for j in range(n):
            if(arr[j]<arr[i]):
                count+=1
        
        while(result[count]!=0):   # for same digits
            count+=1
            
        result[count] = arr[i]

    return (result)

arr = [5,2,8,11,0,2]
print(cyclic_sort(arr))