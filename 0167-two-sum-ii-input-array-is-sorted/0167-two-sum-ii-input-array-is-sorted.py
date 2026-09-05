class Solution:
    def twoSum(self, numbers, target):
        p1,p2=0,len(numbers)-1
        while p1<=p2:
            if numbers[p1]+numbers[p2]==target:
                return p1+1,p2+1
            elif numbers[p1]+numbers[p2]<target:
                p1+=1
            else:
                p2-=1
numbers=[2,7,11,15]
target=9
s=Solution()
res=s.twoSum(numbers,target)
print(res)                        
        