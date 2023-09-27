#Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Solution :

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for right in range(1,len(nums)) :
            if nums[right] == nums[right-1]:
                continue
            else :
                nums[k] = nums[right]
                k+=1
        return k