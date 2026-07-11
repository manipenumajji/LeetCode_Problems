class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen={}
        freq={}
        m=[]
        for i in nums1:
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        for j in nums2:
            if j not in freq:
                freq[j]=1
            else:
                freq[j]+=1
        for i in seen:
            if i in freq:
                m.append(i)
        return m                               
               
        
nums1=[1,2,2,1]
nums2=[2,2]
s=Solution()
res=s.intersection(nums1,nums2)
print(res)                 

        