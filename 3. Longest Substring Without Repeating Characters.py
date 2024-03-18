class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        start = 0

        #record appeared string
        char_index = {}

        for end in range(n):
            #add the start if char already in dict and the start is smaller than the indices
            if s[end] in char_index and start <= char_index[s[end]]:
                start = char_index[s[end]] + 1
            else:
                #use the current index to minus the start to get the length
                max_length = max(max_length, end - start + 1)
            #record it
            char_index[s[end]] = end

        return max_length
        


        
