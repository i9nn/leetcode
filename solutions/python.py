#
#   My Java solutions to the LeetCode Java exercises. 
#   Feel free to poke around.
#
#   Exercises finished: 1
#

class Solution:
    # 9. Palindrome Number [EASY]
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

    # 1920. Build Array from Permutation [EASY] 
    def buildArray(self, nums: List[int]) -> List[int]:
        lst = [nums[i] for i in nums]
        return lst
        
