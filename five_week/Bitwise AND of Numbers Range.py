"""
给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。

示例 1：

输入：left = 5, right = 7
输出：4
示例 2：

输入：left = 0, right = 0
输出：0
示例 3：

输入：left = 1, right = 2147483647
输出：0
"""


class Solution:
    def __init__(self):
        self.left = 5
        self.right = 7

    def rangeBitwiseAnd(self):
        left = self.left
        right = self.right
        # 算法部分
        shift = 0

        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
