# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self,root):
        if root == None:
            return 
        self.inorder(root.left)
        self.inorderStack.append(root.val)
        self.inorder(root.right)
        
    def __init__(self, root: TreeNode):
        self.inorderStack = []
        self.inorder(root)
        self.size = len(self.inorderStack)
        self.ptr = 0
        
    def next(self) -> int:
        val = self.inorderStack[self.ptr]
        self.ptr += 1
        return val
        
    def hasNext(self) -> bool:
        if self.ptr<=(self.size-1):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()