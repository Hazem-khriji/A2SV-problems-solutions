# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower_bound = 1
        higher_bound = n
        while(True):
            pick = (lower_bound+higher_bound)//2
            x = guess(pick)
            if x == 1:
                lower_bound = pick + 1
            elif x == -1:
                higher_bound = pick - 1
            else:
                return pick
