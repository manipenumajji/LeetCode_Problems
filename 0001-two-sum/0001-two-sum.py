class Solution:
    def twoSum(self, nums,target): 
        original_index=[]
        for index,num in enumerate(nums):
            original_index.append((num,index))
            original_index.sort()
            p1,p2=0,len(original_index)-1
            while p1<p2:
                if original_index[p1][0]+original_index[p2][0]==target:
                    return original_index[p1][1],original_index[p2][1]
                elif original_index[p1][0]+original_index[p2][0]> target:
                    p2-=1
                else:
                    p1+=1       
nums=[2,7,11,15]
target=9
s=Solution()
res=s.twoSum(nums,target)
print(res)        