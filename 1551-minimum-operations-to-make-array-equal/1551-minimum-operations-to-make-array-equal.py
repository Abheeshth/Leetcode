class Solution:
    def minOperations(self, n: int) -> int:
        array = [(2*i)+1 for i in range(n)]
        #print(array)
        total = 0
        i = 0
        q = array[i]
        while q < n:
            total += (n-q)
            i+=1
            q = array[i]
            #print(q)
        return total
            
            
        