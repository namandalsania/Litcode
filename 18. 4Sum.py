class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()

        if nums is None or len(nums) < 0:
            return quadruplets

        nums.sort()
        n = len(nums)

        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif current_sum < target:
                        k += 1
                    
                    else:
                        l -= 1

        return quadruplets