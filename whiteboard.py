# Remove vowels
# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:
# Input: ‘Joel’
# Output: ‘Jl’
# Input: ‘Shoha’
# Output: ‘Shh’

str1 = 'Joel'
str2 = 'Shoha'

def removeVowels(str):
    print("".join([char for char in str if char not in "aeiouAEIOU"]))
removeVowels(str1)
removeVowels(str2)

