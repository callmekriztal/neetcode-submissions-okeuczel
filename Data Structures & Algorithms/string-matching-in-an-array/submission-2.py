class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        all_substrings = set()
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j] :
                    all_substrings.add(words[i])
                elif words[j] in words[i]:
                    all_substrings.add(words[j])
        
        return list(all_substrings)