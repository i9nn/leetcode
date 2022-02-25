/*
    My Java solutions to the LeetCode Java exercises. 
    Feel free to poke around.

    Exercises finished: 10
*/

class Solution {
    
    // 1. Two Sum
    public int[] twoSum(int[] nums, int target) {
        for (var i = 0; i < nums.length; i++) { 
            for (var j = 0; j < nums.length; j++) { 
                if (nums[i] + nums[j] == target && i != j) {
                    int[] sum = {i, j};
                    return sum; 
                }
            }
		}
        return nums;
    }

    // 771. Jewels and Stones
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0; 
        for (int i = 0; i < jewels.length(); i++) {
            for (int j = 0; j < stones.length(); j++) { 
                if (jewels.charAt(i) == stones.charAt(j)) {
                    count++;
                }
            }
        }
        
        return count; 
    }

    // 1108. Defanging an IP Address
    public String defangIPaddr(String address) {
        String defanged = "";
        
        for (int i = 0; i < address.length(); i++) { 
            if (Character.isDigit(address.charAt(i))) {
                defanged += address.charAt(i);
            } else { 
                defanged += "[.]";
            }
        } 
        
        return defanged; 
    }

	// 1365. How Many Numbers Are Smaller Than the Current Number
	public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] smallers = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) { 
            for (int j = 0; j < nums.length; j++) { 
                if (nums[j] < nums[i]) { 
                    smallers[i]++;
                }
            }   
        }
        
        return smallers; 
    }

    // 1480. Running Sum of 1d Array
    public int[] runningSum(int[] nums) {
        int[] running = new int[nums.length];
        running[0] = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            running[i] = running[i - 1] + nums[i];
        }
        
        return running; 
    }

    // 1672. Richest Customer Wealth
    public int maximumWealth(int[][] accounts) {
        int richest = 0;
        
        for (int i = 0; i < accounts.length; i++) {
            int wealth = 0; 

            for (int j = 0; j < accounts[i].length; j++) {
                wealth += accounts[i][j]; 
            }
            
            if (wealth > richest) {
                richest = wealth; 
            }
        }
        
        return richest; 
    }

    // 1920. Build Array from Permutation
    public int[] buildArray(int[] nums) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            ans[i] = nums[nums[i]];
        }
        
        return ans; 
    }

    // 1929. Concatenation of Array
    public int[] getConcatenation(int[] nums) {
        int[] concat = new int[nums.length * 2];
        for (int i = 0; i < nums.length; i++){
            concat[i] = nums[i];
            concat[i + nums.length] = nums[i];
        }
        
        return concat;
    }

    // 2011. Final Value of Variable After Performing Operations
    public int finalValueAfterOperations(String[] operations) {
        int x = 0; 
        
        for (int i = 0; i < operations.length; i++) {
            if (operations[i].contains("--")) {
                x--; 
            } else {
                x++;
            }
        }
        
        return x; 
    }

	// 2114. Maximum Number of Words Found in Sentences
    public int mostWordsFound(String[] sentences) {
        int words = 0; 
        
        for (int s = 0; s < sentences.length; s++) {
            String str = sentences[s];
            int spaces = 0; 
            
            for (int i = 0; i < str.length(); i++) { 
                if (Character.isWhitespace(str.charAt(i))) { 
                    spaces++;
                }
            }
            spaces++;
                
            if (spaces > words) { 
                words = spaces; 
            }
        }

        return words; 
    }
}