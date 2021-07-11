class Solution:
    def lengthLongestPath(self, input: str) -> int:
        size = len(input)
        stack = []
        max_ = 0
        file = ''
        
        def dfs(idx,str_,level):
            flag = 0
            subStr = ''
            while(idx<size and input[idx]!='\\'):
                if input[idx] == '.':
                    flag = 1
                subStr+=input[idx]
                idx += 1
            
            if flag == 1:
                max_ = max(max_,len(str_+subStr))
                return
            else:
                subStr += '\\'
            return
        lines = input.split('\n')
        #print(lines)
        dirs = []
        files = []
        
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