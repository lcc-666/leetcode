""""
给定一个由 0 和 1 组成的矩阵 mat，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1

示例 1：
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]

示例 2：
输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
"""

import collections


class Solution:
    def __init__(self):
        self.mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

    def updateMatrix(self):
        mat = self.mat
        # 算法部分
        m = len(mat)
        n = len(mat[0])
        dist = [[0] * n for _ in range(m)]
        zero_list = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zero_list.append((i, j))
        q = collections.deque(zero_list)
        seen = set(zero_list)

        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return dist


if __name__ == '__main__':
    t = Solution()
    t.updateMatrix()

