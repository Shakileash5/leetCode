class Solution:
    def longestWord(self, words: List[str]) -> str:
        size = len(words)
        words.sort()
        hashMap = {}
        largestWord = ''
        hashMap[''] = True
        
        for i in range(size):
            word_ = words[i]
            if  word_[:-1] in hashMap:
                if len(word_)>len(largestWord):
                    largestWord = word_
                elif len(word_)==len(largestWord):
                    if word_<largestWord:
                        largestWord = word_
                hashMap[word_] = True
        
        return largestWord
                