class Solution:

    def searchRange(self, nums, target):
        left = self.binSearch(nums. targert, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    # left bias = looking for left most index, right bias looking for ight most index
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
