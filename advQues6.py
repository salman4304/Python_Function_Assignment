# Create a function that takes a string and counts the frequency of each character.
def frequency(string):
    freq = {}
    for chr in string:
        if chr in freq:
            freq[chr] = freq[chr] + 1
        else:
            freq[chr] = 1
    return freq

str_val=input("Please Enter String")
print(frequency(str_val))