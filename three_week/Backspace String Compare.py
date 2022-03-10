"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。

示例 2：
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。

示例 3：
输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。
"""


class Solution:
    def __init__(self):
        self.s = "ab#c"
        self.t = "ad#c"

    def backspaceCompare(self):
        s = self.s
        t = self.t

        # 算法部分
        def build(s):
            ret = []
            for ch in s:
                if ch != '#':
                    ret.append(ch)
                elif ret:
                    ret.pop()
            return "".join(ret)

        return build(s) == build(t)

if __name__ == '__main__':
    t=Solution()
    s=t.backspaceCompare()
    print(s)