# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
            
    def __init__(self, root: TreeNode):
        def nextGenerator(node):
            if node.left:
                yield from nextGenerator(node.left)
            yield node.val
            if node.right:
                yield from nextGenerator(node.right)
                
        self.generator = nextGenerator(root)
        self.root = next(self.generator,None)
            
    def next(self)->int:
        temp = self.root
        self.root = next(self.generator,None)
        return temp
        
    def next_try(self) -> int:
            print("before",self.stack,self.checked)
            while(self.stack):
                if self.checked == False:
                    if self.root.right:
                            self.nextStack.append(1)
                    if self.root.left:
                        self.stack.append(self.root.left)
                        print("added",self.root.left.val)
                        self.root = self.root.left
                        continue
                
                
                if self.checked == False:
                    node = self.stack.pop()
                    self.root = node
                    self.checked = True
                    print(self.root.val)
                    return self.root.val
                self.checked = False
                if self.root.right:
                    self.nextStack.pop()
                    self.stack.append(self.root.right)
                    self.root = self.root.right
            print("After",self.stack)
            return self.root

    def hasNext(self) -> bool:
        #print(self.root.val,"called",self.root.right!=None)
        #node = self.stack[-1]
        #print(self.stack,self.nextStack)
        if self.root!=None:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()