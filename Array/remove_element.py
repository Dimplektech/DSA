""" Given an integer array nums and an integer val, remove all occurrences of 
val in nums in-place. The order of the elements may be changed. Then return 
the number of elements in nums which are not equal to val.
consider the number of elements in nums which are not equal to val be k,
 to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the 
elements which are not equal to val. The remaining elements of nums are not
important as well as the size of nums.
Return k.
"""


class Solution:
    # Two pointer approach
    def removeElement(self, nums:list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)
print(nums[:k])

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = solution.removeElement(nums, val)
print(k)
print(nums[:k])





