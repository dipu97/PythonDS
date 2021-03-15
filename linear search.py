def linearSearch(arr,element):
    for item in range(len(arr)):
        if element==arr[item]:
            return item
    return -1
arr=[1,45,3,5,78,34,99]
element=78
res=linearSearch(arr,element)
if res==-1:
    print('Item Not found')
else:
    print(res)