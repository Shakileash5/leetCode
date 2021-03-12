class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strList = map(str,digits)
        string = "".join(strList)
        string = int(string)
        string += 1
        string = str(string)
        strList = list(string)
        return(list(map(int,strList)))
        