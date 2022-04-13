/*
    My JavaScript solutions to the LeetCode JavaScript exercises. 
    Feel free to poke around.

    Exercises finished: 1
*/

// 1. Two Sum [EASY]
var twoSum = function(nums, target) {
    for (var i = 0; i < nums.length; i++) { 
        for (var j = 0; j < nums.length; j++) { 
            if (nums[i] + nums[j] == target && i != j) {
                return [i, j]; 
            }
        }
    }
    
    return nums;
};