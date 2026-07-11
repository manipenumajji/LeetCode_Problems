class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    x.append(nums1[i])
        k=list(set(x))
        return k        
        
nums1=[1,2,2,1]
nums2=[2,2]
s=Solution()
res=s.intersection(nums1,nums2)
print(res)                 

        