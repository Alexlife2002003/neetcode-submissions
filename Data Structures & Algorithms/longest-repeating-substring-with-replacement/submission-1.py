class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def max_len(target):
            longest=0
            wrong_char=0
            left=0

            for right in range(len(s)):
                if s[right]!=target:
                    wrong_char+=1
                
                while wrong_char>k:
                    if s[left]!=target:
                        wrong_char-=1
                    left+=1
                
                longest=max(longest, right-left+1)
            
            return longest
        
        return max(max_len(char) for char in set(s))