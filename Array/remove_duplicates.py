class solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0, nums
        
        unique_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_index] = nums[i]
                unique_index += 1
                
        return unique_index, nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = solution()
k, modified_nums = s.removeDuplicates(nums)
print(k)
print(modified_nums[:k])
