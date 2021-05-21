# NC101 简单题，注意特例
def find(arr):
    if len(arr) == 0:
        return 0
    if arr[-1] - arr[0] == len(arr) - 1:
        return 0 if arr[0] != 0 else arr[-1]+1
    length = len(arr)
    if length == 2:
        if arr[-1] - arr[0] != length - 1:
            return int((arr[0]+arr[-1])/2)
    else:
        arr1, arr2 = arr[:int(length/2)], arr[int(length/2):]
        if arr2[-1] - arr2[0] != len(arr2) - 1:
            return find(arr2)
        elif arr1[-1] - arr1[0] != len(arr2) - 1:
            return find(arr1)
        else:
            return int((arr2[0]+arr1[-1])/2)

if __name__ == '__main__':
    print(find([0,1,2,3,4,5,7,8]))