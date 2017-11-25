class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def check(nums1):
            ind = nums2.index(nums1) if (nums1 in nums2) else -1
            if ind<0 or ind==len(nums2)-1 :
                return -1
            else:
                for i in range(ind + 1, len(nums2)):
                    if nums1 < nums2[i] : return nums2[i]
                    else: continue
                return -1

        return list(map(check, nums1))
