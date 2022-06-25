class Solution:
    def greatestLetter(self, s: str) -> str:
        p = list(s)
        p.sort()
        print(p)
        capital = []
        small = []
        for i in p:
            if ord(i) <= 90 and ord(i)>= 65:
                capital.append(ord(i))
            else:
                small.append(ord(i))
        print(capital,small)
        for i in small[::-1]:
            if i-32 in capital:
                return chr(i-32)
        return ''
                
                
        
            
        