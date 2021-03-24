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
def bubbles(arr):
    x=len(arr)-1
    for i in range(x):
        for j in range(x-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr=[1,9,2,8,3,7,4,6,5,98]
print(bubbles(arr))
print('Done')

