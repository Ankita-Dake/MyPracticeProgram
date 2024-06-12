d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(d)
op = sorted(d.items(),reverse=True)
original = dict(op)
print(original)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
empty = {}
for i in (dic1,dic2,dic3):
    empty.update(i)

print(empty)

n =  int(input("enter number"))
di =dict()
for x in range(1, n+1):
    di[x] = x*x

print(di)

n1 =  int(input("enter number"))
key =dict()
for x in range(1, n1+1):
    key[x]=x**2

print(key)