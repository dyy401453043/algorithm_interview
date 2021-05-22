# leetcode 394 字符串解码, 栈式解析

def decodeString(s: str) -> str: #答案
    stack = []  # (str, int) 记录左括号之前的字符串和左括号外的上一个数字
    num = 0
    res = ""  # 实时记录当前可以提取出来的字符串
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((res, num))
            res, num = "", 0
        elif c == "]":
            top = stack.pop()
            res = top[0] + res * top[1]
        else:
            res += c
    return res

def decode_string(s):
    num_stack = []
    str_stack = []
    num, res = '', ''
    for i in s:
        if '0'<=i<='9':
            num += i
        elif 'a'<=i<='z':
            res += i
        elif i == '[':
            num_stack,num = num_stack+[int(num)],'0'
            str_stack,res = str_stack+[res],''
        else:
            temp_num = num_stack.pop()
            res = str_stack.pop() + res*temp_num
    return res

if __name__ == '__main__':
    s = "2[2[y]pq4[2[jk]e]]"
    print(decodeString(s))
    print(decode_string((s)))
    pass
