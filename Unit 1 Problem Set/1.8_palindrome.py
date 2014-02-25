###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.


word = "madam"
is_palindrome = word.find(word[::-1]) #initialize is_palindrome to invoke find on word, passing in word read backwards
print is_palindrome

>>>0

# test case 2
word = "madman" # uncomment this to test
is_palindrome = word.find(word[::-1])
print is_palindrome
>>-1



