s = set()#set
s1 = {} # dict 
s2 = {"a", "b", "c", "d"}
s3 = {3.14, 2*2, "tienthein"}

s4 = set([2,43,46,6,54]) 
print(s4)
s4 = list(s4)
s5 = frozenset(s4) 
print(s4)



# len - max - min - sum
#add -> update->
# remove -> discard  -> pop -> clear
# O:L  hợp |  giao & hiệu - đối xứng ^
# is_subset is_supper_set .isdisjoint (ko giao nhau)
#  


set4  = {3,54,[4,6,7]} # không dùng được với list
print(type(set4))