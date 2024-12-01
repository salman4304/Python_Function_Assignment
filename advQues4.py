def anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
str1=input("Please Enter First string")
str2=input("Please Enter Second string")
if anagrams(str1,str2)==True:
    print("Strings are anagrams")
else:
    print("Strings are not anagram")
