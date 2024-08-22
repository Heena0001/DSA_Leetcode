class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # ans=[]
        # for i in nums1:
        #     if i in nums2 or i in nums3:
        #         if(i not in ans):
        #             ans.append(i)
        # for i in nums2:
        #     if i in nums3 :
        #         if(i not in ans):
        #             ans.append(i)
        # return ans
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        result = (set1 & set2) | (set2 & set3) | (set1 & set3)
        return list(result)