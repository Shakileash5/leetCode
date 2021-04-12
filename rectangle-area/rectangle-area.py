class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        def findDifference(a,b):
            if a>=0 and b>=0:
                return b-a
            elif a<0 and b>=0:
                a = abs(a)
                return a+b
            elif a<0 and b<0:
                return abs(a) - abs(b)
        
        def isIntersecting(rct1,rct2):
            
            if rct1[0] == rct1[2] or rct1[2] == rct1[3] or rct2[0] == rct2[2] or rct2[2] == rct2[3]:
                return False
            
            if rct1[0]>rct2[2] or rct1[2]<rct2[0]:
                return False
            
            if rct1[3]<rct2[1] and rct2[3]<rct1[1]:
                return False
            
            return True
        
        def intersection(rect1,rect2):

            x1,y1 = max(rect1[0],rect2[0]),max(rect1[1],rect2[1])
            x2,y2 = min(rect1[2],rect2[2]),min(rect1[3],rect2[3])            
            
            height = abs(y1-y2)
            width = abs(x1-x2)
            
            area = height*width
            
            return area
        
        heightA = findDifference(B,D)
        widthA = findDifference(A,C)
        AreaA = heightA*widthA
        
        heightB = findDifference(F,H)
        widthB = findDifference(E,G)
        AreaB = heightB*widthB
        
        left_bound = max(A, E)
        right_bound = min(C, G)
        top_bound = min(D, H)
        bot_bound = max(F, B)
        
        area = AreaA+AreaB
        #print(area,intersection([A,B,C,D],[E,F,G,H]))
        #print(heightA,widthA,heightB,widthB,AreaA,AreaB)
        #if [A,B,C,D] == [E,F,G,H] or isIntersecting([A,B,C,D],[E,F,G,H]) == True:
        if left_bound < right_bound and bot_bound < top_bound:
            areaC = intersection([A,B,C,D],[E,F,G,H])
            area = area - areaC
            return area
        return area
                