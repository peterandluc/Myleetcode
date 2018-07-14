class Solution:
    """
    This is not good problem. The idea is use hash dict to store position and use O(1) to search.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[target - nums[i]] = i
