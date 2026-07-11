class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=[]
        nums1.sort()
        nums2.sort()  
        p1=0
        p2=0
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]==nums2[p2]:
                m.append(nums1[p1])
                p1+=1
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1        

        return list(set(m))                                           
               
        
nums1=[1,2,2,1]
nums2=[2,2]
s=Solution()
res=s.intersection(nums1,nums2)
print(res)                 

        