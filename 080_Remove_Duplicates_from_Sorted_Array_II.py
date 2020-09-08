'''

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        left = 0
        cur = 0
        while cur < length - 1:
            sums = 1
            while cur < length - 1 and nums[cur] == nums[cur + 1]:
                sums += 1
                cur += 1
            for i in range(min(sums, 2)):
                nums[left] = nums[cur]
                left += 1
            cur += 1
        if cur == length - 1:
            nums[left] = nums[cur]
            left += 1
        #nums = nums[:left + 1]
        return left
