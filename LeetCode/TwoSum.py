class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    continue

test = Solution()
nums = [2,7,11,15]
target = 9
print(test.twoSum(nums, target))