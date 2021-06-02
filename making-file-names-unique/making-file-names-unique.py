class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = {}
        ans = []
        fileCount = 0
        
        for key in names:
            if key not in res:
                    ans.append(key)
                    res[key] = 1
            else:
                fileCount = res[key]
                while fileCount:
                    str_ = key + "(" + str(fileCount) + ")"
                    if str_ not in res:
                        ans.append(str_)
                        res[str_] = 1
                        fileCount += 1
                        break
                    fileCount += 1
                res[key] = fileCount
        
        return ans           