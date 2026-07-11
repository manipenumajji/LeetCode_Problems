class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=list(set(nums1))
        y=list(set(nums2))
        m=[]
        for i in (x):
            if i in y:
                m.append(i)
        return m        
        
nums1=[1,2,2,1]
nums2=[2,2]
s=Solution()
res=s.intersection(nums1,nums2)
print(res)                 

        