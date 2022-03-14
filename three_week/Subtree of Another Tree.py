"""
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

示例 1：

输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
示例 2：

输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self.preorder(root, subRoot)

    def preorder(self, root, subRoot):
        if not root: return False
        resleft = self.preorder(root.left, subRoot)
        resright = self.preorder(root.right, subRoot)
        # 如果 根节点就不同 就直接返回左右子树的结果 跳过这一个root所在的子树
        if root.val != subRoot.val: return resleft or resright
        # 如果 根节点相同 就可以开始一次判断
        return resleft or resright or self.helper(root, subRoot)

    def helper(self, root, subRoot):
        # 保证 子树的构造相同
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # 保证 子树的值 都是相同的
        return root.val == subRoot.val and self.helper(root.left, subRoot.left) and self.helper(root.right,
                                                                                                subRoot.right)
