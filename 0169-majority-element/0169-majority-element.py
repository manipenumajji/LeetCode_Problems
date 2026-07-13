class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1
            if seen[nums[i]]>len(nums)//2:
                return nums[i]            
            
            
nums=[3,2,3]
s=Solution()
res=s.majorityElement(nums)              


        