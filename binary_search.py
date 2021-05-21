# NC105，带重复元素的二分查找，返回第一个出现位置，分治
def find(arr, num):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == num else -1
    length = len(arr)
    arr1,arr2 = arr[:int(length/2)], arr[int(length/2):]
    in_arr1 = arr1[0] <= num <= arr1[-1]
    in_arr2 = arr2[0] <= num <= arr2[-1]
    if in_arr1:
        return find(arr1, num)
    elif in_arr2:
        return int(length/2) + find(arr2, num)
    else:
        return -1

if __name__ == '__main__':
    print(find([1,2,4,4,5],4))