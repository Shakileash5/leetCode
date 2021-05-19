# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solutionTwo(self,l1,l2):
        if l1==None and l2==None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        resultNode = ListNode()
        res = resultNode
        if l1.val<l2.val:
            resultNode.val = l1.val
            l1 = l1.next
        else:
            resultNode.val = l2.val
            l2 = l2.next
        
        while l1 and l2:
            if l1.val>=l2.val:
                node = ListNode(l2.val)
                resultNode.next = node
                resultNode = resultNode.next
                l2 = l2.next
            else:
                node = ListNode(l1.val)
                resultNode.next = node
                resultNode = resultNode.next
                l1 = l1.next
        if l1 and l2 == None:
            resultNode.next = l1
        elif l2 and l1 == None:
            resultNode.next = l2
        
        #print(res)
        return res
            
            
        
        
        
        
        
        
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def solutionOne():
            index1 = l1
            index2 = l2

            if l1 == None and l2 != None:
                return l2
            if l2 == None and l1 != None:
                return l1
            if l1 == None and l2 == None:
                return l1

            if l1.val > l2.val:
                l1,l2 = l2,l1
                index1,index2 = index2,index1

            resHead = ListNode()
            res = resHead

            while l1!=None and l2!=None:

                    if l1.val<l2.val:
                        res.val = l1.val
                        res.next = ListNode()
                        res = res.next
                        l1 = l1.next
                    elif l2.val<l1.val:
                        res.val = l2.val
                        res.next = ListNode()
                        res = res.next
                        l2 = l2.next
                    else:
                        res.val = l1.val
                        res.next = ListNode()
                        res = res.next
                        l1 = l1.next 



            if l1 == None and l2!=None:
                res.val = l2.val
                res.next = l2.next
            elif l2 == None and l1!=None:
                res.val = l1.val
                res.next = l1.next

            #print(resHead,"\n",l1,"\n",l2)   
        #return resHead
        
        return self.solutionTwo(l1,l2)         