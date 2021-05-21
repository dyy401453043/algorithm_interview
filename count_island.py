# 牛客网NC109, 计算岛屿数量，dfs比bfs快不知道为什么
def count_island(grid):
    length, width = len(grid), len(grid[0])
    has_visited = [[False] * width for i in range(length)]
    count_result = 0

    def legal(i, j):
        return i < length and i >= 0 and j < width and j >= 0

    def bfs(i, j):
        queue = []
        queue.append((i, j))
        while len(queue) > 0:
            (i, j), queue = queue[0], queue[1:]
            has_visited[i][j] = True
            for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if legal(i, j) and not has_visited[i][j] and grid[i][j] == 1:
                    queue.append((i, j))

    def dfs(i, j):
        has_visited[i][j] = True
        for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if legal(i, j) and not has_visited[i][j] and grid[i][j] == 1:
                dfs(i, j)

    for i in range(length):
        for j in range(width):
            if grid[i][j] == 1 and not has_visited[i][j]:
                count_result += 1
                dfs(i, j)
    return count_result

if __name__ == '__main__':
    print(count_island([[1, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1]]))