class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        nums = primes[:]
        i = 1
        size = len(primes)
        
        nums = primes.copy() # do a deep copy 
        heapq.heapify(nums) #create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums)
            #print(nums,p)#take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime)
                print(p*prime)#add all those multiples with the smallest number
                if p % prime == 0:
                    break
        #print(nums,p)
        
        """ while len(nums)<n:
            hard = i
            for prime in primes:
                while(hard>0):
                    if hard%prime == 0:
                        hard = hard//prime
                    else:
                        break
                if hard<0:
                    break
            
            if hard == 1:
                nums.append(i)
                #print(i,hard)
            i+=1"""
        return p
            
                