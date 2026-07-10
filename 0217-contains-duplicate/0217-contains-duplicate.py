class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False    
              


nums=[1,2,3,1]
s=Solution()
res=s.containsDuplicate(nums)
print(res)        
        