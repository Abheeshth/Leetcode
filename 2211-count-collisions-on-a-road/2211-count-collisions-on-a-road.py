class Solution:
    def countCollisions(self, directions: str) -> int:
        R = 0
        L = 0
        S = 0
        cout = 0
        collisions = []
        
        for i in directions:
            if i == 'R':
                #print('12')
                R+=1
            elif i  == 'S':
                #print(23)
                cout+=R
                R = 0
                S = 1
            elif i == 'L':
                if R>0:
                    cout+=(R-1)
                    cout+=2
                    S = 1
                elif S>0:
                    cout+=1
                R = 0
                
        return cout
                
                
        