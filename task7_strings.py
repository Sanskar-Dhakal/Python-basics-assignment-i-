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

'''
Reasoning Questions
1. Why is string processing critical in cybersecurity and NLP? 
=> String processing is important because computers mostly work with text. 
In cybersecurity, it helps find harmful messages, fake links, and suspicious activity. 
In NLP, it helps computers understand human language, such as in chatbots and translators. 
Without string processing, computers cannot read or understand text properly.
2. How can improper string handling introduce vulnerabilities? 
=> If strings are not handled properly, hackers can take advantage of them. 
For example, they can enter harmful code instead of normal text. 
This can damage the system, steal information, or give unauthorized access. 
Also, very long input can crash a program if limits are not set.
'''