class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {char:indx for indx, char in enumerate(s)}
        print(dic)
        sol = []
        l = 0
        r = 0
        for index, char in enumerate(s):
            r = max(r, dic[char])
            if index == r:
                sol.append(r - l + 1)
                l = index + 1
        return sol