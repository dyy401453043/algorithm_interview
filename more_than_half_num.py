# 牛客网N73, 找到数组中出现次数超过一半的元素, 要求空间复杂度为O(1),曹操
def MoreThanHalfNum_Solution(numbers):
    most_num = None
    res = 0
    for num in numbers:
        if (res == 0):
            most_num = num
            res += 1
        else:
            if num == most_num:
                res += 1
            else:
                res -= 1
    return most_num