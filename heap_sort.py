# 动手实现堆排序
def heapfify(arr,n,i): # 把i位置元素沉到该沉的位置
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapfify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    # 建堆
    for i in range(n-1,-1,-1):
        heapfify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapfify(arr,i,0)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)