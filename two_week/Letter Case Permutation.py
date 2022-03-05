"""
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。

示例 1：
输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

示例 2:
输入: s = "3z4"
输出: ["3z4","3Z4"]
"""


class Solution:
    def __init__(self):
        self.s = "a1b2"

    def letterCasePermutation(self):
        s = self.s
        # 算法逻辑
        result = []
        n = len(s)
        if n == 0:
            return [""]
        start = 0

        def dfs(start, temp):
            if len(temp) == n:
                result.append(temp)
                return
            if s[start].isdigit():
                dfs(start + 1, temp + s[start])
            elif s[start].islower():
                dfs(start + 1, temp + s[start])
                dfs(start + 1, temp + s[start].upper())
            else:
                dfs(start + 1, temp + s[start])
                dfs(start + 1, temp + s[start].lower())

        dfs(start, "")
        return result


if __name__ == '__main__':
    s = Solution()
    t = s.letterCasePermutation()
    print(t)
