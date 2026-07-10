class Solution:
    def twoSum(self, nums,target): 
        seen={}
        for index,num in enumerate(nums):
            needed=target-num
            if needed in seen:
                return [seen[needed],index]
            seen[num]=index    
nums=[2,7,11,15]
target=9
s=Solution()
res=s.twoSum(nums,target)
print(res)        