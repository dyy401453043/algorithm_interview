# leetcode 164, 基数排序
def exp_sort(nums):
    exp = 1
    length = len(nums)
    buf = [0] * length
    max_val = max(nums)
    while max_val >= exp:
        cnt = [0] * 10
        for i in range(length):
            dight = int((nums[i] / exp) % 10)
            cnt[dight] += 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i - 1]
        print(cnt)
        for i in range(length - 1, -1, -1):
            digit = int((nums[i] / exp) % 10)
            buf[cnt[digit] - 1] = nums[i]
            cnt[digit] -= 1
        nums = [i for i in buf]
        exp *= 10
    return nums
