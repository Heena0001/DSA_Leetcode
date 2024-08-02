class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        num_ones = nums.count(1)
        if num_ones == 0 or num_ones == len(nums):
            return 0
        new_array = nums + nums
        current_window = sum(new_array[:num_ones])
        max_ones = current_window
        for i in range(1, len(nums)):
            current_window = current_window - new_array[i - 1] + new_array[i + num_ones - 1]
            max_ones = max(max_ones, current_window)
        return num_ones - max_ones
                
        