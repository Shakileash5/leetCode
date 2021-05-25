# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetweenTwo(self,head,left,right):
        if left == right:
            return head
        
        tempHead = head
        start = None
        last = None
        count = 1
        lastNext = None
        startPrev = None
        flag = 0
        
        while head:
            if count == left:
                start = head
                flag = 1
            elif count == right:
                last = head
                lastNext = head.next
                break
            count += 1
            if flag == 0:
                startPrev = head
            head = head.next
        
        #print(start,last.val,startPrev.val,lastNext.val)
        last.next = None
        curr = start
        prev =  None
        next_ = None
        while curr:
            #print(curr)
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        #print(tempHead,start,startPrev)
        if startPrev != None:
            startPrev.next = prev
        else:
            tempHead = prev
        start.next = lastNext
        #print(start,tempHead,prev)
        return tempHead
        
            
        
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        def solutionOne():
            if left == right:
                return head

            start = head
            prev = None
            current = head
            nextN = None

            headTemp = head
            currentPos = 1
            while currentPos < left:
                prev = head
                head = head.next
                currentPos+=1
            if prev!=None:    
                start = prev
            #print(head,prev)
            tail = head
            prev = None
            current = head
            while(currentPos>=left and currentPos<=right):
                #print(prev,current,"\n")
                nextN = current.next
                current.next = prev
                prev = current
                current = nextN
                currentPos+=1

            #prevLeft.next = prevLeft
            #print(start,tail)
            #tail = start.next
            start.next = prev
            tail.next = current
            #headT.next = current
            #prev.next = current
            #print(prev,current,tail)
            if left>1:
                return headTemp
            return prev
        
        return self.reverseBetweenTwo(head,left,right)
        
            
        