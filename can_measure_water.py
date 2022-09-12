# leetcode 365，水壶问题，两个水壶构造出指定的水量dfs，自己维护栈
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            if node[0] == targetCapacity or node[1] == targetCapacity or node[0] + node[1] == targetCapacity:
                return True
            seen.add(node)
            stack.append((jug1Capacity, node[1]))
            stack.append((node[0], jug2Capacity))
            stack.append((0, node[1]))
            stack.append((node[0], 0))
            stack.append((min(node[0]+node[1],jug1Capacity), max(node[1]+node[0]-jug1Capacity, 0)))
            stack.append((max(node[1]+node[0]-jug2Capacity,0), min(node[0]+node[1],jug2Capacity)))
        return False
