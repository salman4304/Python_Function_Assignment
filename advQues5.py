# # Write a function that takes a list and removes all duplicate elements.
def distinct_element(input_list):
    length = len(input_list)
    for i in range(length):
        # Compare current element with all subsequent elements
        j = i + 1
        while j < length:
            if input_list[i] == input_list[j]:
                # Remove the duplicate by shifting the elements left
                input_list.pop(j)
                length -= 1  # Decrease the length since we've removed an element
            else:
                j += 1  # Only increment j if no duplicate is found
    return input_list

numbers=[]
total_numbers=int(input("Enter how many numbers do you to want enter"))
for x in range(total_numbers):
    number=int(input("Please Enter Number"))
    numbers.append(number)
print("List of Unique Elements",distinct_element(numbers))