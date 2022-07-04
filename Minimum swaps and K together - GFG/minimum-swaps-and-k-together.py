#User function Template for python3

def minSwap (arr, n, k) : 
    #Complete the function
    # first count all the less elements
    count = 0
    for i in arr:
        if i<= k:
            count+=1
    if count == 0:
        return 0
        
    i = 0
    j = 0 
    bad = 0
    ans = float('inf')
    
    while j<n:
        if arr[j] >k:
            bad+=1
        if j-i+1 <count:
            j+=1
        elif j-i+1 == count:
            ans = min(ans,bad)
            if arr[i] >k :
                bad-=1
            i+=1
            j+=1
            
    return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends