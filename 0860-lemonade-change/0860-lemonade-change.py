class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # make count dict to count number of 5 and 10 
        count={5:0,10:0}
        for bill in bills:
            if bill==5:
                count[5]+=1
            elif bill==10:
                count[10]+=1
                if(count[5]>0):
                    count[5]-=1
                else:
                    return False
            else:
                if count[5]>0 and count[10]>0:
                    count[5]-=1
                    count[10]-=1
                elif count[5]>=3:
                    count[5]-=3
                else:
                    return False
        return True 
                    
        