# NC91 最长递增子序列，较难题，贪心+二分，贪心策略不容易想到
def search(vec, num):
    length = len(vec)
    if length == 1:
        return 0
    vec1, vec2 = vec[:int(length/2)], vec[int(length/2):]
    if num < vec1[-1]:
        return search(vec1, num)
    elif vec1[-1] < num < vec2[0]:
        return int(length/2)
    else:
        return int(length/2) + search(vec2, num)

def LIS(arr):
    vec = []
    max_count = []
    for i in range(len(arr)):
        if i == 0:
            vec.append(arr[i])
            max_count.append(1)
        else:
            if arr[i] > vec[-1]:
                vec.append(arr[i])
                max_count.append(len(vec))
            else:
                j = search(vec, arr[i])
                vec[j] = arr[i]
                max_count.append(j+1)
    temp = len(vec)
    result = []
    for i in range(len(max_count)-1,-1,-1):
        if max_count[i] == temp:
            result = [arr[i]] + result
            temp -= 1
    return result

if __name__ == '__main__':
    print(LIS([2,1,5,3,6,4,8,9,7]))
