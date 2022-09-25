# Get the string
# get replace word and replacement
# change the string with replacement
import re


def replace_word():
    str = "hi this is the word replacer welcome to this playground. again and again hi hi hi"
    word_to_replace = input("Enter the word you want to replace : ")
    word_replacement = input("Enter the replacement word : ")
    print(re.sub(r'\b('+word_to_replace+')', word_replacement, str))

replace_word()

