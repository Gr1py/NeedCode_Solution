# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

s = "egg"
t = "add"

mapping = {}

for i in range(len(s)):
    if s[i] not in mapping:
        if t[i] not in mapping.values():
                 
            mapping[s[i]] = t[i]
        else: print (False) #return replaced by print
    elif mapping[s[i]] != t[i]:
        print (False) #return replaced by print
print (True)  #return replaced by print 