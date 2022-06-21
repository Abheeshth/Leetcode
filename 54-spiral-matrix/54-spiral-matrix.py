class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        l = []
        r = len(a)
        c = len(a[0])
        top = 0
        down = r-1
        left= 0
        right = c-1
        dirc = 0
        while top<=down and left<=right:
            if dirc == 0:
                for i in range(left,right+1):
                    l.append(a[top][i])
                top+=1
            elif dirc == 1:
                for i in range(top,down+1):
                    l.append(a[i][right])
                right-=1
            elif dirc == 2:
                for i in range(right,left-1,-1):
                    l.append(a[down][i])
                down-=1
            else:
                for i in range(down,top-1,-1):
                    l.append(a[i][left])
                left+=1
            dirc = (dirc+1)%4
        #print(l)
        
        return l