class BinarySearch():
    def binary_search(self,arr, element):
        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = (low + high) // 2

            if arr[mid] == element:
                return mid
            elif arr[mid] > element:
                high = mid - 1
            else:
                low = mid + 1

        return -1
arr=[12,23,24,27,34,45,48,98,90]
element=34
b=BinarySearch()
result=b.binary_search(arr,element)
print(result)
print(arr[result])