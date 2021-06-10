class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        size = len(croakOfFrogs)
        frogs = [0]*5
        hashMap = {
            'c' : 0,
            'r' : 1,
            'o' : 2,
            'a' : 3,
            'k' : 4
        }
        count = 0
        last = -1
        for i in range(size):
            if croakOfFrogs[i] == 'c':
                frogs[0] += 1
                if count>=1:
                    count -= 1
            else:
                key = hashMap[croakOfFrogs[i]]
                #print(key,croakOfFrogs[i])
                if frogs[key-1]>frogs[key]:
                    frogs[key] += 1
                else:
                    return -1
            if croakOfFrogs[i] == 'k':
                #print(frogs)
                count += 1
        #print(frogs)
        for i in range(1,5):
            if frogs[i] != frogs[i-1]:
                return  -1
        
        return count
        