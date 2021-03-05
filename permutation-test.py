def recur(res,strn,perms):
    if len(strn) == 0:
        perms.append(res)
        return
    for i in range(len(strn)):
        recur(res+strn[i],strn[:i]+strn[i+1:],perms)

perms = []
recur("","abc",perms)
sep = str([1,2,3]).split(",")
print(perms,"".join(sep)[1:-1])