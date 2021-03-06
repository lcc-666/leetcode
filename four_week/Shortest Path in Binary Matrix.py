"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

示例 1：


输入：grid = [[0,1],[1,0]]
输出：2
示例 2：


输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4
示例 3：

输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1
"""


class Solution:
    def __init__(self):
        self.grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

    def shortestPathBinaryMatrix(self):
        grid = self.grid
        # 算法部分
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1] != 0:
            return -1
        if n == 1:
            return 1

        start = 1
        dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        x1 = 0
        x2 = 0
        que = [[x1, x2]]
        while que:
            m = len(que)
            while m:
                m -= 1
                x, y = que.pop(0)
                if x == n - 1 and y == n - 1:
                    return start
                for dx, dy in dxy:
                    x1 = x + dx
                    x2 = y + dy
                    if 0 <= x1 < n and 0 <= x2 < n and grid[x1][x2] == 0:
                        grid[x1][x2] = 1
                        que.append([x1, x2])
            start += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    p = s.shortestPathBinaryMatrix()
    print(p)
