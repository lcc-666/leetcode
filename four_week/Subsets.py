"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    def __init__(self):
        self.nums = [1, 2, 3]

    def subsets(self):
        nums = self.nums
        # 算法部分
        result = []

        def backtrack(start, k, cur, nums):
            if k == 0:
                result.append(cur[:])
                return
            for i in range(start, n):
                cur.append(nums[i])
                backtrack(i + 1, k - 1, cur, nums)
                cur.pop()

        n = len(nums)
        for k in range(n + 1):
            backtrack(0, k, [], nums)
        return result


if __name__ == '__main__':
    s = Solution()
    t = s.subsets()
    print(t)
