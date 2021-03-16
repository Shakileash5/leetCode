class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        size1 = len(nums1)
        size2 = len(nums2)
        
        merPointer = 0
        secondPointer = 0
        sizeVar = size1 - size2
        flag = 0
        #nums1.insert(4,2)
        #nums1[0] = nums1[1]
        #def insertAt
        if m == 0:
            while secondPointer<n:
                nums1[secondPointer] = nums2[secondPointer]
                secondPointer+=1            
            #nums1 = nums2
        else:
            while(secondPointer<size2):
                print(merPointer,secondPointer,sizeVar,nums1)
                if nums1[merPointer]<=nums2[secondPointer] and merPointer+1<size1 and nums1[merPointer+1]>=nums2[secondPointer]:
                    #nums1 = nums1[:merPointer+1] + [nums2[secondPointer]] + nums1[merPointer+1:]
                    nums1.insert(merPointer+1,nums2[secondPointer])
                    #merPointer+=1
                    secondPointer+=1
                    sizeVar+=1
                elif nums1[merPointer]>nums2[secondPointer]:
                    nums1.insert(merPointer,nums2[secondPointer])
                    secondPointer+=1
                    sizeVar+=1
                elif merPointer == 0 and nums1[merPointer]>nums2[secondPointer]:
                    #nums1 = nums2[secondPointer]+nums[:]
                    nums1.insert(0,nums2[secondPointer])
                    secondPointer+=1
                    #merPointer+=1
                    sizeVar+=1
                elif merPointer>=sizeVar:
                    print("here")
                    flag = 1
                    break
                merPointer+=1

            if flag == 1:
                merPointer = sizeVar
                while secondPointer<size2:
                    nums1[merPointer] = nums2[secondPointer]
                    merPointer+=1
                    secondPointer+=1
                #merPointer-=1
                print(merPointer,nums1,len(nums1))
                s = len(nums1)
                while merPointer<s:
                    print("timesH",merPointer)
                    nums1.pop()
                    merPointer+=1
                #nums1 = nums1[:sizeVar] + nums2[secondPointer:]  
            else:
                merPointer = sizeVar
                #merPointer-=1
                print(merPointer,nums1,len(nums1))
                #nums1  = nums1[:sizeVar]
                s = len(nums1)
                while merPointer<s:
                    print("times",merPointer)
                    nums1.pop()
                    merPointer+=1
            print(nums1)
            #nums1.pop()
            #nums1.append(23)
        return
                
        