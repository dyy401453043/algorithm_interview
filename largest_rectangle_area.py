# leetcode 84,直方图中的最大矩形面积，（双指针+分治）或者单调栈，单调栈除了可以求右侧第一个小还可以同时求左侧第一个小于等于
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def area_across_k(arr, k):
            left,right = k-1,k+1
            best_area = arr[k]
            min_bar = arr[k]
            while left >= 0 or right <= len(arr)-1: # 循环前 right, left 还没被探索
                left_value = arr[left] if left >= 0 else 0
                right_value = arr[right] if right <= len(arr)-1 else 0
                if left_value > right_value:
                    min_bar = min(min_bar, left_value)
                    temp_area = min_bar * (right - left)
                    if temp_area > best_area:
                        best_area = temp_area
                    left -= 1
                elif left_value < right_value:
                    min_bar = min(min_bar, right_value)
                    temp_area = min_bar * (right - left)
                    if temp_area > best_area:
                        best_area = temp_area
                    right += 1
                else:
                    min_bar = min(min_bar, left_value)
                    temp_area = min_bar * (right - left + 1)
                    if temp_area > best_area:
                        best_area = temp_area
                    left -= 1
                    right += 1
            return best_area

        def rectangle_area(arr):
            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]
            mid = int(len(arr)/2)
            return max(area_across_k(arr,mid), rectangle_area(arr[:mid]), rectangle_area(arr[mid+1:]))
        
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
            # stack = []
            # for i in range(len(arr)-1,-1,-1):
            #     if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
            #         stack.append(i)
            #     else:
            #         while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            #             element = stack.pop()
            #             left_border[element] = i
            #         stack.append(i)
            # for element in stack:
            #     left_border[element] = -1
            area = 0
            print(right_border, left_border)
            for i in range(len(arr)):
                temp_area = arr[i] * (right_border[i]-left_border[i]-1)
                if temp_area > area:
                    area = temp_area
            return area
        
        return rectangle_area_stack(heights)
