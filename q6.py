#1: Write a Python program group Similar items to Dictionary Values List.
# Input: test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
# Expected: {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 
list_items = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
empty_dict = {}
for element in list_items:
    if element not in empty_dict:
        empty_dict[element]=[]
        empty_dict[element].append(element)
    else:
        empty_dict[element].append(element)
print(empty_dict)

#2: Write a Python program convert List of Dictionaries to List of Lists
# Input:  [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}] 
# Expected: [['Gfg', 'best'], [123, 10], [51, 7]] 
list_dict = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
list_items= []
for element in list_dict:
    empty_list = []
    for key in element.keys():
        empty_list.append(key)
    if empty_list not in list_items:
        list_items.append(empty_list)
    
    empty_list = []
    for val in element.values():
        empty_list.append(val)
    if empty_list not in list_items:
        list_items.append(empty_list)
    
print(list_dict)


# 3: Write a Python program to print all distinct values in a dictionary.

# Original List:  [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]        
# Unique Values: {'S009', 'S002', 'S007', 'S005', 'S001'}  
list_dict =  [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
distict_list = []

for element in list_dict:
    for value in element.values():
          distict_list.append(value)

print("Unique Values are: ", set(distict_list))

# 4: Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
 
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# Expected: ['b', 'e', 'c']
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
value_dict = []
sorted_list = sorted(my_dict.values())
key_dict = sorted_list[-3:]
for i in my_dict:
    if my_dict[i] in key_dict:
        value_dict.append(i)
print(value_dict)

#5: Write a Python program to combine values in a list of dictionaries.

# Input: item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected: ({'item1': 1150, 'item2': 300})
item_list= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result_dict = {}

for element_dict in item_list:
    for key in element_dict:
        if key == "item":
            store_dict = element_dict[key]
            if element_dict[key] not in result_dict:
                result_dict[element_dict[key]] = 0
        if key == "amount":
            for key_element in result_dict:
                if key_element == store_dict:
                    result_dict[key_element] = result_dict[key_element] + element_dict[key]
            
print(result_dict)

#6: Write a Python program to sort a list alphabetically in a dictionary.

# Input: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# Expected: {'n1': [1, 2, 3], ‘n2’:10,'n3': [1, 2, 5], 'n3': [2, 3, 4]}, ‘n4’: 30
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key, value in num.items():
    num[key] = sorted(value)
    
print("Sorted list is  ", num)


#7: Write a Python program to count the number of items in a dictionary value that is a list.

# Input: dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Expected: 5

list_dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
value_count = 0
for value in list_dict.values():
    if type(value) == list:
      value_count = value_count + len(value)
        
print("Total elements are: ", value_count)

# 8: Write a Python program remove duplicate values across Dictionary Values

# Input: {'first': [1, 4, 5, 6], 'sec': [1, 8, 9], 'third': [10, 22, 4], 'fourth': [5, 11, 22]}
# Expected: {'first': [6], 'sec': [8, 9], 'third': [10], 'fourth': [11]}
dict_value={'first': [1, 4, 5, 6], 'sec': [1, 8, 9], 'third': [10, 22, 4], 'fourth': [5, 11, 22]}
values_list = []

for value in dict_value.values():
    values_list.extend(value)
    
print(values_list)

for key, val in dict_value.items():
    sample_list = []
    for element in val:
        if values_list.count(element) == 1:
            sample_list.append(element)
            dict_value[key] = sample_list

print("remove duplicate values:", dict_value)

# 9: Write a Python program counting the frequencies in a list using dictionary in Python

# Input:  [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
#                   4, 4, 4, 2, 2, 2, 2]
# Expected:  1 : 5
#            2 : 4
#            3 : 3
#            4 : 3
#            5 : 2
new_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
result_dict = {}

for element in new_list:
    if element not in result_dict:
        result_dict[element] = 1
    else:
        result_dict[element] = result_dict[element] + 1
        
print(result_dict)