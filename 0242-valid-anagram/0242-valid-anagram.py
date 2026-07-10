class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        freq={}
        for i in s:
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        for j in t:
            if j not in freq:
                freq[j]=1
            else:
                freq[j]+=1
        if seen==freq:
            return True
        else:
            return False                

                   
s="anagram"
t="nagaram"
S=Solution()
res=S.isAnagram(s,t)
print(res)        
        