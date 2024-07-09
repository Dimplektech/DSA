"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""


class Solutions:
    def twosum(self, nums: list[int], target: int)->list[int]:
        num_map = {}  # Create a dictionary to store the indices of the number.
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return (num_map[complement], i)
            num_map[num] = i
        return []    
    

# Test Cases    
solve_prob = Solutions()    

nums = [2, 7, 11, 15]
target = 9
output = solve_prob.twosum(nums, target)
print(output)

nums2 = [3, 2, 4]
target2 = 6
output2 = solve_prob.twosum(nums2, target2)
print(output2)  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
output3 = solve_prob.twosum(nums3, target3)
print(output3)  # Output: [0, 1]
