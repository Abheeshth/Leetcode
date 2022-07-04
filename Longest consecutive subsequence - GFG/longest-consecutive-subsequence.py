 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,nums, N):
        #code here
        s= set()
        if len(nums)<=0:
            return 0
        
        for i in nums:
            s.add(i)
           
        maxi = float('-inf')
        for j in range(len(nums)):
            count = 0
            if nums[j]-1 not in s:
                p = nums[j]
                while p in s:
                    p+=1
                    count+=1
            maxi = max(maxi,count)
        return maxi
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends