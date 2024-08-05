class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result=[]
        for i in arr:
            if arr.count(i)==1:
                result.append(i)
        if len(result)<k:
            return ""
        else:
            return result[k-1]
        