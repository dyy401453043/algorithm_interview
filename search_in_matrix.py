# leetcode 剑指offer 04，二维矩阵查找问题，思路有点难想
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        n,m = len(matrix),len(matrix[0]) # 起点为右上角或左下角，方便移动指针
        i,j = 0,m-1
        while i < n and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False
