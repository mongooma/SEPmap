# snippet 1 https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
import re
DATA = "Hey, you - what are you doing here!?"
print re.findall(r"[\w']+", DATA)
# Prints ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']



# snippet 2: https://stackoverflow.com/questions/21209024/python-regex-remove-all-punctuation-except-hyphen-for-unicode-string
# works in python 2 and 3
import re
import string

remove = string.punctuation
remove = remove.replace("-", "") # don't remove hyphens
pattern = r"[{}]".format(remove) # create the pattern

txt = ")*^%{}[]thi's - is - @@#!a !%%!!%- test."
re.sub(pattern, "", txt) 
# >>> 'this - is - a - test'



