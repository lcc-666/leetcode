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
        self.s1 = "ba"
        self.s2 = "ab"

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
        if n1 ==1:
            if s1 in s2:
                return True
            else:
                return False

        if n1 > n2:
            return False
        while n1 == n2:
            if s1 == s2:
                return True
            else:
                break

        for i in s2[0:n1]:
            if i in dict2:
                dict2[i] = dict2[i] + 1
            else:
                dict2[i] = 1
        if dict1 == dict2 :
            return True
        for i in range(1,(n2 - n1) + 1):
            s = s2[i:i + n1]
            x=s2[i-1]
            y=s2[i+n1-1]
            if x==y:
                continue

            dict2[x]=dict2[x]-1
            if dict2[x]==0:
                del dict2[x]

            if y in dict2:
                dict2[y]=dict2[y]+1
            else:
                dict2[y]=1
            if dict1==dict2:
                return True

        return False


if __name__ == '__main__':
    t = Solution()
    s = t.checkInclusion()
    print(s)
