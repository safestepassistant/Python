### List Tasks

#1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
from timeit import repeat

user_list = input("Enter list elements separated by space: ").split()
element = input("Enter the element to count: ")
count = user_list.count(element)
print(f"The element '{element}' appears {count} time(s) in the list.")

#2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
numbers = input("Enter numbers separated by space: ").split()
numbers = [float(num) for num in numbers]
total = sum(numbers) 
print("Sum of elements:", total)

#3. **Max Element**: From a given list, determine the largest element.
max_element = max(numbers)
print("Maximum element:", max_element)

#4. **Min Element**: From a given list, determine the smallest element.
min_element = min(numbers)
print("Minimum element:", min_element)
  
#5. **Check Element**: Given a list and an element, check if the element is present in the list.
check_element = input("Enter the element to check: ")
if check_element in user_list:
    print(f"The element '{check_element}' is present in the list.")
else:
    print(f"The element '{check_element}' is not present in the list.")

#6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
if user_list:
    first_element = user_list[0]
    print("First element:", first_element)

#7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
if user_list:
    last_element = user_list[-1]
    print("Last element:", last_element)

#8. **Slice List**: Create a new list that contains only the first three elements of the original list.
sliced_list = user_list[:3]
print("Sliced list (first three elements):", sliced_list)

#9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
reversed_list = user_list[::-1]
print("Reversed list:", reversed_list)

#10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
sorted_list = sorted(user_list)
print("Sorted list:", sorted_list)

#11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
unique_list = list(set(user_list))
print("List with unique elements:", unique_list)

#12. **Insert Element**: Given a list and an element, insert the element at a specified index.  
index = int(input("Enter the index to insert the element at: "))
new_element = input("Enter the element to insert: ")
user_list.insert(index, new_element)
print("List after insertion:", user_list)

#13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
try:
    element_index = user_list.index(check_element)
    print(f"The index of the first occurrence of '{check_element}' is: {element_index}")
except ValueError:
    print(f"The element '{check_element}' is not found in the list.")
 

#15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
even_count = sum(1 for num in numbers if int(num) % 2 == 0)
print("Count of even numbers:", even_count)

#16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
odd_count = sum(1 for num in numbers if int(num) % 2 != 0)
print("Count of odd numbers:", odd_count)

#17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.    
second_list = input("Enter elements of the second list separated by space: ").split()
concatenated_list = user_list + second_list
print("Concatenated list:", concatenated_list)

#18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
sublist = input("Enter elements of the sublist separated by space: ").split()
user_list = input("Enter elements of the main list separated by space: ").split()
def is_sublist(main_list, sub_list):
    sub_len = len(sub_list)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i + sub_len] == sub_list:
            return True
    return False
if is_sublist(user_list, sublist):
    print("The sublist exists within the list.")

#19. **Replace Element**: Given a list, replace the first    occurrence of a specified element with another element.
old_element = input("Enter the element to replace: ")
new_element = input("Enter the new element: ")
try:
    index_to_replace = user_list.index(old_element)
    user_list[index_to_replace] = new_element
    print("List after replacement:", user_list)
except ValueError:
    print(f"The element '{old_element}' is not found in the list.")

#20. **Find Second Largest**: From a given list, find the second largest element.
unique_numbers = list(set(numbers))
if len(unique_numbers) >= 2:
    unique_numbers.sort()
    second_largest = unique_numbers[-2]
    print("Second largest element:", second_largest)
else:
    print("Not enough unique elements to determine the second largest.")

#21. **Find Second Smallest**: From a given list, find the second smallest element.
if len(unique_numbers) >= 2:
    unique_numbers.sort()
    second_smallest = unique_numbers[1] 
    print("Second smallest element:", second_smallest)
else:
    print("Not enough unique elements to determine the second smallest.")

#22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
even_numbers = [num for num in numbers if int(num) % 2 == 0]
print("List of even numbers:", even_numbers)

