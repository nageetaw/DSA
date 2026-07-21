class Solution(object):

    # Overall Time complexity O((m+n)log(m+n))  Space Complexity: O(1)
    # def merge(self, nums1, m, nums2, n):
    #     for j in range(n):  # Time complexity O(j) ,  Space Complexity: O(1)
    #         nums1[j+m] = nums2[j]
    #     nums1.sort()  # Time complexity O((m+n)log(m+n))

    # Optimized -> Two pointer
    def merge(self, nums1, m, nums2, n):
        # Time complexity: O(k) or O(m + n)
        # Space complexity: O(1)
        i, j, k = m-1, n-1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
