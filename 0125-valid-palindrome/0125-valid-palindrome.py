class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        x=""
        for i in range(len(s)):
            assci=ord(s[i])
            if (97<=assci<=122) or 48<=assci<=57 :
                x+=chr(assci)
        if x==x[::-1]:
            return True
        else:
            return False         

s="Race A Car" 
S=Solution()
res=S.isPalindrome(s)
print(res)
       
        