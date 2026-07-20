class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}

        for i, word in enumerate(strs):
            sortWord = ''.join(sorted(word))
            if sortWord not in groups:
                groups[sortWord] = []
            groups[sortWord].append(word)

        for k,v in groups.items():
            row = []
            for w in v:
                row.append(w)
            res.append(row)    
    
        return res
            