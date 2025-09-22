class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
   
        box = set()
        for i in range(len(nums)):
            if nums[i] in box:
                return True
            box.add(nums[i])
            if i >= k:
                box.remove(nums[i - k])
        return False
        