# leetcode 39，找到数组中和为target的解，不定长且有放回，大空间dfs。
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        results = []
        candidates.sort()
        def dfs(sub_target, temp_result, idx):
            if sub_target < 0 or idx == len(candidates):
                return
            elif sub_target == 0:
                results.append(temp_result)
            else:
                if sub_target < candidates[idx]:
                    return
                else:
                    dfs(sub_target, temp_result, idx+1)
                    dfs(sub_target-candidates[idx], temp_result+[candidates[idx]], idx)
        dfs(target, [], 0)
        return results
