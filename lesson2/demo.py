# %%
 
sentence = input("Enter a sentence: ")
words = sentence.split()
acronym = "".join(word[0].upper() for word in words)
print("Acronym:", acronym)
# %%

#14. **Check for Empty List**: Determine if a list is empty and return a boolean.
is_empty = len(user_list) == 0
print("Is the list empty?", is_empty)
# %%
