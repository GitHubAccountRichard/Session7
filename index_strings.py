s1 = "Hello World!"
print(s1)
print(s1[0], s1[1], s1[2])
print(s1[4], s1[7]) #print both o's
print(s1[11], s1[-1]) # print the last one
print(s1[14//2])
s1 = "hello"
s2 = "world"
print(s1+ " " + s2)

# If operations

if ("bob"): # bob is True!
    print("bob is")
else:
    print("bob is not")


if (""): # bob is True!
    print("empty string is True")
else:
    print("empty string is False")


s ="abcdefghijklmnop"
print(len(s))
# we can iterate over a string and we can get each character !
for character in s:
    print(character, end=" ")


#Same thing using a while loop
counting = 0
length = len(s)
while counting < length:
    print(s[counting], end = " ")
    counting += 1
    if counting == length:
      break
print()


i = 0
while i < len(s):
   print(s[len(s) - i -1], end = " ")
   i += 1

# slide is a fancy index
s= "0123456789"

#first number is included last number is excluded
print(s)
print(s[2:3]) #2
print(s[4:6]) #45
print(s[:3]) #012
print(s[3:]) #3456789
print(s[1:7:2]) # 135
print(s[::-1]) #beginning to end
print(s[::-2]) # reverse string in steps of two