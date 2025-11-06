
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)  # Initialize with n (length of array)
        for i in range(len(nums)):
            result ^= i      # XOR with index
            result ^= nums[i]  # XOR with number
        return result
