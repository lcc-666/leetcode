"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""


class Solution:
    def __init__(self):
        self.n = 44

    def climbStairs(self):
        n = self.n
        # 算法部分
        if n == 1:
            return 1
        if n == 2:
            return 2
        d1 = 1
        d2 = 2
        sum = 0
        for i in range(3, n + 1):
            sum = d1 + d2
            d1 = d2
            d2 = sum
        return d2


if __name__ == '__main__':
    t = Solution()
    s = t.climbStairs()
    print(s)
