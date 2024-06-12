# employees = [     {"name": "Alice", "details": {"age": 30, "salary": 50000}},    
                    # {"name": "Bob", "details": {"age": 35, "salary": 60000}},     
                    # {"name": "Charlie", "details": {"age": 28, "salary": 55000}}, ]
 
# find the total of salary
employees = [     {"name": "Alice", "details": {"age": 30, "salary": 50000}},     
                  {"name": "Bob", "details": {"age": 35, "salary": 60000}},     
                  {"name": "Charlie", "details": {"age": 28, "salary": 55000}}, ]
 
a = employees[0]["details"]["salary"]
b = employees[1]["details"]["salary"]
c = employees[2]["details"]["salary"]
print(a+b+c)

 
input_data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
data = {}
val = input_data['Name'][0]
print(input_data['Age'][0])
for key,value in input_data.items():
    a = key
    # print(a)
print('{'+a+':'+val+'}')
# required output :-[{'Name': 'Tom', 'Age': 28}, {'Name': 'Jack', 'Age': 34}, {'Name': 'Steve', 'Age': 29}, {'Name': 'Ricky', 'Age': 42}]