class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heappush(self.heap,val) if len(self.heap) < self.k else heappushpop(self.heap, val)
        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)