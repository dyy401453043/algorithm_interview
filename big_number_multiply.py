# leet_code 43, 字符串大数字乘法，找规律很重要 num1[i]*num[j]会出现在result[i+j]和result[i+j+1]中！

def reverse(string):
    reverse = ''
    for s in string:
        reverse = s + reverse
    return reverse

def multiply(num1: str, num2: str):
    if num1 == '0' or num2 == '0':
        return '0'
    max_scoop = 0
    result = [0] * 15000
    len1 = len(num1)
    len2 = len(num2)
    num1 = reverse(num1)
    num2 = reverse(num2)
    index_sum_max = len1 + len2 - 2
    for index_sum in range(index_sum_max + 1):
        for i in range(min(index_sum+1,len1)):
            j = index_sum - i
            if j >= len2:
                continue
            i_m_j = reverse(str(int(num1[i])*int(num2[j])))
            k = index_sum
            result[k] += int(i_m_j[0])
            max_scoop = k if k > max_scoop else max_scoop
            while result[k] >= 10:
                result[k] -= 10
                k+=1
                result[k] += 1
                max_scoop = k if k > max_scoop else max_scoop
                k+=1
            if len(i_m_j) > 1:
                k = index_sum+1
                result[k] += int(i_m_j[1])
                max_scoop = k if k > max_scoop else max_scoop
            while result[k] >= 10:
                result[k] -= 10
                k+=1
                result[k] += 1
                max_scoop = k if k > max_scoop else max_scoop
    return result[:max_scoop+1]

if __name__ == '__main__':
    result = multiply('9999','9999')
    sum_reverse = ''.join([str(i) for i in result])
    sum = reverse(sum_reverse)
    pass