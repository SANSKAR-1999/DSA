
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        seen = set(nums2)  
        
        for num in nums1:
            if num in seen:
                result.append(num)
                seen.remove(num)  
        
        return result