#23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
odd_numbers = [num for num in numbers if int(num) % 2 != 0]
print("List of odd numbers:", odd_numbers)

#24. **List Length**: Determine the number of elements in the list.  
list_length = len(user_list)
print("Length of the list:", list_length)

#25. **Create a Copy**: Create a new list that is a copy of the original list.
copied_list = user_list.copy()
print("Copied list:", copied_list)

#26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
if user_list:
    mid_index = len(user_list) // 2
    if len(user_list) % 2 == 0:
        middle_elements = user_list[mid_index - 1:mid_index + 1]
        print("Middle elements (even length):", middle_elements)
    else:
        middle_element = user_list[mid_index]
        print("Middle element (odd length):", middle_element)

#27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
start_index = int(input("Enter the start index of the sublist: "))
end_index = int(input("Enter the end index of the sublist: "))
sublist = numbers[start_index:end_index]
if sublist:
    max_sublist = max(sublist)
    print("Maximum element of the sublist:", max_sublist)

#28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
if sublist:
    min_sublist = min(sublist)
    print("Minimum element of the sublist:", min_sublist)

#29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
remove_index = int(input("Enter the index of the element to remove: "))
if 0 <= remove_index < len(user_list):
    removed_element = user_list.pop(remove_index)
    print(f"Removed element '{removed_element}' from index {remove_index}.")
    print("List after removal:", user_list)

#30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
is_sorted = user_list == sorted(user_list)
print("Is the list sorted in ascending order?", is_sorted)

#31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
repeat_count = int(input("Enter the number of times to repeat each element: "))
repeated_list = [element for element in user_list for _ in range(repeat_count)]
print("List with repeated elements:", repeated_list)

#32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
merged_list = user_list + second_list
merged_sorted_list = sorted(merged_list)
print("Merged and sorted list:", merged_sorted_list)

#33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
all_indices = [index for index, value in enumerate(user_list) if value == check_element]
print(f"All indices of element '{check_element}':", all_indices)

#34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
rotation_count = int(input("Enter the number of positions to rotate the list: "))
rotated_list = user_list[-rotation_count:] + user_list[:-rotation_count]
print("Rotated list:", rotated_list)

#35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))
range_list = list(range(range_start, range_end + 1))
print("Range list:", range_list)

#36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
sum_positive = sum(num for num in numbers if num > 0)
print("Sum of positive numbers:", sum_positive)

#37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
sum_negative = sum(num for num in numbers if num < 0)
print("Sum of negative numbers:", sum_negative)

#38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
is_palindrome = user_list == user_list[::-1]
print("Is the list a palindrome?", is_palindrome)

#39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
n = int(input("Enter the number of elements per sublist: "))
nested_list = [user_list[i:i + n] for i in range(0, len(user_list), n)]
print("Nested list:", nested_list)

#40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
seen = set()
unique_ordered_list = []
for item in user_list:
    if item not in seen:
        seen.add(item)
        unique_ordered_list.append(item)
print("List with unique elements in original order:", unique_ordered_list)
####################################################################################################################
####################################################################################################################
####################################################################################################################

### Tuple Tasks

#1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
user_tuple = tuple(input("Enter tuple elements separated by space: ").split())
element = input("Enter the element to count: ")
count = user_tuple.count(element)
print(f"The element '{element}' appears {count} time(s) in the tuple.")

#2. **Max Element**: From a given tuple, determine the largest element.
max_element = max(user_tuple)
print("Maximum element:", max_element)

#3. **Min Element**: From a given tuple, determine the smallest element.
min_element = min(user_tuple)
print("Minimum element:", min_element)

#4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
check_element = input("Enter the element to check: ")
if check_element in user_tuple:
    print(f"The element '{check_element}' is present in the tuple.")
else:
    print(f"The element '{check_element}' is not present in the tuple.")

#5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
if user_tuple:
    first_element = user_tuple[0]
    print("First element:", first_element)

