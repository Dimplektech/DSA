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


class solutions:
    def twosum(self, num: list[int], target: int) -> list[int]:

        for i in range(len(num) - 1):

            for j in range(i + 1, len(num)):

                if num[i] + num[j] == target:
                    return [i, j]

        return []


solve_prob = solutions()
num_list = [2, 7, 11, 15]
target = 18
output = solve_prob.twosum(num_list, target)
print(output)
