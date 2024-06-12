# list1 = [100, 200, 300, 400, 500]
# print(list1[::-1])

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# for i,j in zip(list1,list2):
#     print(i+j)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in numbers:
#    res.append(i*i)
# print(res)

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = []
# for i in list1:
#    for j in list2:
#       list3.append(i+j)
#     #   print(i+j, end=" ")
# print(list3)

# list1 = [10, 20, 30, 40]

# list2 = [100, 200, 300, 400]

# for i ,j in zip(list1,list2[::-1]):
#     print(i,j)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# emp = []
# for i in list1:
#     if i != "":
#         emp.append(i)
# print(emp)

# l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# l1[2][2].append(8000)
# l1[2][2].insert(1,7000)
# print(l1)

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] =200
print(list1)

l = [5, 20, 15, 20, 25, 50, 20]
result = []
for index in l : 
    if index == 20:
        result.append(index)
print(result)

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# res = dict(zip(keys,values))
# print(res)
# res_dict = dict()
# for i in range(len(keys)):
#     res_dict.update({keys[i]:values[i]})

# print(res_dict)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty':300}
# dict2 = {'Thirty': 0, 'Fourty': 40, 'Fifty': 50}
# d = {**dict1,**dict2}
# print(d)

# d1  = dict1.copy()
# d1.update(dict2)
# print(d1)

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# res = dict.fromkeys(employees,defaults)
# print(res)
# print(res["Kelly"]["designation"])

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# a = sample_dict.keys()
# b = sample_dict.values()
# print(a,b)
# print([sample_dict['name']],sample_dict['salary'])

# dicti = dict()
# for key,values in sample_dict:
#     print(key,values)

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# print(sample_dict['emp3']['salary'])
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# print(min(sample_dict,key=sample_dict.get))
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict['location']= sample_dict.pop('city')
# print(sample_dict)

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# print(sample_dict.values())
# if  200 in sample_dict.values():
#     print("200 present in a dict")
# else:
#     print("Not present")

# Sample_string = 'w3resource'
# Expected_output= {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# res = {}
# count = 0
# for i in Sample_string:
#     if i in res:
#         res[i] +=1
#     else:
#         res[i] = 1
# print(res)

Sample= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

print(min(Sample,key=Sample.get))