#6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
if user_tuple:
    last_element = user_tuple[-1]
    print("Last element:", last_element)
    
#7. **Tuple Length**: Determine the number of elements in the tuple.
tuple_length = len(user_tuple)
print("Tuple length:", tuple_length)

#8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
sliced_tuple = user_tuple[:3]
print("Sliced tuple (first three elements):", sliced_tuple)

#9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
second_tuple = tuple(input("Enter elements of the second tuple separated by space: ").split())
concatenated_tuple = user_tuple + second_tuple
print("Concatenated tuple:", concatenated_tuple)

#10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
is_empty = len(user_tuple) == 0
print("Is the tuple empty?", is_empty)
#11. **Find Second Largest**: From a given tuple, find the second largest element.
unique_elements = list(set(user_tuple))
if len(unique_elements) >= 2:
    unique_elements.sort()
    second_largest = unique_elements[-2]
    print("Second largest element:", second_largest)
else:
    print("Not enough unique elements to determine the second largest.")

#13. **Find Second Smallest**: From a given tuple, find the second smallest element.
if len(unique_elements) >= 2:
    unique_elements.sort()
    second_smallest = unique_elements[1]
    print("Second smallest element:", second_smallest)
else:
    print("Not enough unique elements to determine the second smallest.")

#14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
single_element = input("Enter the single element for the tuple: ")
single_element_tuple = (single_element,)
print("Single element tuple:", single_element_tuple)

#15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
list_to_convert = input("Enter list elements separated by space to convert to tuple: ").split()
converted_tuple = tuple(list_to_convert)
print("Converted tuple:", converted_tuple)

#16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
is_sorted = user_tuple == tuple(sorted(user_tuple))
print("Is the tuple sorted in ascending order?", is_sorted)

#17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
start_index = int(input("Enter the start index of the subtuple: "))
end_index = int(input("Enter the end index of the subtuple: "))
subtuple = user_tuple[start_index:end_index]
if subtuple:
    max_subtuple = max(subtuple)
    print("Maximum element of the subtuple:", max_subtuple)

#18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
if subtuple:
    min_subtuple = min(subtuple)
    print("Minimum element of the subtuple:", min_subtuple)
#19. **Repeat Tuple Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
repeat_count = int(input("Enter the number of times to repeat each element: "))
repeated_tuple = tuple(element for item in user_tuple for element in (item,)) * repeat_count
print("Tuple with repeated elements:", repeated_tuple)

#20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
n = int(input("Enter the number of elements per subtuple: "))
nested_tuple = tuple(user_tuple[i:i + n] for i in range(0, len
(user_tuple), n))
print("Nested tuple:", nested_tuple)

#21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
repeat_count = int(input("Enter the number of times to repeat each element: "))
repeated_tuple = tuple(element for item in user_tuple for element in (item,)) * repeat_count
print("Tuple with repeated elements:", repeated_tuple)

#22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))
range_tuple = tuple(range(range_start, range_end + 1))
print("Range tuple:", range_tuple)

#23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
reversed_tuple = user_tuple[::-1]
print("Reversed tuple:", reversed_tuple)

#24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
is_palindrome = user_tuple == user_tuple[::-1]
print("Is the tuple a palindrome?", is_palindrome)

#25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
seen = set()
unique_ordered_tuple = tuple(item for item in user_tuple if not (item in seen or seen.add(item)))
print("Tuple with unique elements in original order:", unique_ordered_tuple)
####################################################################################################################
####################################################################################################################
####################################################################################################################

### Set Tasks

#1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
set1 = set(input("Enter elements of the first set separated by space: ").split())
set2 = set(input("Enter elements of the second set separated by space: ").split())
union_set = set1.union(set2)
print("Union of sets:", union_set)

#2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

#3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)

#4. **Check Subset**: Given two sets, check if one set is a subset of the other.
is_subset = set1.issubset(set2)
print("Is the first set a subset of the second set?", is_subset)

