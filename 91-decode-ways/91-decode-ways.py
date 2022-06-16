class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        for i in range(1,len(s)):
            # first case is both are zero
            if s[i-1] == '0' and s[i] == '0':
                dp[i] = 0
            # if fist is zero and second is non zero
            
            elif s[i-1] == '0' and s[i] != '0':
                dp[i] = dp[i-1]
                
            # if fist is non zero and second is zero
            elif s[i-1] != '0' and s[i] == '0':
                if int(s[i-1:i+1]) <=26:
                    dp[i] = dp[i-2] if i>=2 else 1
                else:
                    dp[i] = 0
                    
            # if both are non zero
            elif s[i-1] != '0' and s[i] != '0':
                if int(s[i-1:i+1]) <=26:
                    dp[i] = dp[i-1]+ (dp[i-2] if i>=2 else 1)
                else:
                    dp[i] = dp[i-1]
                    
        return dp[-1]
        
        # 
        
        
        
            
                
        