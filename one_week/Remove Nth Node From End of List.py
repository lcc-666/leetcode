"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
"""


def list_to_link(nums):
    """
    从列表转换成链表
    """
    new = ListNode(0)
    head = new
    for num in nums:
        head.next = ListNode(num)
        head = head.next
    return new.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        ls = [1, 2, 3, 4, 5]
        self.head = list_to_link(ls)
        self.n = 2

    def removeNthFromEnd(self):
        head = self.head
        n = self.n
        # 算法部分
        slow = fast = head
        if fast.next is None:
            return None
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow == head:
            head = slow.next
            return head
        if fast is None:
            head = slow.next
            return head
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    t = Solution()
    s = t.removeNthFromEnd()
