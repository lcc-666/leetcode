"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    def __init__(self):
        self.nums = [4,4,4,1,4]

    def subsetsWithDup(self):
        nums = self.nums
        # 算法部分
        nums.sort()
        result = []

        def backtrack(start, k, cur, nums):
            if k == 0:
                if cur not in result:
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
    t = s.subsetsWithDup()
    print(t)


