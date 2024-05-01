#Valid Anagram

# s = "anagram", t = "nagaram"
# Output: true

s = sorted(s)
t = sorted(t)
if s == t:
    print (True)
print (False)
