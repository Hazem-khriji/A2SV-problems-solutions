class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s=skill[0]+skill[-1]
        chem=skill[0]*skill[-1]
        l,r=1,len(skill)-2
        while(l<r):
            ss=skill[l]+skill[r]
            cc=skill[l]*skill[r]
            if(ss==s):
                chem+=cc
            else:
                chem=-1
                break 
            l+=1
            r-=1
        return chem
