class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = []
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.append(left * left)
                l += 1
            else:
                answer.append(right * right)
                r -= 1
        answer = answer[::-1]
        return answer
                
                
                
                
            
            
            
        