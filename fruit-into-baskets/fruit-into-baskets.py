class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = defaultdict(int)
        start = 0
        maxFruit = 0
        size = len(tree)
        idx = 0
        
        while(idx<size):
            basket1 = []
            basket2 = []
            idx2 = idx
            flag = 0
            count = 0
            while(idx2<size):
                if basket1 == []:
                    basket1.append(tree[idx2])
                    count += 1
                elif basket1[-1] != tree[idx2]:
                    if basket2 == []:
                        basket2.append(tree[idx2])
                        count += 1
                    elif basket2[-1] == tree[idx2]:
                        basket2.append(tree[idx2])
                        count += 1
                    else:
                        flag = 1
                        break
                else:
                    basket1.append(tree[idx2])
                    count += 1
                idx2 += 1
            #print(count,basket1,basket2)
            maxFruit = max(maxFruit,count)
            if flag == 1:
                idx = idx + 1
            else:
                break
        
        return maxFruit