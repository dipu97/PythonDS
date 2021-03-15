def bubbleSort(arr):
    for num in range(len(arr)-1,0,-1):
        for i in range(num):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

arr = [9,8,6,7,1,4,5,32,45,3,4,555,3,2,3,2,1]
bubbleSort(arr)
print(arr)