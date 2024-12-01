# 6. Create a function that accepts a dictionary and returns the key with the highest value.
def highest_keyvalue(dic):
    if not dic:
        return None
    else:
        return max(dic,key=dic.get)

dictionary={"a":10,"b":20,"c":30,"d":40}
print(highest_keyvalue(dictionary))