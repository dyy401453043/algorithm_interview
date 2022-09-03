# leetcode 202, 找区间范围内接近的元素，滑动窗口 & （二分查找 or 分桶查找）
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # length = len(nums)
        # if length == 1 or k == 0:
        #     return False
        # window_size = k+1
        # temp = nums[:min(window_size, length)]
        # temp = sorted(temp)

        # for i in range(min(window_size, length)-1):
        #     if abs(temp[i]-temp[i+1]) <= t:
        #         return True

        # def get_index(n, arr): # 返回 右边界
        #     l, r = 0, len(temp)-1
        #     if n > arr[r]:
        #         return r + 1
        #     while l != r:
        #         mid = (l + r) // 2
        #         if arr[mid] < n:
        #             l = mid + 1
        #         elif arr[mid] > n:
        #             r = mid
        #         else:
        #             return mid
        #     assert l == r
        #     return l
        
        # for i in range(length-window_size):
        #     node1, node2 = nums[i], nums[i+window_size]
        #     index1 = get_index(node1, temp)
        #     temp = temp[:index1] + temp[index1+1:]
        #     index2 = get_index(node2, temp)
        #     if index2 == 0:
        #         if abs(node2-temp[index2]) <= t:
        #             return True   
        #     elif index2 == window_size-1:
        #         if abs(node2-temp[index2-1]) <= t:
        #             return True 
        #     else:
        #         if abs(node2-temp[index2]) <= t or abs(node2-temp[index2-1]) <= t:
        #             return True
        #     temp = temp[:index2] + [node2] + temp[index2:]
        # return False

        def get_id(x):
            return x // t if t != 0 else x
        length = len(nums)
        if length == 1 or k == 0:
            return False
        window_size = k+1
        temp_dict = {}
        for i in range(min(window_size, length)):
            key = get_id(nums[i])
            if key in temp_dict or ((key+1) in temp_dict and abs(nums[i]-temp_dict[key+1]) <= t) or ((key-1) in temp_dict and abs(nums[i]-temp_dict[key-1]) <= t):
                return True
            else:
                temp_dict[key] = nums[i]
        for i in range(length-window_size):
            key1, key2 = get_id(nums[i]), get_id(nums[i+window_size])
            del temp_dict[key1]
            if key2 in temp_dict or ((key2+1) in temp_dict and abs(nums[i+window_size]-temp_dict[key2+1]) <= t) or ((key2-1) in temp_dict and abs(nums[i+window_size]-temp_dict[key2-1]) <= t):
                return True
            temp_dict[key2] = nums[i+window_size]
        return False
