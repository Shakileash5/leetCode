# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:
    def shuffleArray(self,arr):
        '''
            Shuffles array using fisher yates algorithm.
        '''
        size = len(arr)
        #print(size)
        for i in range(size-1,-1,-1):
            idx = random.randint(0,i)
            #print(idx,i)
            arr[i],arr[idx] = arr[idx],arr[i]
        return arr
    
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nodesList = []
        self.head = head
        headTemp = head
        self.idx = 0
        self.size = 0
        while head:
            self.nodesList.append(head.val)
            head = head.next
            self.size += 1
        self.nodesList = self.shuffleArray(self.nodesList)
        return
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        #self.idx = (self.idx+1)%self.size
        return random.choice(self.nodesList)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()