class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        # let's do sliding window
        start = 0
        i  = 0
        maxi = float('inf')
        temp  = 0
        while i < len(a):
            #temp = 0
            

            
            temp += a[i]
            while temp > x:
                maxi = min(maxi,i-start+1)
                temp-=a[start]
                start+=1
            
            i+=1
        return maxi
            
            
            
            
        


#{ 
#  Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends