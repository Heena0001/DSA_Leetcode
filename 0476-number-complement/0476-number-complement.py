class Solution:
    def findComplement(self, num: int) -> int:
        ans=[]
        a=bin(num)[2:]
        for i in a:
            if i=='1':
                ans.append('0')
            else:
                ans.append('1')
        a="".join(ans)
        return int(a,2)
        
        