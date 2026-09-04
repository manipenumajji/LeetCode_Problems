class Solution:
    def merge(self, nums1,m,nums2,n):
        elements=[]
        for i in range(m):
            elements.append(nums1[i])
        for j in range(n):
            elements.append(nums2[j])
        elements=sorted(elements)
        for i in range(m+n):
            nums1[i]=elements[i]
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
s=Solution()
res=s.merge(nums1,m,nums2,n)  
print(res)              


       
        