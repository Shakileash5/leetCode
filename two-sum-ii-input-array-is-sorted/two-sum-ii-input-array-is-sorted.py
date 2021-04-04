class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        start = 0
        end = size - 1
        
        while(start<end):
            val = numbers[start] + numbers[end]
            if val == target:
                return start+1,end+1
            elif val>target:
                end -=1
            elif val<target:
                start+=1
        
        return 0,0
    