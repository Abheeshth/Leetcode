class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        #Albhabets  = [s[0],s[3]]
        #digits = [s[1],s[4]]
        alpha1 = s[0]
        alpha2 = s[3]
        digit1 = s[1]
        digit2 = s[4]
        l = []
        for i in range(ord(alpha1),ord(alpha2)+1):
            for j in range(int(digit1),int(digit2)+1):
                l.append(str(chr(i))+str(j))
        return l