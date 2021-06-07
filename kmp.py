# kmp算法，1.next数组获取 2.主逻辑
# A:ababdababcde
# B:ababcd
# B:  ababcd
# B:     ababcd

def get_next(string):
    length = len(string)
    k,i = -1,0
    next = [-1] * length
    while i < length-1:
        if k == -1 or string[k] == string[i]:
            k += 1
            i += 1
            next[i] = k
        else:
            k = next[k]
    return next

def find(A, B):
    next = get_next(B)
    length1,length2 = len(A),len(B)
    i,j=0,0
    while i < length1 and j < length2:
        if j == -1 or A[i] == B[j]:
            i+=1
            j+=1
        else:
            j = next[j]
    if j == length2:
        return i - length2
    else:
        return -1

if __name__ == '__main__':
    print(find("ababdababcde", "ababcd"))

