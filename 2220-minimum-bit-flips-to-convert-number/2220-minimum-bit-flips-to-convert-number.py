class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        
        if len(start) > len(goal):
            goal = (len(start)-len(goal))*'0'+goal
        if len(start) < len(goal):
            start = (len(goal)-len(start))*'0'+start
            
        print(start,goal)
        
        count = 0
        for i in range(len(start)):
            count += abs(int(start[i]) - int(goal[i]))
        return count
            