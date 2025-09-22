class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:  # Handle empty list
            return []
        
        result = []
        start = nums[0]  # Start of the current range
        
        for i in range(len(nums)):
            # If at the last number or next number isn't consecutive
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                # If start and end are the same, add single number
                if start == nums[i]:
                    result.append(str(start))
                # Otherwise, add range as "start->end"
                else:
                    result.append(f"{start}->{nums[i]}")
                # If not at the end, start new range with next number
                if i < len(nums) - 1:
                    start = nums[i + 1]
        
        return result