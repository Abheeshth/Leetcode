class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        rest  = 0
        count = 0.00000
        for [x,y] in brackets:
            print(x,y)
            if income >x:
                p = x-rest
                rest = x
                count+= float(f'{((p*y)/100):.5f}')
            else:
                p = income-rest
                count+= float(f'{((p*y)/100):.5f}')
                break
                
        return count
                
        