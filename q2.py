# string1 = "12#4245"
# if string1.isdigit()== True:
#     print("True")
# else:
#     print("False")


# str1 = "Python"
# str2 = "django"
# s = str1[0]+str2[0]
# s1 = str1[2]+str2[2]
# s2 = str1[5]+str2[5]
# print(s+s1+s2)

# # Write a program to append new string in the middle of a given string
# given_string = input("enter the string")
# middle_len=int(len(given_string) / 2)
# append_string = "MYSTRING"
# print(given_string[:middle_len:]+append_string+given_string[middle_len:])

 # Write a program to arrange string characters such that lowercase letters should come first
string_char= "pyFASthTAonPI"
empty_string = ""
for lower_letter in string_char:
    if lower_letter.islower():
        empty_string=empty_string+lower_letter
for upper_letter in string_char:
    if upper_letter.isupper():
        empty_string=empty_string+upper_letter
print(empty_string)

# Write a program to Count all letters, digits, and special symbols from a given string.
# Total counts of chars, digits, and symbols

# Chars = 8

# Digits = 3

# Symbol = 4

string = "ankita1234@#$dake!"
letter = 0
digit = 0
symbol = 0
for i in string:
    if i.isdigit():
        # print(i)
        digit=digit+1
    elif i.isalpha():
        letter = letter+1
    else:
        symbol = symbol+1
print("Total counts of chars, digits, and symbols")
print("Chars =",letter)
print("Digit =",digit)
print("symbol =",symbol)

# Write a program to String characters balance Test
 
def String_character(string1,string2):
    cnt = 0
    for index in string1:
        if index in string2:
          cnt=cnt+1
    if cnt == len(string1):
       print(True)
    else:
        print(False)

string1 = "Fast"
string2 = "PythonFastAPI"
String_character(string1,string2)


# Write a program to count occurrences of all characters within a string
string1= "pythonpy"
dict = {}
for index in string1:
    if index in dict:
        dict[index]=dict[index]+1
    else:
        dict[index]=1
print(dict)

# 8: Write a program to find the last position of a substring in a given string.
string1 = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
substring = "chuck"
result = string1.rfind(substring)
print(result)

# # 9: Write a program to split a given string on hyphens and display each substring.
given_string = "Violet-Indigo-Blue-Green-Yellow-Orange-Red"
new_string = given_string.split("-")
print(new_string)

# Write a program to remove special symbols / punctuation from a string.
string1 = "Hello!, he said, -- I have $45 & you?"
new_string = ""
for letter in string1:
    if letter == " ":
        new_string = new_string+letter
    elif letter.isalpha() or letter.isdigit():
        new_string= new_string+letter

print(new_string)

# #  11: Write a Python class to reverse a string word by word.
str1 = "geeks quiz practice code"
class ReversedString():
    def reverse_words(self,s):
        split_string = s.split(" ")
        rev_split_string = split_string[::-1]
        join_str = " ".join(rev_split_string)

        return join_str
print("original string...=>",str1)
rev_object = ReversedString()
print("reverse string...=>",rev_object.reverse_words(str1))
        

# string1 = "Hello World"
# new_string = ""
 
# for letter in string1:
#     if letter not in new_string:
#         new_string = new_string + letter
 
# print("Old String is: ", string1)
# print("New String is: ", new_string)


# string1 = "Hello World"
# count = 0
 
# while count<len(string1):
#     count = count + 1
   
# print("Total count of string is:- ", count)

string1 = "Hello World"
reverse_string = string1[::-1]
count = 0
 
while count<len(reverse_string):
    count = count + 1
   
print("Total count of string is:- ", count)


str1 = "Python"
str2 = "Django"
 
def modify_string(string1, string2):
    new_string = ""
    new_string = new_string + string1[0] + string2[0]
     
    if len(string1)%2 == 0:
         new_string = new_string + string1[(len(string1)//2)-1]
    else:
        new_string = new_string + string1[(len(string1)//2)]
       
    if len(string2)%2 == 0:
         new_string = new_string + string2[(len(string2)//2)-1]
    else:
        new_string = new_string + string2[(len(string2)//2)]
       
    new_string = new_string + string1[-1] + string2[-1]
   
    return new_string
 
print(modify_string(str1, str2))