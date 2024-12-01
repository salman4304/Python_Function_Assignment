def count_vowel(str_var):
    count=0
    for ch in str_var:
        if ch=='a' or ch=='i' or ch=='o' or ch=='e' or ch=='u':
            count=count+1
    return count
var=input("Please Enter String")
print(count_vowel(var))