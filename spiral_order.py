# 牛客网NC38，螺旋矩阵，逻辑清楚就可以
def spiralOrder(matrix):
    m,n = len(matrix),len(matrix[0])
    def legal(i, j):
        return 0 <= i < m and 0 <= j < n
    visited = [[False] * n for i in range(m)]
    i, j = 0, 0
    result = []
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction, directions = directions[0], directions[1:] + [directions[0]]
    while True:
        result.append(matrix[i][j])
        visited[i][j] = True
        if legal(i + direction[0], j + direction[1]) and not visited[i + direction[0]][j + direction[1]]:
            i, j = i + direction[0], j + direction[1]
        else:
            direction, directions = directions[0], directions[1:] + [directions[0]]
            i, j = i + direction[0], j + direction[1]
            if legal(i,j) and not visited[i][j]:
                continue
            else:
                break
    return result

if __name__ == '__main__':
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))