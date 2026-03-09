class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while(l<r):
            if not('a'<=s[l].lower()<='z' or '0'<=s[l]<='9'):
                l+=1
            elif not( 'a'<=s[r].lower()<='z' or '0'<=s[r]<='9'):
                r-=1
            else:
                if(s[l].lower()!=s[r].lower()):
                    return False
                else:
                    r-=1
                    l+=1
        return True