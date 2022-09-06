# leetcode 287, Floyd 判圈算法寻找重复数, 重复点入度为2出度为1故有环
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow == 0 or nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]
