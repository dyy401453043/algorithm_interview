# leetcode 85, 01矩阵中内嵌的最大矩形，与直方图内嵌最大矩形解法类似
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def rectangle_area_stack(arr):
            right_border = [i for i in range(len(arr))]
            left_border = [i for i in range(len(arr))]
            stack = []
            for i in range(len(arr)):
                if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
                    left_border[i] = stack[-1] if len(stack) != 0 else -1
                    stack.append(i)
                else:
                    while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                        element = stack.pop()
                        right_border[element] = i
                    left_border[i] = stack[-1] if len(stack) != 0 else -1
                    stack.append(i)
            for element in stack:
                right_border[element] = len(arr)
            area = 0
            for i in range(len(arr)):
                temp_area = arr[i] * (right_border[i]-left_border[i]-1)
                if temp_area > area:
                    area = temp_area
            return area

        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        left_length = [[0] * n for i in range(m)]
        for i in range(m):
            count = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    count += 1
                else:
                    count = 0
                left_length[i][j] = count
        area = 0
        for j in range(n):
            temp_area = rectangle_area_stack([left_length[i][j] for i in range(m)])
            if temp_area > area:
                area = temp_area
        return area
