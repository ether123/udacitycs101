# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo" 
print text.find('hoo') 
#we invoke find on 'text' to find the first occurrence of 'hoo'. 

>>>6

text= "hi"
print text.find('hoo') 
>>>-1
