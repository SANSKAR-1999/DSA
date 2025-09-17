class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                number = num
            if num == number:
                count += 1
            else:
                count -= 1
        return number