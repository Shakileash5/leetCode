# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        inorderList = []
        preOrderList = []
        
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            inorderList.append(root.val)
            inorder(root.right)
        
        def preOrder(root):
            if root == None:
                preOrderList.append(None)
                return
            preOrderList.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        
        #inorder(root)
        preOrder(root)
        #print(preOrderList,inorderList)
        serialised = {
            "inorder": inorderList,
            "preorder": preOrderList
        }
        
        return serialised
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        inorder = data["inorder"]
        preorder = data["preorder"]
        
        def buildTree(preorder,inorder,left,right):
            if left>right:
                return
            
            node = TreeNode(preorder[preorderIdx[0]])
            preorderIdx[0] += 1
            
            if left == right:
                return node
            
            rootIdx = searchInorder(inorder,left,right,node.val)
            
            node.left = buildTree(preorder,inorder,left,rootIdx-1)
            node.right = buildTree(preorder,inorder,rootIdx+1,right)
            
            return node
        
        def searchInorder(inorder,left,right,val):
            for i in range(left,right+1):
                if inorder[i] == val:
                    return i
            return None
        
        def buildPreorder(root,preOrder,preorderIdx):
            if len(preOrder) == 0:
                return None
            if preOrder[0] == None :
                #preorderIdx[0]+=1
                preOrder.pop(0)
                return None
            
            root = TreeNode(preOrder.pop(0))
            root.left = buildPreorder(root.left,preOrder,preorderIdx)
            root.right = buildPreorder(root.right,preOrder,preorderIdx)
            return root
        #buildTree(preorder,inorder,0,len(preorder)-1)
        preorderIdx = [0]
        root = None
        #root = helper(preorder)
        root = buildPreorder(root,preorder,preorderIdx)
        return root 
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))