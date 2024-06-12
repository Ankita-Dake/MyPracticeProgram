s = "dnnx jd "
print(len(s))

s1 = 'hello world'
empty = {}
for count in s1:
    if count in empty:
        empty[count] += 1
    else:
        empty[count] = 1

print(empty)

Sample_String = 'w'
def func(Sample_String):
    if len(Sample_String)<2:
        print(" ") 
    else:
        print(Sample_String[0:2]+Sample_String[-2:])
        
func(Sample_String)