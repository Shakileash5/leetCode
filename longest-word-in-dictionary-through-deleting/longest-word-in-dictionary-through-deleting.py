class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x:(-len(x),x))
        size = len(s)
        for word in dictionary:
            idx = 0
            i = 0
            while idx<size and i<len(word):
                if word[i] == s[idx]:
                    idx += 1
                    i += 1
                else:
                    idx += 1
            if i>=len(word):
                return word
            
        return ''