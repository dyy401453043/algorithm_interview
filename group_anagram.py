class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dist = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char)-ord('a')] += 1
            count = tuple(count) # list和dict不可哈希，但是tuple可以
            result_dist[count] = result_dist[count] + [str] if count in result_dist else [str]
        return list(result_dist.values())
