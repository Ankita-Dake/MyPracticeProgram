# Input = [["a", "b","c"], [1,2,3]]
# ouput = {"a":1,"b":2,"c":3}
# print(Input[1])
# op = {}
# for i in Input:
#     i



# str1 = "ankitadake"
# print(len(str1))
# print(str1[-1:-8:-1])
# empty = []
# for i in str1:
#     if i not in empty:
#         empty.append(i)
# print(empty)
# str2 = [1,2,3,1,4,3,2]
# dict = {}
# for i in str2:
#     if i in dict:
#         dict[i] +=1
#     else:
#         dict[i] = 1
# print(dict)

# str3 = "ankitadakeee"
# dic ={}
# for i in str3:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i] = 1
# print(str(dic))

# input = 26

# str1 = "James"
# length =int(len(str1)/2)
# mi = int(len(str1) / 2)
# print(length)
# print(str1[length])
# # print(str1[0]+str1[2]+str1[-1])
# # print(str1[-1])
# first = str1[0]+str1[length]+str1[-1]
# print(first)

# s = "JhonDipPeta"
# l1 = int(len(s)/2)

# res = s[l1 - 1:l1 + 2]
# print(res)

# s1 = "Ault"
# s2 = "Kelly"
# l1 = int(len(s1)/2)
# print(s1[:l1]+s1[l1]+s2+s1[l1:])
# print(s1[:l1:]+s2+s1[l1:])

# s1 = "America"
# s2 = "Japan"
# length = len(s1)
# ll = int(len(s1)/2)
# first = s1[0]+s1[ll]+s1[length-1]
# length2 = len(s2)
# l2 = int(len(s2)/2)
# second = s2[0]+s2[l2]+s2[length2-1]
# print(first+second)
# print(s1[0]+s2[0]+s1[ll]+s2[l2]+s1[length-1]+s2[length2-1])


# str1 = "PyNaTive"
# s1 = []
# s2 = []
# for i in str1:
#     if i.islower():
#         s1.append(i)
#     # else:
#     #     s1.append(i)
# print(s1)
# print(s1+s2)
# print(s2)
# ans = ''.join(s1+s2)
# print(ans)

# str1 = "PYnAtivE"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # add lowercase characters to lower list
#         lower.append(char)
#     else:
#         # add uppercase characters to lower list
#         upper.append(char)

# # Join both list
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)


# str1 = "P@#yn26at^&i5ve"
# digit = 0
# char = 0
# symbol = 0
# for i in str1:
#     if i.isdigit():
#         digit = digit+1
#     elif i.isalpha():
#         char = char+1
#     else:
#         symbol = symbol+1
# print("Digit = ",digit)
# print("Character = ",char)
# print("Symbol = ",symbol)


# s1 = "Abcdefh"
# s2 = "Xyzwz"
# l1 = len(s1)

# l2 = len(s2)

# length = l1 if l1>l2 else l2
# print(length)
# result = " "
# s2 =s2[: : -1]
# print(s2)
# for i in range(length):
#     if i < l1:
#         result = result + s1[i]
#     if i < l2:
#         result = result + s2[i]

# print(result)

# s1 = "Ynf"
# s2 = "PYnative"
# flag = True
# for i in s1:
#     if i in s2:
#         continue
#     else:
#         flag = False
# print(flag)
# # ans = True if s1 in s2 else False
# # print(ans)

# str1 = "Welcome to USA USA. usa awesome, isn't it?"
# sub_string = "a"
# strr = str1.lower()
# count = strr.count(sub_string.lower())
# print("The USA count is:", count)



# str1 = "PYnative29@#8496"
# digit = []
# count = 0
# sum = 0
# for i in str1:
#     if i.isdigit():
#         digit.append(i)
#         count = count+1
# for j in digit:
#     sum = sum + (int(j))

# print("sum..",sum)
# print("avrage...",sum/count)


# str1 = "Apple"
# dic = {}
# for i in str1:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# print(" occurance of each character",dic)


# str1 = "PYnative"
# print(str1[::-1])


# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# ans = str1.rfind("works")
# print(ans)

# str1 = "Emma-is-a-data-scientist"
# print(str1)
# ans = str1.split("-")

# for i in ans:
#     print(i)

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# emp = []
# for i in str_list:
#     if i != "":
#         emp.append(i)
# print(emp)

# str1 =  'I am 25 years and 10 months old'
# emp = []
# for i in str1:
#     if i.isdigit():
#         emp.append(i)
# ans = "".join(emp)
# print(ans)

str1 = "Emma25 is Data scientist50 and AI Expert"
emp = []
temp = str1.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        emp.append(item)
print(emp)