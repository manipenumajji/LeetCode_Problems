class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1   
                if seen[nums[i]]>=2:
                    return True
        return False    

                
                     
nums=[1,2,3,1]
s=Solution()
res=s.containsDuplicate(nums)
print(res)        
        