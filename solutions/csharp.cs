/*
    My C# solutions to the LeetCode C# exercises. 
    Feel free to poke around.

    Exercises finished: 2
*/

public class Solution {
    
    // 1. Two Sum [EASY]
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++) { 
            for (int j = 0; j < nums.Length; j++) { 
                if (nums[i] + nums[j] == target && i != j) {
                    int[] sum = new int[2]; 
                    sum[0] = i;
                    sum[1] = j;
                    
                    return sum; 
                }
            }
        }
        return nums;
    }
    
    // 1960. Build Array from Permutation [EASY]
    public int[] BuildArray(int[] nums) {
        int[] ans = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++){
            ans[i] = nums[nums[i]];
        }
        
        return ans; 
    }
}
