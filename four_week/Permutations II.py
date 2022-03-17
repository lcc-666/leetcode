"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def __init__(self):
        self.nums = [1, 1, 2]

    def permuteUnique(self):
        nums = self.nums
        # 算法逻辑
        result = []
        lens = len(nums)
        used = [0] * lens
        if lens == 0:
            return []
        depth = 0
        path = []

        def dfs(nums, lens, depth, used, path):
            if depth == lens and path[:] not in result:
                result.append(path[:])
                return
            for i in range(lens):
                if used[i] == 1:
                    continue
                path.append(nums[i])
                used[i] = 1
                dfs(nums, lens, depth + 1, used, path)
                path.pop()
                used[i] = 0

        dfs(nums, lens, depth, used, path)
        return result
if __name__ == '__main__':
    s=Solution()
    t=s.permuteUnique()
    print(t)