class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.right == None and root.left == None:
            return 1
        else:
            leftHeight = 0
            rightHeight = 0
            if root.right != None:
                rightHeight = self.maxDepth(root.right)
            if root.left != None:
                leftHeight = self.maxDepth(root.left)
            return max(leftHeight, rightHeight) + 1
