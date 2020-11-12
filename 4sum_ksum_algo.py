def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def twoSum(nums, target):
        lo, hi = 0, len(nums) - 1
        res = []
        while lo < hi:
            if nums[lo] + nums[hi] == target:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            elif nums[lo] + nums[hi] < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif nums[lo] + nums[hi] > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
        return res
        
    def kSum(nums, target, k):
        res = []
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
             if i == 0 or nums[i - 1] != nums[i]:
                    for newset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        newset_full = [nums[i]] + newset
                        if newset_full not in res:
                            res.append(newset_full)
                    
        return res
    nums.sort()
    return kSum(nums, target,4)
