# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRightSolTwo(self,head,n):
        prev = None
        tempHead = head
        nthNode = head
        endNode = None
        count = 0
        size = 0
        while head!= None:
            size+=1
            head = head.next
        head = tempHead
        if size == 0:
            return head
        n = n%size
        if n == 0 or size == 0:
            return head
        
        while head!=None:
            if count>=n:
                prev = nthNode
                nthNode = nthNode.next
            count+=1
            endNode = head
            head = head.next
        #print(prev.val,nthNode.val)
        prev.next = None
        endNode.next = tempHead
        return nthNode
            
    
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        proxyHead = head
        headC = head
        breakPoint = head
        count = 0
        flag = 0
        headL = head
        
        def naiveSolution():
            if head == None:
                return head
            def length(size,curr):
                if curr.next==None:
                    return size
                return length(size+1,curr.next)

            size = length(1,headL)
            if size<k:
                k = k%size
            if size == k or k == 0:
                return head


            while head.next!=None:
                if count>=k:
                    flag = 1
                    if breakPoint.next == None:
                        breakPoint = headC
                    else:
                        breakPoint = breakPoint.next

                #if flag == 0 and head.next.next == None:
                #prev = head
                head = head.next
                count+=1
                #print(count,breakPoint,"\n",head)

            print(breakPoint,proxyHead)
            proxyHead = breakPoint.next
            print("\n",proxyHead)
            head.next = headC
            breakPoint.next = None
        
        
        #return proxyHead
        return self.rotateRightSolTwo(head,k)        
        