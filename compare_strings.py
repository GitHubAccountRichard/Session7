s1 = "banana"
s2 = "banana"
print(s1 == s2)
s2 = "banana"
print(s1 == s2)
s1 = "Banana"
print(s1 == s2)
print(s1 > s2) #True because b > B, lowercase characters are considered greater than capital characters
s1 = "banana"
s2 = "banany"
print(s1 > s2) #False because a is not greater than y

# in operator can be used for strings !
s1 = "I went to see Jane"
s2 = "went"
print(s2 in s1) #True
print("ana" in "banana") #True
print("ANA" in "banana") #False
