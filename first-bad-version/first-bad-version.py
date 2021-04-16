# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = n
        while(left<=right):
            mid = (left+right)//2
            midVal = isBadVersion(mid)
            #print(mid,midVal,left,right)
            if midVal == True and mid-1 == 0:
                break
            
            if midVal == True and isBadVersion(mid-1) == False:
                #print("come",mid)
                break
            
            if midVal == True:
                right = mid-1
            else:
                #print("right")
                left = mid+1
        
        #res = binarySearch(1,n)
        #print(mid)
        return mid
        