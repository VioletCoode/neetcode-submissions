class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} #VALUE:INDEX

        for i, n in enumerate(nums):#i gives the index and n gives the number 
        #for i in range(len(nums)):
            #n = nums[i]
            diff=target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n]=i
        return

        
