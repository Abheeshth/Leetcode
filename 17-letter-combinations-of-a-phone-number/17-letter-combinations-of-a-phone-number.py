class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # it should be simple
        # it's a simple combination question
        # step 1 -let's map all the no. to their respective charachters
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        combinations = []
        for i in digits:
            if len(combinations) == 0:
                combinations = list(interpret_digit[i])
            else:
                allletters = list(interpret_digit[i])
                length = len(combinations)
                for j in range(length):
                    q = combinations.pop(0)
                    for k in allletters:
                        combinations.append(q+k)
                        
                        
        return combinations
                
                
            
        
        