class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = [[] for _ in range(len(nums)+1)]
        cHash = Counter(nums)
        for num, occur in cHash.items():
            print(num, occur)
            count[occur].append(num)

        for i in range(len(count)-1, -1, -1):
            if len(count[i]) > 0:
                for j in count[i]:
                    if k == 0:
                        return res
                    res.append(j)
                    k-=1
        return res
            