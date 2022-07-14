class Solution:
    def average(self, salary: List[int]) -> float:
        avgSal = 0
        minSal = salary[0]
        maxSal = salary[0]
        
        for sal in salary[1:]:
            flag = 0
            if sal < minSal:
                if maxSal != minSal:
                    avgSal += minSal
                minSal = sal
                flag = 1
            if sal > maxSal:
                if maxSal != minSal:
                    avgSal += maxSal
                maxSal = sal
                flag = 1
            if not flag:
                avgSal += sal
        
        return avgSal/(len(salary)-2)
                
        