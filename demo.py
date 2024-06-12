#  Write a Python program to sum all the items in a list.
list_item = [1,2,3,4,5]
sum = 0
for element in list_item:
    sum = sum+element
print(sum)

#  Write a Python program to multiply all the items in a list
mult_item = [1,2,3,4,5]
multiply = 1
for element in mult_item:
    multiply=multiply*element
print(multiply)

# Write a Python program to get the largest number from a list.
list_number = [1,2,3,4]
max_no = list_number[0]
for element in list_number:
    if element>max_no:
        max_no = element
print(max_no)

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221',"abca"]
# Expected Result : 2
Sample_List =['abc', 'xyz', 'aba', '1221',"abca","11","a"]
count_no = 0
for element in Sample_List:
    if len(element)>=2 and element[0]==element[-1]:
        count_no = count_no+1
print(count_no)

# . Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
Sample_list =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def get_element(lst):
    return lst[-1]

def demo(sample_list):
    return sorted(sample_list,key=get_element)

print(demo(Sample_list))

# 7. Write a Python program to remove duplicates from a list
ls = [1,2,3,4,5,6,4,5]
print(set(ls))
l = []
for i in ls:
    if i not in l:
        l.append(i)
print(l)

# 8. Write a Python program to check if a list is empty or not.
l1 = []
if len(l1)==0:
    print("empty")
else:
    print("not empty")

# Write a Python program to clone or copy a list.# 
l1 = [1,2,3,4,5,6]
l2=[]
l2 = l1
# l2 = l1.copy()
print(l2)
print(l1)

#  Write a Python program to find the list of words that are longer than n from a given list of words.
# lss = ['dvf','fvfv','ttgvv','fvv','fvfvtv']
# # n = int(input("enter number"))
# e = []
# for i in lss:
#     if len(i)>n:
#         e.append(i)
# print(e)

# 11. Wr9ite a Python function that takes two lists and returns True if they have at least one common member.
def func(l1,l2):
    for i in l1:
        if i in l2:
            print("True")
            break
    
l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9,1]
func(l1,l2)

#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
Sample_ist = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Sample_ist.pop(0)
Sample_ist.pop(3)
Sample_ist.pop()
print(Sample_ist)  