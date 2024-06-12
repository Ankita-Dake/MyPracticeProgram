# # 1: Write a Python program merge two tuples and remove duplicates
# tuple1 = (1,2,3,4,5,3,2)
# tuple2 = (4,2,1,5,2,3,4)
# merge_tuple = tuple1+tuple2
# print("merge two tuples...",merge_tuple)
# print("remove duplicates...",tuple(set(merge_tuple)))

# #2: Write a Python program convert a tuple of integers to a tuple of strings.
# tuple_string = (1,2,3,4,5,6)
# new_list = []
# for element in tuple_string:
#     new_list.append(str(element))
# print(tuple(new_list))

# # 3: Write a Python program find the frequency of each element in a tuple.
# tuple_element = (1,2,3,4,5,6,2,3,1,3,4,5)
# dict = {}
# for index in tuple_element:
#     if index in dict:
#         dict[index]= dict[index]+1
#     else:
#         dict[index]=1
# print(" frequency of each element in a tuple...",dict)

# # 4:  Write a Python program find the difference between two tuples.
# tuple1 = (1,2,3,4,5,6)
# tuple2= (4,5,3,8,9,6,7)
# tuple3 = set(tuple1)^set(tuple2)
# print(tuple3)

# # 5: Write a Python program find the second largest element in a tuple
# tuple_element = (1,2,3,4,5,5,6,1)
# second_largest = sorted(tuple_element)
# print("tuple element are ...",second_largest)
# print("second largest element in a tuple...",second_largest[-2])

# #6:  Write a Python program check if a tuple is a subset of another tuple.
# tuple1 = (1,2,3,4,5)
# tuple2 = (1,2,3)
# subset_tuple = set(tuple2).issubset(set(tuple1))
# print(subset_tuple)

# 7: Write a Python program to Extract tuples having K digit elements.
# K = 2
# Original List :  [(47, 23), (3, 78), (22, 53), (121, 45), (7,)]
# Extracted Tuples :  [(47, 23), (22, 53)]
original_list = [(47, 23), (3, 78), (22, 53), (121, 45), (7,)]
k = 2
result = []
count_element = 0
for element in original_list:
    count_element = 0
    for tuple_element in element:
        if len(str(tuple_element))!=k:
            break
        elif len(str(tuple_element))==k:
            count_element = count_element+1
    if count_element ==len(element):
        result.append(element)
print(result)
           
# 8: Write a Python program to sort a list of tuples by the second Item.
# tup =[('for', 2), ('is', 9), ('to', 7),('Go', 5), ('or', 15), ('a', 13)]

# Expected:
# [('for', 2), ('Go', 5), ('to', 7), ('is', 9), ('a', 13), ('or', 15)]
# list_tuple =[('for', 2), ('is', 9), ('to', 7),('Go', 5), ('or', 15), ('a', 13)]
# def sort_tuple(element):
#     return element[1]

# list_tuple.sort(key=sort_tuple)
# print(list_tuple)

# # 9: Remove an element from a tuple.
# tuple_element=(1,2,3,4,5)
# tuple1 = list(tuple_element)
# tuple1.remove(1)
# print(tuple(tuple1))

# # 10: Write a Python program to compute the element-wise sum of given tuples.
# # Original lists:
# # Input:
# # (1, 2, 3, 4)
# # (3, 5, 2, 1)
# # (2, 2, 3, 1)
# # Expected: Element-wise sum of the said tuples:
# (6, 9, 8, 6)
# tuple1 = (1, 2, 3, 4)
# tuple2 =(3, 5, 2, 1)
# tuple3 = (2, 2, 3, 1)
# final_tuple = []
# for element in range(len(tuple1)):
#     sum = 0
#     sum = sum+tuple1[element]+tuple2[element]+tuple3[element]
#     final_tuple.append(sum)
# print("sum of the tuples",tuple(final_tuple))



