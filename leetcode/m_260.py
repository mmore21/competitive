class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = defaultdict(int)
        
        for n in nums:
            seen[n] += 1
        
        smallest = [k for k, v in seen.items() if v == 1]
        return smallest
