'''
TASK 7: String Processing & Traversal 
Concepts: Strings, Indexing, Iteration 
Analyze a user-entered sentence: 
● Count vowels, consonants, digits, spaces 
● Convert case and remove extra spaces 

'''
message = input("Enter your message: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
space =" "
vowel_count = 0
consonant_count = 0
space_count = 0
for char in message:
    if char in vowels:
        vowel_count += 1
    elif char == space:
        space_count += 1
    else:
        consonant_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Spaces: {space_count}") 

# Convert case and remove extra spaces
converted_message = ' '.join(message.split()).swapcase()
print("Converted Message:", converted_message)
