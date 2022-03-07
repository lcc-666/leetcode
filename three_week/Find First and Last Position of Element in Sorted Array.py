"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""


class Solution:
    def __init__(self):
        self.nums = [5,7,7,8,8,10]
        self.target = 6

    def searchRange(self):
        nums = self.nums
        target = self.target
        # 算法部分
        n = len(nums)
        if n == 0:
            return [-1, -1]

        def firstPostition(nums, target):
            left = 0
            right = n - 1
            while left < right:
                mid = int((left + right) / 2)
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid
                else:
                    right = mid - 1
            if nums[left] == target:
                return left
            else:
                return -1

        def lastPostition(nums, target):
            left = 0
            right = n - 1
            while left < right:
                mid = int((left + right + 1) / 2)
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid
                else:
                    right = mid - 1
            return left


        first = firstPostition(nums, target)
        if first == -1:
            return [-1, -1]
        last = lastPostition(nums, target)
        return [first, last]

if __name__ == '__main__':
    t=Solution()
    s=t.searchRange()
    print(s)