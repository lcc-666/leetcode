"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，
如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
"""
import time

class Solution:
    def __init__(self):
        self.nums = [-1,0,3,5,9,12]
        self.target = 9

    def search(self):
        nums = self.nums
        target = self.target
        # 算法部分
        low = 0
        height = len(nums)-1
        mid = (height + low) // 2

        while low != height:
            print(low, mid, height)

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid+1
            else:
                height = mid
            mid = int((low + height) / 2)
        if nums[low]==target:
            return low
        return -1


if __name__ == '__main__':
    t = Solution()
    s = t.search()
    print(s)
