class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rest = []
        for i in range(len(rocks)):
            rest.append(capacity[i]-rocks[i])
            
        rest.sort()
        j = 0
        #print(rest)
        while j < len(rocks) and additionalRocks > 0:
            if additionalRocks>=rest[j]:
                additionalRocks = additionalRocks - rest[j]
                rest[j] = 0
                j+=1
            else:
                break
        #print(rest)
        return rest.count(0)
            