# # 1: Write a Python Program to Interchange First and Last Elements of in a List
# list_element = [1,2,3,4,5,6]
# print("original list...",list_element)
# list_element[0] ,list_element[-1] =list_element[-1],list_element[0]
# print("Interchange First and Last Elements of in a List...",list_element)


# # 2: Write a Python Program to Remove Multiple Empty Strings from a List of Strings
# list_string = ["ankita"," ","dake","python"," "]
# print("original list of string...",list_string)
# for string in list_string:
#     if string==" ":
#         list_string.remove(string)
# print("After Removing Empty Strings...",list_string)

# # 3: Write a Python Program to Split a List in Half and Store the Elements in Two Different Lists
# list_element = [1,2,3,4,5,4]
# middle_len=int(len(list_element) / 2)
# print(middle_len)
# firt_half_list = list_element[:middle_len:]
# second_half_list = list_element[middle_len:]
# print("first half list...",firt_half_list)
# print("second half list...",second_half_list)

# # 4: Write a Python Program to Remove All Occurrences of an Element From a Given List
# given_list = [2,1,2,3,1,4,5,2,3,2]
# input_number =int(input("enter the number"))
# new_list = []
# for elemnt in given_list:
#     if elemnt!=input_number:
#         new_list.append(elemnt)
# print(new_list)

# # 5: Write a Python Program to Remove Negative Values From a List With Filter() Function
# element_list = [1,2,3,-1,-4,5,2,-5]
# print("original list")
# result = list(filter(lambda value:value>0,element_list))
# print("Remove all negative element",result)

# # 6: Write a Python program to count the number of strings where the string length is 2 or more and
# #  the first and last character are same from a given list of strings
# # # Sample Output
# # ['abc', 'xyz', 'aba', '1221']
# list1 =['abc', 'xyz', 'aba', '1221']
# print("original list..",list1)
# count = 0
# for element in list1:
#     if len(element)>=2 and element[0]==element[-1]:
#         count = count+1
# print("first and last character are same element..",count)

# #7:  Write a Python program to shuffle and print a specified list (shuffle)
# # Sample Output
# # ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# # ['Fox', 'Cat', 'Tiger', 'Lion', 'Dog', 'Ponda', 'Elephant']
# import random
# sample_list = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# random.shuffle(sample_list)
# print("The shuffled list is :",sample_list)

# #8: Write a program  to remove repetitive items from a list.
# list_item = [1,2,3,1,4,5,6]
# print(list(set(list_item)))

# covert nested list into flat list
# l = [1,2,3,[1,2,3],[2,3],"fxd"]
# flatlist = []
# for i in l:
#     if type(i) == list:
#         for j in i:
#             flatlist.append(j)
#     elif type(i)==str:
#          l.remove(i)
#     else:
#         flatlist.append(i)
   
# print(flatlist)

# Write a Python program to sum all the items in a list
# list_item = [1,2,3,4]
# sum = 0
# for index in list_item:
#     sum = sum+index
# print(sum)

#  Write a Python program to multiply all the items in a list
# list_items = [1,2,3,4]
# multipy = 1
# for index in list_items:
#     multipy = multipy*index
# print(multipy)

# . Write a Python program to get the largest number from a list.
# list_element = [1,2,3,4,99]
# max1 = list_element[0]
# for index in list_element:
#     if index>max1:
#         max1 = index
# print(max1)

#  Write a Python program to get the smallest number from a list.
# l1 = [1,2,3,-4,3]
# min_element = l1[0]
# for index in l1:
#     if index<min_element:
#         min_element = index
# print(min_element)

#  Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# l1 = ['abc', 'xyz', 'aba', '1221',"aaa"]
# count = 0
# for index in l1:
#     if len(index)>=2 and index[0]==index[-1]:
#         count = count+1
# print(count)

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


















list_data = [[1,2,3],[4,5,6],[7,8,9]]
even_no = [index for element in list_data for index in element if index%2==0]
print(even_no)
