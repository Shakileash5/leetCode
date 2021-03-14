class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for f in path.split('/'):
            if f and f!='.':
                if f!='..':
                    stack.append(f)
                elif stack:
                    stack.pop()
        res = "/"+"/".join(stack)
        return res
                    