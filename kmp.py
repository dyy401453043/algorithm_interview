# kmp算法，1.next数组获取 2.主逻辑
def get_next(string):
    next = [-1] * len(string)
    j,k=0,-1
    while j < len(string)-1:
        if k<0 or string[k]==string[j]:
            k+=1
            j+=1
            next[j] = k
        else:
            k = next[k]
    return next

def kmp(source,target):
    i,j = 0,0
    next = get_next(target)
    while i < len(source) and j < len(target):
        if source[i] == target[j]:
            i+=1
            j+=1
        else:
            j=next[j]
            if j == -1:
                i+=1
                j+=1
    if j == len(target):
        return i - j
    else:
        return -1

if __name__ == '__main__':
    print(get_next('ABAD'))
    print(kmp('ABACABADE','ABAD'))

