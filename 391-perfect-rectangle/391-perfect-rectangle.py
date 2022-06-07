class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Steps =
        # Step 1 First we'll calculate the area of each rectagle seprately so that we can finaaly compare with the final rectangle
        # Step 2 we will taking Xor of every corner so that every repeated corner get cancled because it is in a intiriar part 
        
        area = 0
        corners = set()
        for x,y,X,Y in rectangles:
            area+=((Y-y)*(X-x))
            corners^={(x,y),(x,Y),(X,y),(X,Y)}
        
        # check if we are getting exactly four corners or not
        if len(corners)!=4:
            return False
        
        # let's find the cornor point to finad the area of a final rectagle
        x,y = min(corners, key =lambda x:x[0]+x[1])
        X,Y = max(corners,key = lambda x:x[0]+x[1])
        
        final = (Y-y)*(X-x)
        
        return final == area
            