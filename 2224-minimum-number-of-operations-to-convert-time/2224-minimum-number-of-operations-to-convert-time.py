class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        total_minutes1 = (int(correct[:2]) - int(current[:2]))*60
        total_minutes2 = (int(correct[3:]) - int(current[3:]))
        total = total_minutes1 + total_minutes2
        l  = [60,15,5,1]
        i = 0
        steps = 0
        while total:
            #print(total)
            steps += total//l[i]
            total = total%l[i]
            i+=1
            
        return steps
            
            
            
        
        