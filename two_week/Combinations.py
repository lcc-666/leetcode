""""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]
"""


class Solution:
    def __init__(self):
        self.n = 4
        self.k = 2

    def combine(self):
        n = self.n
        k = self.k
        # 算法逻辑
        result = []
        path = []
        def backtrack(n, k, index):
            if len(path) == k:
                result.append(path[:])
                print(result)
                return
            for i in range(index, n+1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return result


if __name__ == '__main__':
    t = Solution()
    s = t.combine()
    print(s)
