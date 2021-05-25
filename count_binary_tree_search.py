# leetcode96 给定节点数量，不同的二叉搜索树计数，动态规划（递归思路）
class Solution:
    def numTrees(self, n: int) -> int:
        # F(1) = 1
        # F(2) = F(1) + F(1)
        # F(3) = F(2) + F(1)*F(1) + F(2)
        # F(4) = F(3) + F(1)*F(2) + F(2)*F(1) + F(3)
        F = [0]*(n+1)
        for i in range(n+1):
            if i==0 or i==1:
                F[i] = 1
            else:
                for j in range(i):
                    F[i] += F[j]*F[i-1-j]
        return F[n]