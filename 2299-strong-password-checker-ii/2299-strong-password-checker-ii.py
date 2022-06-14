class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        #digit = False
        #length = False
        onelowercase = False
        oneuppercase = False
        onedigit = False
        onespecialcharacter = False 
        #adjacent = False
        
        for i,value in enumerate(password):
            #print(ord(value))
            if i>0 and password[i-1] == value:
                #print(password[i-1])
                #print(value,i)
                #print('sjdhs')
                return False
            if value.isdigit():
                onedigit = True
            elif ord(value)<=122 and ord(value)>=97:
                onelowercase  = True
            elif ord(value)<=90 and ord(value)>=65:
                oneuppercase = True
            elif value in "!@#$%^&*()-+":
                onespecialcharacter = True

        
        return onedigit and onelowercase and oneuppercase and onedigit and onespecialcharacter
                
                
                
        