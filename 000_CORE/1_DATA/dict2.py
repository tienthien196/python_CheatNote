
# init  -> form tuple -> 1 ARR , 2 ARR
# get  -> keys -> values-> items-> -> setdefault -> copy -> update -> pop -> clear 
# 2 dict -> 1 dict -> all() | any()

d = dict(name = "tienthien", skills=["python", "java"], age=25)
d3 = dict([("a", 60), ("coin", 100)])
d4 = dict.fromkeys(["a", "b","c"], 9)
d5 = {k:v for k,v in zip("akjfhd", range(7))}

d6 = d3 | d4
print({**d6})


d0 = {"name": "Tien", "age": 25, "city": "HCM"}
required_keys = ["name", "age"]



# Kiểm tra xem d có chứa TẤT CẢ các key trong required_keys không?
if all(k in d for k in required_keys):
    print("Đủ dữ liệu!")
else:
    print("Thiếu key!")

scores = {"math": 90, "physics": 85, "chem": 78}
a = [n>0 for n in scores.values()]
print(all(a))

form = {"name": "Tien", "email": "tien@example.com", "phone": ""}
print("all value corect" if all(form.values())  else "values failed")
print("all value corect" if any(form.values())  else "values failed")
