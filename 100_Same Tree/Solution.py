class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if(q.val == p.val):
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
