#
#   My Java solutions to the LeetCode Java exercises. 
#   Feel free to poke around.
#
#   Exercises finished: 1
#

class Solution:
    # 1. Two Sum [EASY]
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        solutions = ["a", "b"]
        for i in range(len(nums)):
                solutions = [i, nums.index(target - nums[i])] if target - nums[i] in nums and nums.index(target - nums[i]) != i else solutions
                if solutions != ["a", "b"]:
                    return solutions
            
        return solutions
    
    # 9. Palindrome Number [EASY]
    def is_palindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
    
    # 14. Longest Common Prefix [EASY]
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if len(strs) == 1:
            return strs[0]
        
        for i in range(len(strs[0]) + 1):
            prefix = strs[0][:i]
            for j in strs:
                if not j.startswith(prefix):
                    return prefix[:-1]
                
            if len(prefix) == len(strs[0]):
                return strs[0]
                

        return ""

    # 1920. Build Array from Permutation [EASY] 
    def build_array(self, nums: List[int]) -> List[int]:
        lst = [nums[i] for i in nums]
        return lst
        
