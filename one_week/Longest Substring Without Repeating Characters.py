"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
"""


class Solution:
    def __init__(self):
        self.s = "abba"

    def lengthOfLongestSubstring(self):
        s = self.s
        # 算法部分

        string_dict = {}
        start = 0
        end = 0
        max=0
        if s == "":
            return 0
        for i in range(len(s)):
            end = i
            if s[end] in s[start:end]:
                start = string_dict[s[end]] + 1
                string_dict[s[i]] = i
            else:
                string_dict[s[i]] = i
            item=(end - start) + 1
            if item>max:
                max=item

        return max


if __name__ == '__main__':
    t = Solution()
    s = t.lengthOfLongestSubstring()
    print(s)
