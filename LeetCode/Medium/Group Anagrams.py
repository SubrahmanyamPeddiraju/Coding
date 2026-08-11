class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False]*len(strs)
        result = []
        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True
            for j in range(i+1, len(strs)):
                if visited[j]:
                    continue
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            result.append(group)
        return result       
