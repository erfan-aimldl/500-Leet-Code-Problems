# Problem Link : https://leetcode.com/problems/concatenation-of-array/

# Solution 1
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = ["_"] * len(nums) * 2

        for idx in range(len(ans)):
            ans[idx] = nums[idx % len(nums)]

        return ans

#Solution 2

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for n in range(2):
            for num in nums:
                ans.append(num)

        return ans
