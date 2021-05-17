# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recur(self,head,multiple):
        if head == None:
            return 0
        return self.recur(head.next,multiple*10) + head.val*multiple
        
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #print(l1,l2)
        resultRoot = ListNode()
        def naiveSolution():
            strr1 = ""
            strr2 = ""
            while True:
                if l1 !=None:
                    strr1 = strr1 + str(l1.val)
                    l1 = l1.next
                if l2 !=None:
                    strr2 = strr2 + str(l2.val)
                    l2 = l2.next
                if l1==None and l2==None:
                    val = str(int(strr2[::-1]) + int(strr1[::-1]))
                    #print(strr1,strr2,val)
                    temp = resultRoot
                    for i in range(len(val)-1,-1,-1):
                        resultRoot.val = int(val[i])
                        if i !=0:
                            resultRoot.next = ListNode()
                            resultRoot = resultRoot.next
                        else:
                            resultRoot.next = None
                    resultRoot = temp    
                    print(resultRoot)
                    return resultRoot
        
        num1 = self.recur(l1,1)
        num2 = self.recur(l2,1)
        num3 = num1+num2
        num3 = str(num3)
        num3 = num3[::-1]
        tempRoot = resultRoot
        for i in range(len(num3)):
            resultRoot.val = int(num3[i])
            if i != len(num3)-1:
                resultRoot.next = ListNode()
                resultRoot = resultRoot.next
            else:
                resultRoot.next= None
            
        
        return tempRoot
                
            