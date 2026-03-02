from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        c=Counter(s)
        ss= dict(c.most_common())
        res=""
        for key,value in ss.items():
            res+=(value*key)
        return res

        