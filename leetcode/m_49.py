class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:       
        d = defaultdict(list)
        
        for s in strs:
            alpha = "".join(sorted(s))
            d[alpha].append(s)
        res = list(d.values())
        # print(res)
        
        return res
