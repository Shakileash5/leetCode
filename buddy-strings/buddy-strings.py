class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sizeS = len(s)
        sizeG = len(goal)
        s = list(s)
        
        hashMap = {}
        flag = False
        swap = False
        toSwap = None
        for i in range(sizeS):
            if s[i] not in hashMap:
                hashMap[s[i]] = [i]
            else:
                hashMap[s[i]].append(i)
                flag = True
        
        """for i in range(sizeS):
            if s[i] != goal[i]:
                if swap == False:
                    if goal[i] in hashMap:
                        if i in hashMap[goal[i]]:
                            s[i],s[hashMap[goal[i]][0]] = s[hashMap[goal[i]][0]],s[i]
                            swap = True
                else:
                    return False"""
        
        for i in range(sizeS):
            if s[i] != goal[i]:
                #print(s[i],toSwap,goal[i])
                if toSwap == None:
                    if goal[i] not in hashMap:
                        return False
                    toSwap = s[i]
                    s[i] = goal[i]
                else:
                    if goal[i] in hashMap:
                        if goal[i] == toSwap:
                            s[i] = toSwap
                            swap = True
                        else:
                            return False
                    else:
                            return False
                
        
        s = ''.join(s)
        #print(swap,toSwap)
        if s == goal:
            if swap == True or flag == True:
                return True
        return False
        