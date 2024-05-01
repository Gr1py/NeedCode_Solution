# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

s = "abc"
t = "ahbgdc"
#True output

s_ptr = 0
t_ptr = 0
    
while s_ptr < len(s) and t_ptr < len(t):
    if s[s_ptr] == t[t_ptr]:
        s_ptr += 1
        t_ptr += 1
    
print (s_ptr == len(s))