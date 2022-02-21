'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
'''
class Solution:
    def __init__(self):
        self.l1=[5,6]
        self.l2=[5,4,9]

    def addTwoNumbers(self):
        l1=self.l1
        l2=self.l2

        #算法部分
        num_cha = len(l1) - len(l2)
        if num_cha<0:
            num_cha=-num_cha
            max_list=l2
            min_list = l1
        else:
            min_list = l2
            max_list = l1
        if num_cha:
            max_num=max(len(l1),len(l2))
            min_num=min(len(l1),len(l2))
            l4=[]
            l3=max_list[min_num:]
            for i in range(min_num):
                l4.append(max_list[i]+min_list[i])
            l3=l4+l3
        else:
            l3=[]
            for i in range(len(l1)):
                l3.append(max(l1,l2)[i]+min(l1,l2)[i-num_cha])

        ten=0
        result=[]
        print(l3)
        for i in range(len(l3)):
            item=l3[i]+ten
            s=item%10
            result.append(item%10)
            ten=(item-item%10)//10
        if ten:
            result.append(ten)
        print(result)


        return (result)

if __name__ == '__main__':
    t=Solution()
    t.addTwoNumbers()