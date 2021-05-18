# 牛客网NC119，找无序数组中最小的k个数
def part(arr):
    i,j = 0,len(arr)-1
    partition = arr[0]
    while i != j:
        while arr[j] >= partition and j > i:
            j -= 1
        if j == i:
            break
        else:
            arr[i] = arr[j]
            i += 1
        while arr[i] <= partition and i < j:
            i += 1
        if i == j:
            break
        else:
            arr[j] = arr[i]
            j -= 1
    assert i==j
    arr[i] = partition
    return i

def find_k(arr,k):
    if k > len(arr):
        return []
    i = part(arr)
    if i+1 == k:
        return arr[:i+1]
    elif i+1 < k:
        return arr[:i+1] + find_k(arr[i+1:],k-i-1)
    else:
        return find_k(arr[:i],k)

if __name__ == '__main__':
    arr = [4,5,1,6,2,7,3,8]
    k = 4
    result = find_k(arr, k)
    pass