# . Write a Python program to sum all the items in a list.
l1 = [1,2,3,45]
sum = 0
for i in l1:
    sum = sum+i
print(sum)

# Write a Python program to multiply all the items in a list.
l2 = [1,2,3,4]
mult = 1
for i in l2:
    mult = mult*i
print(mult)

# Write a Python program to get the largest number from a list
l3 = [1,2,3,4,5,56,45,0]

def maxele(l3):
    max = l3[0]
    for i in l3:
        if i>max:
            max = i
    return max

print(maxele(l3))

# Write a Python program to get the smallest number from a list
def minele(l4):
    mini = l4[0]
    for i in l4:
        if i< mini:
            mini = i
    return mini

l4 = [1,2,3,-1]
print(minele(l4))

# Write a Python program to count the number of strings from a given list of strings.
#  The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
sample_list = ['abc', 'xyz', 'aba', '1221']

def countele(sample_list):
    count = 0
    for word in sample_list:
        if len(word)>1 and word[0]==word[-1]:
            count = count+1
    return count

print(countele(sample_list))

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40,70]
l5 = set(a)
print(l5)
emp_list = []
for i in a:
    if i not in emp_list:
        emp_list.append(i)
print(emp_list)

# input = "aaabbcccdggaaa"
# output = "a3b2c3d1g2a3"
input1 = "aaabbcccdggaaa"
emptylist = {}
output = ""

for a in input1:
    if a in emptylist:
      emptylist[a]+=1 
    else:
        emptylist[a] = 1
    
print(str(emptylist))
print(str(emptylist.keys()))
print(str(emptylist.values()))
op = ''
op1=''
data =''
for key,value in emptylist.items():
    op1 = key
    op = value
    data =data+op1+str(op)
print(data)


# Numbers = [1,1, 2, 3,3,2,4,5,4,6,6,6] 
Numbers = [1,1, 2, 3,3,2,4,5,4,6,6,6,6] 
count = 0
oddnum ={}
for num in Numbers:
    if num in oddnum:
        oddnum[num]+=1
    else:
        oddnum[num] =1
print(oddnum)
for key ,value in oddnum.items():
    if value<2:
        print(key)
    if value>2:
        print(key)



    