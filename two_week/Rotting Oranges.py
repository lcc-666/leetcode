"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

示例 1：
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4

示例 2：
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

示例 3：
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
"""

import collections


class Solution:
    def __init__(self):
        self.grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    def orangesRotting(self):
        grid = self.grid
        # 算法部分
        m = len(grid)
        n = len(grid[0])
        bad_list = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bad_list.append((i, j))
        q = collections.deque(bad_list)
        time = 0

        def good_bag(q):
            ls = []
            while q:
                i, j = q.popleft()
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        ls.append((ni, nj))
            q = collections.deque(ls)
            return q

        while q:
            q = good_bag(q)
            time += 1
        if time > 0:
            time -= 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time


if __name__ == '__main__':
    t = Solution()
    s = t.orangesRotting()
    print(s)
