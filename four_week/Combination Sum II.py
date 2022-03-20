"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

"""


class Solution:
    def __init__(self):
        self.candidates = [10, 1, 2, 7, 6, 1, 5]
        self.target = 8

    def combinationSum2(self):
        candidates = self.candidates
        target = self.target
        # 算法部分
        res = []
        path = []

        def backtrack(candidates, target, sum, begin):
            if sum == target:
                res.append(path[:])

            for i in range(begin, len(candidates)):
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                rs = candidates[i] + sum
                if rs <= target:
                    path.append(candidates[i])
                    backtrack(candidates, target, rs, i + 1)
                    path.pop()
                else:
                    break

        candidates.sort()
        backtrack(candidates, target, 0, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    t = s.combinationSum2()
    print(t)
