class Solution:
    def lengthLongestPath(self, input: str) -> int:
        size = len(input)
        max_ = 0
        lines = input.split('\n')
        dirs = []
        
        for line in lines:
            tabCount = line.count('\t')
            fileName = line[tabCount:]
            if '.' in fileName:
                if tabCount == 0:
                    max_ = max(max_,len(fileName))    
                else:
                    if tabCount<len(dirs):
                        #print("t",tabCount,dirs)
                        while(tabCount<len(dirs)):
                            #print('out',dirs)
                            dirs.pop()
                    tempDirs = '\\'.join(dirs+[fileName])
                    max_ = max(max_,len(tempDirs))
                    #print(tempDirs)
                #print(max_)
            else:
                if tabCount<len(dirs):
                    #print("t",tabCount,dirs)
                    while(tabCount<len(dirs)):
                        #print('out',dirs)
                        dirs.pop()
                        
                dirs.append(fileName)
            #print(dirs)
        
        return max_