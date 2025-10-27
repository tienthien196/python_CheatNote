# ───────────────────────────────────────
# 🔷 SET — Tập hợp (không thứ tự, không trùng lặp)
# ───────────────────────────────────────

print(" tiến \t thiệ\n  tiếnh ".strip().splitlines())

# add(): Thêm phần tử vào set (nếu chưa có)
{1, 2}.add(3)                     # → {1, 2, 3}
{1, 2}.add(2)                     # → {1, 2}  (không thêm trùng)

# clear(): Xóa tất cả phần tử
{1, 2, 3}.clear()                 # → set()

# pop(): Lấy và xóa 1 phần tử NGẪU NHIÊN (không xác định thứ tự)
{1, 2, 3}.pop()                   # → 1 (hoặc 2, hoặc 3 — không đảm bảo)

# union(): Trả về hợp của 2 set (không thay đổi gốc)
{1, 2}.union({2, 3})              # → {1, 2, 3}

# issuperset(): Kiểm tra set này có chứa set kia?
{1, 2, 3}.issuperset({1, 2})      # → True
{1, 2}.issuperset({1, 2, 3})      # → False

# issubset(): Kiểm tra set này có là tập con?
{1, 2}.issubset({1, 2, 3})        # → True

# intersection(): Giao của 2 set
{1, 2, 3}.intersection({2, 3, 4}) # → {2, 3}

# difference(): Hiệu (A - B): phần tử trong A nhưng không trong B
{1, 2, 3}.difference({2, 3})      # → {1}

# isdisjoint(): Kiểm tra 2 set có không giao nhau?
{1, 2}.isdisjoint({3, 4})         # → True
{1, 2}.isdisjoint({2, 3})         # → False

# discard(): Xóa phần tử nếu tồn tại — KHÔNG lỗi nếu không có
{1, 2, 3}.discard(2)              # → {1, 3}
{1, 2, 3}.discard(99)             # → {1, 2, 3}  (an toàn)

# remove(): Xóa phần tử — NẾU KHÔNG CÓ → KeyError
# {1, 2}.remove(99)               # → KeyError

# copy(): Tạo bản sao nông (shallow copy)
{1, 2, [3]}.copy()                # → ⚠️ Lỗi nếu có phần tử unhashable (list không dùng được trong set!)
{1, 2, "a"}.copy()                # → {1, 2, "a"}

# ───────────────────────────────────────
# 📋 LIST — Danh sách (có thứ tự, cho phép trùng lặp)
# ───────────────────────────────────────

# append(): Thêm phần tử vào CUỐI list
[1, 2].append(3)                  # → [1, 2, 3]

# copy(): Tạo bản sao nông
[1, [2]].copy()                   # → [1, [2]]  (list con vẫn chia sẻ tham chiếu)

# count(): Đếm số lần xuất hiện
[1, 2, 2, 3].count(2)             # → 2
[1, 2, 3].count(99)               # → 0

# insert(i, x): Chèn x tại vị trí i
[1, 3].insert(1, 2)               # → [1, 2, 3]

# reverse(): Đảo ngược list (in-place)
[1, 2, 3].reverse()               # → [3, 2, 1]

# remove(x): Xóa phần tử x đầu tiên — nếu không có → ValueError
[1, 2, 2, 3].remove(2)            # → [1, 2, 3]
# [1, 2].remove(99)               # → ValueError

# sort(): Sắp xếp list (in-place, mặc định tăng dần)
[3, 1, 2].sort()                  # → [1, 2, 3]
["b", "A", "a"].sort()            # → ["A", "a", "b"]  (theo ASCII)

# pop([i]): Lấy & xóa phần tử tại i (mặc định cuối)
[1, 2, 3].pop()                   # → 3; list → [1, 2]
[1, 2, 3].pop(0)                  # → 1; list → [2, 3]

# extend(iterable): Nối các phần tử từ iterable vào cuối
[1, 2].extend([3, 4])             # → [1, 2, 3, 4]
[1, 2].extend("ab")               # → [1, 2, 'a', 'b']

# index(x): Trả về vị trí đầu tiên của x — nếu không có → ValueError
[1, 2, 3].index(2)                # → 1
# [1, 2].index(99)                # → ValueError

# clear(): Xóa tất cả phần tử
[1, 2, 3].clear()                 # → []

# ───────────────────────────────────────
# 📘 DICTIONARY — Từ điển (key-value, key phải hashable)
# ───────────────────────────────────────

# copy(): Tạo bản sao nông
{"a": [1]}.copy()                 # → {"a": [1]}  (list con vẫn chia sẻ)

# clear(): Xóa tất cả cặp key-value
{"a": 1, "b": 2}.clear()          # → {}

# fromkeys(keys, value): Tạo dict mới từ danh sách keys
dict.fromkeys(["a", "b"], 0)      # → {"a": 0, "b": 0}
dict.fromkeys(["a", "b"])         # → {"a": None, "b": None}

# items(): Trả về view (dict_items) của các cặp (key, value)
{"a": 1, "b": 2}.items()          # → dict_items([('a', 1), ('b', 2)])

# get(key, default): Lấy value — nếu không có → trả default (mặc định None)
{"a": 1}.get("a")                 # → 1
{"a": 1}.get("b", "N/A")          # → "N/A"

# keys(): Trả về view chứa các key
{"a": 1, "b": 2}.keys()           # → dict_keys(['a', 'b'])

# values(): Trả về view chứa các value
{"a": 1, "b": 2}.values()         # → dict_values([1, 2])

# pop(key, default): Xóa & trả về value — nếu không có và không có default → KeyError
{"a": 1, "b": 2}.pop("a")         # → 1; dict → {"b": 2}
{"a": 1}.pop("b", "N/A")          # → "N/A"

# update(other): Cập nhật dict từ dict/iterable khác
{"a": 1}.update({"b": 2})         # → {"a": 1, "b": 2}
{"a": 1}.update([("b", 2)])       # → {"a": 1, "b": 2}

# setdefault(key, default): Trả về value; nếu không có → tạo key với default
d = {"a": 1}
d.setdefault("b", 2)              # → 2; d → {"a": 1, "b": 2}
d.setdefault("a", 99)             # → 1; d không đổi

# popitem(): Xóa & trả về cặp (key, value) CUỐI CÙNG (LIFO — từ Python 3.7+)
{"a": 1, "b": 2}.popitem()        # → ("b", 2)

# ───────────────────────────────────────
# 🔗 TUPLE — Bộ (immutable, có thứ tự)
# ───────────────────────────────────────

# ⚠️ Tuple KHÔNG CÓ phương thức thay đổi nội dung (append, pop, sort…)
# Chỉ có 2 method:

# count(): Đếm số lần xuất hiện
(1, 2, 2, 3).count(2)             # → 2

# index(): Trả về vị trí đầu tiên
(1, 2, 3).index(2)                # → 1
# (1, 2).index(99)                # → ValueError

# Các thao tác như +, * vẫn được (tạo tuple mới, không thay đổi gốc)
(1, 2) + (3,)                     # → (1, 2, 3)
(1,) * 3                          # → (1, 1, 1)