#5. **Check Element**: Given a set and an element, check if the element exists in the set.
check_element = input("Enter the element to check: ")
if check_element in set1:
    print(f"The element '{check_element}' is present in the first set.")
else:
    print(f"The element '{check_element}' is not present in the first set.")

#6. **Set Length**: Determine the number of unique elements in a set.
set_length = len(set1)
print("Length of the first set:", set_length)

#7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
user_list = input("Enter list elements separated by space: ").split()
converted_set = set(user_list)
print("Converted set from list:", converted_set)

#8. **Remove Element**: Given a set and an element, remove the element if it exists.
remove_element = input("Enter the element to remove from the first set: ")
set1.discard(remove_element)
print("Set after removal:", set1)

#9. **Clear Set**: Create a new empty set from an existing set.
cleared_set = set1.clear()
print("Cleared set:", cleared_set)

#10. **Check if Set is Empty**: Determine if a set has any elements.
is_empty = len(set1) == 0
print("Is the first set empty?", is_empty)

#11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", symmetric_difference_set)

#12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
add_element = input("Enter the element to add to the first set: ")
set1.add(add_element)
print("Set after addition:", set1)

#13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
if set1:
    popped_element = set1.pop()
    print(f"Popped element: {popped_element}")
    print("Set after popping an element:", set1)

#14. **Find Maximum**: From a given set of numbers, find the maximum element.
max_element = max(map(float, set1))
print("Maximum element of the set:", max_element)

#15. **Find Minimum**: From a given set of numbers, find the minimum element.
min_element = min(map(float, set1))
print("Minimum element of the set:", min_element)

#16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
even_numbers_set = {num for num in map(int, set1) if num % 2 == 0}
print("Set of even numbers:", even_numbers_set)

#17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
odd_numbers_set = {num for num in map(int, set1) if num % 2 != 0}
print("Set of odd numbers:", odd_numbers_set)

#18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))
range_set = set(range(range_start, range_end + 1))
print("Range set:", range_set)

#19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
list1 = input("Enter elements of the first list separated by space: ").split()
list2 = input("Enter elements of the second list separated by space: ").split()
merged_deduplicated_set = set(list1 + list2)
print("Merged and deduplicated set:", merged_deduplicated_set)

#20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
are_disjoint = set1.isdisjoint(set2)
print("Are the two sets disjoint?", are_disjoint)

#21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
deduplicated_list = list(set(user_list))
print("List after removing duplicates:", deduplicated_list)

#22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
unique_count = len(set(user_list))
print("Count of unique elements in the list:", unique_count)

#23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.
import random
num_elements = int(input("Enter the number of random integers to generate: "))
random_set = {random.randint(1, 100) for _ in range(num_elements)}
print("Random set of integers:", random_set)
####################################################################################################################
####################################################################################################################
####################################################################################################################



### Dictionary Tasks

#1. **Get Value**: Given a dictionary and a key, retrieve the associated value, 
# considering what to return if the key doesn’t exist.
user_dict = {}
key = input("Enter the key to retrieve its value: ")
value = user_dict.get(key, "Key not found.")
print(f"Value for key '{key}':", value)
#2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
key_to_check = input("Enter the key to check: ")
if key_to_check in user_dict:
    print(f"The key '{key_to_check}' is present in the dictionary.") 
else:
    print(f"The key '{key_to_check}' is not present in the dictionary.")

#3. **Count Keys**: Determine the number of keys in the dictionary.
key_count = len(user_dict)
print("Number of keys in the dictionary:", key_count)

#4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
all_keys = list(user_dict.keys())
print("All keys in the dictionary:", all_keys)

#5. **Get All Values**: Create a list that contains all the values in the dictionary.
all_values = list(user_dict.values())
print("All values in the dictionary:", all_values)

#6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
second_dict = {}
merged_dict = {**user_dict, **second_dict}
print("Merged dictionary:", merged_dict)

