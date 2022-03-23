#
#   My Python solutions to the LeetCode Python exercises. 
#   Feel free to poke around.
#
#   Exercises finished: 5
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
    
    # 58. Length of Last Word [EASY]
    def length_of_last_word(self, s: str) -> int:
        return len(s.split()[len(s.split()) - 1])
    
    # 69. Sqrt(x) [EASY] 
    def my_sqrt(self, x: int) -> int:
        for i in range(x + 1):
            if i * i == x:
                return i 
            elif i * i > x:
                return i - 1
            
        return 0 
    
    # 169. Majority Element [EASY] 
    def majority_element(self, nums: List[int]) -> int:
        return sorted(nums)[len(sorted(nums)) // 2]
    
    # 171. Excel Sheet Column Number
    def title_to_number(self, column_title: str) -> int:
        alphabet, colnum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0 
        
        for i in range(len(column_title)):
            colnum += 26 ** (len(column_title) - (i + 1)) * (alphabet.index(column_title[i]) + 1) 
            
        return colnum
    
    # 412. Fizz Buzz [EASY]
    def fizz_buzz(self, n: int) -> List[str]:
        p = []
        
        for i in range(1, n + 1):
            s = ""
            
            s += "Fizz" if i % 3 == 0 else ""
            s += "Buzz" if i % 5 == 0 else ""
            
            if s == "":
                s = str(i)
                
            p.append(s)
            
        return p

    # 1920. Build Array from Permutation [EASY] 
    def build_array(self, nums: List[int]) -> List[int]:
        lst = [nums[i] for i in nums]
        return lst
        
