# leetcode 46 全排列，dfs，自己的写法和题解的写法
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     result = []
    #     def dfs(temp_in, temp_out):
    #         if len(temp_out) == 0:
    #             result.append(temp_in)
    #             return
    #         else:
    #             for i,num in enumerate(temp_out):
    #                 dfs(temp_in+[num], temp_out[:i]+temp_out[i+1:])
    #     dfs([],nums)
    #     return result
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def dfs(i):
            if i == n:
                result.append(nums[:])# 切片浅拷贝创建新的对象
                return
            else:
                for j in range(i,n):
                    nums[i],nums[j] = nums[j],nums[i]
                    dfs(i+1)
                    nums[i],nums[j] = nums[j],nums[i]
        dfs(0)
        return result