#7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
key_to_remove = input("Enter the key to remove: ")
removed_value = user_dict.pop(key_to_remove, "Key not found.")
print(f"Removed value for key '{key_to_remove}':", removed_value)

#8. **Clear Dictionary**: Create a new empty dictionary.
cleared_dict = user_dict.clear()
print("Cleared dictionary:", cleared_dict)

#9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
is_empty = len(user_dict) == 0
print("Is the dictionary empty?", is_empty)

#10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
key_to_get = input("Enter the key to get its key-value pair: ")
if key_to_get in user_dict:
    key_value_pair = (key_to_get, user_dict[key_to_get])
    print(f"Key-value pair for key '{key_to_get}':", key_value_pair)
else:
    print(f"The key '{key_to_get}' is not found in the dictionary.")

#11. **Update Value**: Given a dictionary, update the value for a specified key.
key_to_update = input("Enter the key to update its value: ")
new_value = input("Enter the new value: ")
user_dict[key_to_update] = new_value
print(f"Updated dictionary:", user_dict)

#12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
value_to_count = input("Enter the value to count its occurrences: ")
value_occurrences = list(user_dict.values()).count(value_to_count)
print(f"The value '{value_to_count}' appears {value_occurrences} time(s) in the dictionary.")

#13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
inverted_dict = {value: key for key, value in user_dict.items()}
print("Inverted dictionary:", inverted_dict)

#14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
value_to_find = input("Enter the value to find its keys: ")
keys_with_value = [key for key, value in user_dict.items() if value == value_to_find]
print(f"Keys with value '{value_to_find}':", keys_with_value)

#15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
keys_list = input("Enter keys separated by space: ").split()
values_list = input("Enter values separated by space: ").split()
created_dict = dict(zip(keys_list, values_list))
print("Created dictionary from lists:", created_dict)

#16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
has_nested_dict = any(isinstance(value, dict) for value in user_dict.values())
print("Does the dictionary have nested dictionaries?", has_nested_dict)

#17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
nested_dict = {
    'outer_key': {
        'inner_key': 'inner_value'
    }
}
outer_key = input("Enter the outer key: ")
inner_key = input("Enter the inner key: ")
if outer_key in nested_dict and inner_key in nested_dict[outer_key]:
    nested_value = nested_dict[outer_key][inner_key]
    print(f"Value for '{outer_key} -> {inner_key}':", nested_value)
else:
    print("The specified keys do not exist in the nested dictionary.")

#18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
from collections import defaultdict
default_dict = defaultdict(lambda: "Default Value")
print("Default dictionary created. Accessing a missing key gives:", default_dict['missing_key'])

#19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
unique_values_count = len(set(user_dict.values()))
print("Number of unique values in the dictionary:", unique_values_count)

#20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
sorted_dict_by_key = dict(sorted(user_dict.items()))
print("Dictionary sorted by keys:", sorted_dict_by_key)

#21. **Sort Dictionary by Value**: Create a new dictionary sorted by values
sorted_dict_by_value = dict(sorted(user_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_dict_by_value)

#22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
threshold = input("Enter the threshold value: ")
filtered_dict = {key: value for key, value in user_dict.items() if value >= threshold}
print("Filtered dictionary by value:", filtered_dict)

#23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
common_keys = set(user_dict.keys()).intersection(set(second_dict.keys()))
print("Common keys between the two dictionaries:", common_keys)

#24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
tuple_of_pairs = (('key1', 'value1'), ('key2', 'value2'))
created_dict_from_tuple = dict(tuple_of_pairs)
print("Dictionary created from tuple of pairs:", created_dict_from_tuple)

#25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
if user_dict:
    first_key = next(iter(user_dict))
    first_key_value_pair = (first_key, user_dict[first_key])
    print("First key-value pair in the dictionary:", first_key_value_pair)
else:
    print("The dictionary is empty.")
    