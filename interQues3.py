def palindrome(str_var):
    if str_var==str_var[::-1]:
        return True
    else:
        return False
varstr=input("Enter String")
if palindrome(varstr)==True:
    print("String is Palindrome")
else:
    print("String is not Palindrome")