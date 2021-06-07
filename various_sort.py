# 冒泡，选择，插入，希尔，归并，快速，堆排序
def bubble_sort(arr):
    length = len(arr)
    j = length  # j不表示下标，表示当前长度
    while j >= 2:
        for i in range(j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        j -= 1


def select_sort(arr):
    length = len(arr)
    max_index = -1
    j = length - 1
    while j >= 1:
        for i in range(j + 1):
            if max_index == -1 or arr[i] > arr[max_index]:
                max_index = i
        if max_index != j:
            arr[max_index], arr[j] = arr[j], arr[max_index]
        max_index = -1
        j -= 1


def insect_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def shell_sort(arr):
    length = len(arr)
    gap = int(length / 2)
    while gap >= 1:
        for i in range(0, length, gap):
            j = i
            while j - gap >= 0 and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap = int(gap / 2)


def merge_sort(arr):  # 至少有一个元素
    if len(arr) == 1:
        return arr
    mid = int(len(arr) / 2)
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result += [arr1[i], arr2[j]]
            i += 1
            j += 1
    if i < len(arr1):
        result += arr1[i:]
    if j < len(arr2):
        result += arr2[j:]
    return result


def fast_sort(arr):
    def partition(arr):  # ensure len(arr) >= 1
        pivot = arr[0]
        i, j = 0, len(arr) - 1
        while i != j:
            while arr[j] >= pivot and i != j:
                j -= 1
            if i == j:
                break
            else:
                arr[i] = arr[j]
                i += 1
            while arr[i] <= pivot and i != j:
                i += 1
            if i == j:
                break
            else:
                arr[j] = arr[i]
                j -= 1
        assert i == j
        arr[i] = pivot
        return i

    if len(arr) <= 1:
        return arr
    mid = partition(arr)
    first = fast_sort(arr[:mid])
    last = fast_sort(arr[mid + 1:])
    return first + [arr[mid]] + last


def heap_sort(arr):
    length = len(arr)

    def heapfify(arr, n, i):  # 把i元素下沉，n是最后下标，n也参与
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l <= n and arr[l] > arr[largest]:
            largest = l
        if r <= n and arr[r] > arr[largest]:
            largest = r
        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapfify(arr, n, largest)

    for i in range(length - 1, -1, -1):
        heapfify(arr, length - 1, i)
    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapfify(arr, i - 1, 0)


if __name__ == '__main__':
    arr = [4, 3, -2, 7, 1, -10, -6, -4]
    heap_sort(arr)
    print(arr)
