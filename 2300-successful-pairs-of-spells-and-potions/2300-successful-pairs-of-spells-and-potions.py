class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # let sort th postions first
        # then we'll do the binary search in potions
        
        potions.sort()
        l = len(potions)
        
        def bs(spell):
            initial = 0
            end = l
            ret = -1
            while initial< end:
                mid = (initial+end)//2
                
                if spell*potions[mid]>=success:
                    end = mid
                    ret = mid
                    
                else:
                    initial = mid+1
            return l-ret if ret!= -1 else 0
        return [bs(spell) for spell in spells]
        
                    
        