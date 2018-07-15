class Solution:
    """
    python cheating, O(nlogn)
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        a = m + n
        l = sorted(nums1 + nums2)
        c = int(a/2)
        if a % 2 == 1:
            return l[c]*1.0
        else:
            return (l[c-1] + l[c])/2.0
