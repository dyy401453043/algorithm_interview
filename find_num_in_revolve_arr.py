# 牛客网N48 在有旋转点的数组中找到target的索引，不存在为-1，二分分治法
def binary_search(arr,num):
    length = len(arr)
    if length == 0:
        return -1
    if length == 1:
        return -1 if arr[0] != num else 0
    arr1,mid,arr2 = arr[:int(length/2)],arr[int(length/2)],arr[int(length/2)+1:]
    if mid == num:
        return int(length/2)
    elif mid > num:
        return binary_search(arr1,num)
    else:
        index = binary_search(arr2,num)
        return -1 if index == -1 else int(length/2)+1+index

def find(arr, num):
    length = len(arr)
    if length == 1:
        return -1 if arr[0] != num else 0
    arr1,arr2 = arr[:int(length/2)],arr[int(length/2):]
    if arr1[0] <= arr1[-1] and arr2[0] <= arr2[-1]:
        if arr1[0]<=num<=arr1[-1]:
            return binary_search(arr1,num)
        elif arr2[0]<=num<=arr2[-1]:
            index = binary_search(arr2,num)
            return -1 if index == -1 else int(length/2) + index
        else:
            return -1
    elif arr1[0] <= arr1[-1]:
        if arr1[0]<=num<=arr1[-1]:
            return binary_search(arr1,num)
        else:
            index = find(arr2,num)
            return -1 if index == -1 else int(length/2) + index
    else:
        if arr2[0]<=num<=arr2[-1]:
            index = binary_search(arr2,num)
            return -1 if index == -1 else int(length/2) + index
        else:
            return find(arr1, num)