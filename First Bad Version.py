'''
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import time
def isBadVersion(version):
    bad = 1
    if version>=bad:
        return True
    else:
        return False
class Solution:
    def __init__(self):
        self.n=1

    def firstBadVersion(self):
        n=self.n
        #算法部分
        low=1
        height=n
        mid = int(low + (height - low) / 2)
        while low != height:
            time.sleep(0.5)
            print(low,mid,height)
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    height=mid-1

            if isBadVersion(mid):
                if isBadVersion(mid-1) is False:
                    return mid

            if isBadVersion(mid) is False:
                if isBadVersion(mid-1) is False:
                    low=mid+1

            if isBadVersion(mid) is False:
                if isBadVersion(mid+1):
                    return (mid+1)
            mid = int(low + (height - low) / 2)
        return low




if __name__ == '__main__':
    t=Solution()
    s=t.firstBadVersion()
    print(s)
