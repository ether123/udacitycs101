###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
# Replace the first occurrence of marker in the line below.

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

#Example 2 # uncomment this to test with different input
#marker = "EY"
#replacement = "Eyjafjallajokull"
#line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."


pos = line.find(marker) #initialize variable pos to the result of invoking find on line, passing in the variable marker
first_part = line[:pos] #initialize first_part to the result of the subsequence of line, from the beginning of the string to pos
last_part = line[pos+len(marker):]  #initialize last_part to the result of subsequence of line, from after the marker to end of line
replaced = first_part + replacement + last_part  #initialize replaced to be the concatenation of previously defined variables
print replaced
    
    

# Example 1 output:
>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.