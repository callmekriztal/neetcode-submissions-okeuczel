class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1,val1 in enumerate(numbers):
            for index2,val2 in enumerate(numbers):
                if val1+val2 == target:
                    return [index1+1,index2+1]
        return []