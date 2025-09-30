a = [4, 8, 2,4,5,6]
b = [7,8,9]

required_keys = ["name", "age"] 
print(any(x in a for x in  b))


d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(a=9, k=8)

i = list(k in d1 for k in d2.keys())
print(any(i), " ", all(i))

