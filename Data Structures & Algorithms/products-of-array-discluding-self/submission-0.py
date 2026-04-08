class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    continue 
                output[i] *= nums[j]
        return output