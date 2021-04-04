class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        ver1Stack = []
        ver2Stack = []
        
        ver1Stack = [int(x) for x in version1.split('.')]
        ver2Stack = [int(x) for x in version2.split('.')]
        
        #print(ver1Stack)
        #print(ver2Stack)
        
        size1 = len(ver1Stack)
        size2 = len(ver2Stack)
        idx = 0
        flag = 0
        
        while (idx<size1):
            if idx>=size2:
                flag = 1
                break
            if ver1Stack[idx]>ver2Stack[idx]:
                return 1
            elif ver1Stack[idx]<ver2Stack[idx]:
                return -1
            
            idx += 1
        #print(idx,size1,size2)
        if flag == 0:
            for i in range(idx,size2):
                if ver2Stack[i] != 0:
                    return -1
        if flag == 1:
            #print("here",idx,size1)
            for i in range(idx,size1):
                #print(ver1Stack)
                if ver1Stack[i]!= 0:
                    return 1
        
        return 0
                
        