#NC1 大数加法
def add(str1, str2):
    num_array = [0] * 100001
    str1, str2 = (str1, str2) if len(str1) > len(str2) else (str2, str1)
    str1, str2 = str1.strip(), str2.strip()
    list1, list2 = list(map(int, list(str1))), list(map(int, list(str2)))
    list1.reverse()
    list2.reverse()
    max_scope = len(list1) - 1
    for i in range(len(list1)):
        j = i
        num1 = list1[i]
        num2 = list2[j] if j < len(list2) else 0
        num_array[i] = num1 + num2
    for i in range(len(list1)):
        if num_array[i] >= 10:
            num_array[i] -= 10
            num_array[i + 1] += 1
            if i + 1 == len(list1):
                max_scope = i + 1
    num_array = num_array[:max_scope + 1]
    num_array.reverse()
    str_result = ''.join(list(map(str, num_array)))
    return str_result

if __name__ == '__main__':
    result = add('1','99')
    pass
