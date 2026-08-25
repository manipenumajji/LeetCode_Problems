class Solution:
    def topKFrequent(self, nums,k):
        seen={}
        x=[]
        for i in (nums):
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        sorted_nums=sorted(seen,key=seen.get,reverse=True)
        return sorted_nums[:k]
nums=[1,1,1,2,2,3]
k=2
s=Solution()
res=s.topKFrequent(nums,k)
print(res)                

        