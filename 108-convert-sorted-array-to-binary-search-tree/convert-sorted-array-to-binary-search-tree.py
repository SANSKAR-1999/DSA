class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root
        
        return buildBST(0, len(nums) - 1)