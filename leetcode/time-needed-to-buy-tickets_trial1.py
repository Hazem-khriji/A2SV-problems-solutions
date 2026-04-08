from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = 0
        q = deque ()
        while (tickets[k] != 0) :
            if(tickets[i] != 0):
                time+=1
                tickets[i]-= 1 
            
            i = (i + 1)%len(tickets)
        
        return time