class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = []
        for i in nums1:
            nums.append(i)
        for i in nums2:
            nums.append(i)
        nums.sort()

        if len(nums) % 2 == 0:
            i = (len(nums) / 2) - 0.5
            i = int(i)
            j = i + 1
            return (nums[i] + nums[j]) / 2
        else:
            i = len(nums) / 2
            i = int(i)
            return nums[i]

        # for i in range(0, len(nums)):
        #     if i == j:
        #         return nums[i]
        #     elif len(nums) % 2 == 0 and i + 1 == j:
        #         return (nums[i] + nums[j]) / 2
        #     else:
        #         j -= 1


test = Solution()
nums1 = [1, 2]
nums2 = [3, 4, 5, 6, 7, 8, 9, 10]
print(test.findMedianSortedArrays(nums1, nums2))
