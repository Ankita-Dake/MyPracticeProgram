# 1: Write a Python program to check if a set a subset of another set
set_first = {1,2,3,4}
set_second = {1,2,3}
print(set_second.issubset(set_first))

# 2: Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. 
# Use the Python set data type.
list_string = ['python','java','c','php','java','python','dotnet','reactjs']
print("original string...",list_string)
unique_string = list(set(list_string))
print("list of unique string...",unique_string)

#3: Write a Python program to find the union, symmetric difference, and intersection of the two sets.
#  Print the results of each operation.
set_one = {1,2,3,4,5,6,7,8,9}
set_two = {3,1,5,3,7,5,8}
union_set = set_one.union(set_two)
print("union of two set...",union_set)
intersection_set = set_one.intersection(set_two)
print("intersection of two set...",intersection_set)
symmetric_difference = set_one.symmetric_difference(set_two)
print("symmetric_differenceof two set...",symmetric_difference)

# 4: Write a Python program to create a symmetric difference.
set_one = {'java','python','c'}
set_two = {"java",'dotnet','python','c#','c++'}
symmetric_difference = set_one.symmetric_difference(set_two)
print("symmetric_differenceof two set...",symmetric_difference)

# 5: program to count number of vowels using sets in given string.
def count_vowel(set_string):
    count = 0
    vowels = set("aeiouAEIOU")
    for element in set_string:
        if element in vowels:
            count = count+1
    
    print("No. of vowels :", count)
set_string= "mynameis"
 
# Function Call
count_vowel(set_string)

sample_list = [                            # list[{{}}]
    {
        "School": {
            "Student1": {
                "Name": "Pravin",
                "Email": "Pravin@gmail.com",
                "Address" : "Pune"
            },
           
            "Student2": {
                "Name": "Vishal",
                "Email": "Vishal@gmail.com",
                "Address" : "Mumbai"
            }
        }
    },
   
    {
        "Office": {
            "Epmloyee1" : {
                "Name": "Pratik",
                "Email": "Pratik@gmail.com",
                "Address" : "Pune"
            },
           
            "Epmloyee2" : {
                "Name": "Kiran",
                "Email": "Kiran@gmail.com",
                "Address" : "Mumbai"
            },
           
        }
    }
]


print(sample_list[0]["School"]["Student1"]["Email"])