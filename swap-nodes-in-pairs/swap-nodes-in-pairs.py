# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairsTwo(self,head):
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next
        if length < 2:
            return head
        
        count = 1
        prev = None
        last = None
        temp = None
        while head:
            #print(count,'initial head---.',head)
            if count % 2 == 0:
                #print(head)
                if head.next is not None:
                    #print('head.next not none------')
                    if last is None:
                        #print('last is none-----')
                        temmp = head.next
                        head.next = prev
                        prev.next = temmp
                        temp = head
                    else:
                        #print('last is not none------')
                        temmp = head.next
                        head.next = prev
                        prev.next = temmp
                        last.next = head
                    head = temmp
                    count += 1
                    #print('after swapp head--->',temp)
                    continue
                else:
                    #print('head.next is none')
                    if last is None:
                        #print('last is none')
                        head.next = prev
                        prev.next = None
                        temp = head
                    else:
                        #print('last is not none----')
                        head.next = prev
                        prev.next = None
                        last.next = head
                    #print('after swapp head--->',temp)
                    break
                #print(temp)
            last = prev
            prev = head
            head = head.next
            count += 1
        
        #print('final--------->',temp)
        return temp
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        curr = head
        
        """
        while curr!= None:
            if curr.next:
                val = curr.next.val
                curr.next.val = curr.val
                curr.val = val
                curr = curr.next.next
            else:
                break
        
        count = 0
        while curr.next!=None:
            if count%2==0: 
                print("here")
                temp = curr.next.val
                curr.next.val = curr.val
                curr.val = temp
            curr = curr.next
            count+=1"""
            
        return self.swapPairsTwo(head)
           