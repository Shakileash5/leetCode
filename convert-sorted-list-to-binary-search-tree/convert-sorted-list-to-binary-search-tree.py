# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        if head == None:
            return None
        arr = []
        def depthOfList(head):
            height = 1
            while head!=None:
                arr.append(head.val)
                head = head.next
                height+=1
            return height
        
        def getVal(head,index):
            count = 0
            while count<index:
                head = head.next
                count+=1
            
            return head.val
        
        def binaryBuildTree(arr,left,right):
            
            if left>right:
                return None
            
            mid = (left+right)//2
            
            #val = getVal(head,mid)
            node = TreeNode(arr[mid])
            
            if left == right:
                return node
            
            node.left = binaryBuildTree(arr,left,mid-1)
            node.right = binaryBuildTree(arr,mid+1,right)
            
            return node
        
        size = depthOfList(head)   
        print(arr,size)
        tree = binaryBuildTree(arr,0,size-2)

        return tree
        
            