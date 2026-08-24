
"""
raw_values =[100,None,250,"invalid",300,None,450]
integers = []

for i in raw_values:

    a= isinstance(i,int)
    if a == False :
        continue
    integers.append(i)

print(integers)
"""
#list comprehension
raw_values =[100,None,250,"invalid",300,None,450]

integers = [i for i in raw_values if isinstance(i,int)]

print(integers)