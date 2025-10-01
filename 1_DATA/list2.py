from copy import deepcopy

a1 = list(range(4))
a2 = list("hello")
a3 = [5] * 3
a4 = [x for x in range(4,9)]
# Int Arr -> Str Arr -> gen 1  -> gen Arr 

# a = []
# a[0]
# a[-1]
# a[1:4]
# # gán slice -> [] -> gán dư -> gán thiếu

# aa  = a1 + a2
# aa *= 2
# aa.copy()
# deepcopy(aa)


#---local varriable ---
# ab= [4,5,6,7]
# def change_arr():
#     ab*= 2
# change_arr()
# print(ab)


#insert -> append -> extend -> list += [Arr]
# remove -> pop -> clear
# len -> min -> max -> sum -> count -> index
#sort(reverse: bool) -> reverse 
sales = [120, 150, 90, 200, 170, 130, 160]

print("=======sale======")
print("sum", sum(sales))
print("avr", sum(sales)/len(sales))
print("min>>", min(sales))
print("max>>", max(sales))
print([x for x in sales if x > 150])

temps = [22.5, None, 25.0, 24.8, None, 26.1, 23.9, 100.0]  # 100.0 là outlier
temps =[x for x in temps if x]
temps = [round(x,1) for x in temps if not x>50] 
t= temps
print(t)

