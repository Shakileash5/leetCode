class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        size = len(emails)
        hashMap = {}
        count = 0
        
        for i in range(size):
            splits = emails[i].split('@')
            if '.' or '+' in splits[0]:
                tempStr = ''
                j = 0
                while(j<len(splits[0])):
                    if splits[0][j] == '+':
                        break
                    elif splits[0][j] != '.':
                        tempStr += splits[0][j]
                    j += 1
                tempStr += '@' + splits[1]
                #print(hashMap,tempStr)
                if tempStr not in hashMap:
                    hashMap[tempStr] = 1
                    count += 1
            else:
                if emails[i] not in hashMap:
                    hashMap[emails[i]] = 1
                    count += 1
                    
        return count
                