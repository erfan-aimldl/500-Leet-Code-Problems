# Problem Link : https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for idx in range(len(nums)) :
            if nums[idx] != val :
                nums[k] = nums[idx]
                k+=1
        return k
