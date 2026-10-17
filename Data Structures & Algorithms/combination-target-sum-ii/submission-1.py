class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        def backtrack(path, s, idx):
            if s == target:
                results.append(path[:])
            elif s > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(path, s=s+candidates[i], idx=i+1)
                path.pop()
        backtrack([],0,0)
        return results