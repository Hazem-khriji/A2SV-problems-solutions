class Solution:
    def smallestNumber(self, num: int) -> int:
        s=str(num)
        if(num>=0):
            s=''.join(sorted(s))
            index=-1
            if s[0]=='0':
                index=0
                while(index<len(s) and s[index]=='0'):
                    index+=1
            if(index==-1):
                return int(s) 
            elif(index==len(s)):
                return 0   
            return int(s[index]+s[:index]+s[index+1::])
        else:
            s=''.join(sorted(s,reverse=True))
            s=s[:len(s)-1]
            return -int(s)

            
