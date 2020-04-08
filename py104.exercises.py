#Small Exercise: user enters string, print the vowels of string. Upper & Lowercase should be handled

# user_string = input('Enter a word or sentence: ')
# #string_indexes = range(len(user_string))
# vowels_array = ['a', 'e', 'i', 'o', 'u']
# #vowels_indexes = range(len(vowels_array))

# for i in range(len(user_string)):
#     for x in range(len(vowels_array)):
#         if user_string[i] == vowels_array[x]:
#             print(vowels_array[x])

#SMALL EXERCISE COMPLETE


#Medium Exercise: Prompt user for startup name, generate name by removing the last vowel that comes before a non-vowel
#ex. Bacon = Bacn, Shrubbery = Shrubbry

user_entry = input('Enter the name of your start-up: ')
vowels_array2 = ['a', 'e', 'i', 'o', 'u']
vowels_indexes = range(len(vowels_array2))

answer = ''
#iterate through the user's entry
for y in user_entry:
    #iterates through the vowels array
    for x in vowels_array2:
        if x == y:
            #.rsplit() removes last instance
            #var answer changes value as the loop iterates
            answer = user_entry.rsplit(x, 1)
#joins the 2 strings
answer = ''.join(answer)
print(answer)

       
        



