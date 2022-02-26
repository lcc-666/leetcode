"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。


示例 1：
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").

示例 2：
输入：s1= "ab" s2 = "eidboaoo"
输出：false
"""


class Solution:
    def __init__(self):
        self.s1 = "dbb"
        self.s2 = "ccc"

    def checkInclusion(self):
        s1 = self.s1
        s2 = self.s2
        # 算法部分
        n1 = len(s1)
        n2 = len(s2)
        dict1 = {}
        dict2 = {}
        for i in s1:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1

        if n1 > n2:
            return False
        while n1 == n2:
            if s1 == s2:
                return True
            else:
                break

        for i in range((n2 - n1) + 1):
            s = s2[i:i + n1]
            for item in s:
                if item in dict2:
                    dict2[item] = dict2[item] + 1
                else:
                    dict2[item] = 1
            if dict1 == dict2:
                return True
            else:
                dict2.clear()
        return False


if __name__ == '__main__':
    t = Solution()
    s = t.checkInclusion()
    print(s)
