```

Python Built-in Functions
│
├── 1. Chuyển đổi & Tạo kiểu dữ liệu
│   ├── int()        → Chuyển sang số nguyên
│   ├── float()      → Chuyển sang số thực
│   ├── complex()    → Tạo số phức
│   ├── bool()       → Chuyển sang boolean (True/False)
│   ├── str()        → Chuyển sang chuỗi
│   ├── bytes()      → Tạo đối tượng bytes (immutable)
│   ├── bytearray()  → Tạo đối tượng bytearray (mutable)
│   ├── list()       → Tạo danh sách từ iterable
│   ├── tuple()      → Tạo tuple từ iterable
│   ├── set()        → Tạo tập hợp không trùng lặp
│   ├── frozenset()  → Tạo tập hợp bất biến
│   ├── dict()       → Tạo từ điển
│   └── range()      → Tạo dãy số (lazy, không lưu toàn bộ trong RAM)
│
├── 2. Xử lý chuỗi & mã ký tự
│   ├── chr()        → Trả về ký tự từ mã Unicode (số → ký tự)
│   ├── ord()        → Trả về mã Unicode của ký tự (ký tự → số)
│   ├── ascii()      → Giống repr(), nhưng escape ký tự không ASCII
│   ├── repr()       → Trả về biểu diễn "chính thức" của đối tượng (dùng để debug)
│   ├── bin()        → Chuyển số nguyên sang chuỗi nhị phân (vd: '0b101')
│   ├── oct()        → Chuyển sang chuỗi bát phân (vd: '0o17')
│   ├── hex()        → Chuyển sang chuỗi thập lục phân (vd: '0xff')
│   └── format()     → Định dạng giá trị theo chuỗi định dạng
│
├── 3. Toán học & So sánh
│   ├── abs()        → Trả về giá trị tuyệt đối
│   ├── round()      → Làm tròn số (có thể chỉ định số chữ số thập phân)
│   ├── pow()        → Lũy thừa: pow(x, y) = x**y; pow(x, y, z) = (x**y) % z
│   ├── divmod()     → Trả về (x // y, x % y) — thương và dư
│   ├── min()        → Trả về giá trị nhỏ nhất trong iterable hoặc các đối số
│   ├── max()        → Trả về giá trị lớn nhất
│   └── sum()        → Tính tổng các phần tử trong iterable (có thể thêm start)
│
├── 4. Lặp & Xử lý Iterable
│   ├── len()        → Trả về độ dài của đối tượng (list, str, dict…)
│   ├── enumerate()  → Gán chỉ số cho các phần tử (index, value)
│   ├── iter()       → Trả về iterator từ iterable
│   ├── next()       → Lấy phần tử tiếp theo từ iterator
│   ├── reversed()   → Trả về iterator đảo ngược thứ tự
│   ├── sorted()     → Trả về list đã được sắp xếp (không thay đổi gốc)
│   ├── slice()      → Tạo đối tượng slice để cắt chuỗi/danh sách
│   ├── map()        → Ánh xạ hàm lên từng phần tử của iterable
│   ├── filter()     → Lọc các phần tử theo điều kiện (hàm trả True/False)
│   └── zip()        → Ghép các iterable theo vị trí (trả về iterator của tuple)
│
├── 5. Kiểm tra & Phản chiếu (Introspection)
│   ├── type()       → Trả về kiểu dữ liệu của đối tượng
│   ├── isinstance() → Kiểm tra đối tượng có phải là instance của lớp nào đó?
│   ├── issubclass() → Kiểm tra lớp A có phải con của lớp B?
│   ├── callable()   → Kiểm tra đối tượng có thể gọi được (hàm, lớp…)?
│   ├── dir()        → Liệt kê thuộc tính/phương thức của đối tượng
│   ├── vars()       → Trả về __dict__ của đối tượng (thuộc tính dạng dict)
│   ├── locals()     → Trả về dict chứa các biến cục bộ
│   ├── globals()    → Trả về dict chứa các biến toàn cục
│   ├── hasattr()    → Kiểm tra đối tượng có thuộc tính nào đó?
│   ├── getattr()    → Lấy giá trị thuộc tính (có thể đặt giá trị mặc định)
│   ├── setattr()    → Gán giá trị cho thuộc tính
│   ├── delattr()    → Xóa thuộc tính
│   ├── id()         → Trả về định danh (địa chỉ bộ nhớ) của đối tượng
│   ├── hash()       → Trả về giá trị băm (nếu đối tượng hashable)
│   └── help()       → Hiển thị trợ giúp (docstring) của đối tượng/hàm
│
├── 6. Thực thi mã động
│   ├── eval()       → Đánh giá biểu thức Python trong chuỗi (trả kết quả)
│   ├── exec()       → Thực thi khối mã Python trong chuỗi (không trả kết quả)
│   ├── compile()    → Biên dịch mã nguồn thành mã bytecode để chạy sau
│   └── __import__() → Hàm nội bộ dùng để import module (ít dùng trực tiếp)
│
├── 7. Quản lý lớp & đối tượng
│   ├── object()     → Lớp cơ sở của mọi lớp trong Python
│   ├── super()      → Truy cập phương thức của lớp cha (trong kế thừa)
│   ├── property()   → Tạo thuộc tính có getter/setter/deleter
│   ├── staticmethod() → Biến phương thức thành static (không cần self)
│   ├── classmethod()  → Biến phương thức thành class method (nhận cls)
│   └── memoryview() → Tạo view bộ nhớ để truy cập dữ liệu mà không sao chép
│
├──8. Nhập/Xuất & Tương tác người dùng
│   ├── print()      → In giá trị ra màn hình (hoặc file)
│   ├── input()      → Đọc chuỗi từ người dùng (dừng chương trình chờ nhập)
│   └── open()       → Mở file và trả về file object (để đọc/ghi)
│
├── 9. Logic & Điều kiện
│   ├── all()   → True nếu tất cả phần tử là truthy
│   └── any()   → True nếu có ít nhất một phần tử truthy


Important Methods in Python
│
├── SET
│   ├── add()              → Thêm phần tử vào set
│   ├── clear()            → Xóa tất cả phần tử
│   ├── pop()              → Lấy & xóa 1 phần tử ngẫu nhiên
│   ├── union()            → Hợp của 2 set
│   ├── issuperset()       → Kiểm tra set này có chứa set kia?
│   ├── issubset()         → Kiểm tra set này có là con của set kia?
│   ├── intersection()     → Giao của 2 set
│   ├── difference()       → Hiệu của 2 set (A - B)
│   ├── isdisjoint()       → Kiểm tra 2 set có rời nhau?
│   ├── discard()          → Xóa phần tử nếu tồn tại (không lỗi nếu không có)
│   └── copy()             → Tạo bản sao nông của set
│
├── LIST
│   ├── append()           → Thêm phần tử vào cuối danh sách
│   ├── copy()             → Tạo bản sao nông của list
│   ├── count()            → Đếm số lần xuất hiện của phần tử
│   ├── insert()           → Chèn phần tử tại vị trí chỉ định
│   ├── reverse()          → Đảo ngược thứ tự các phần tử
│   ├── remove()           → Xóa phần tử đầu tiên khớp với giá trị
│   ├── sort()             → Sắp xếp list (in-place)
│   ├── pop()              → Lấy & xóa phần tử tại vị trí (mặc định cuối)
│   ├── extend()           → Nối list khác vào cuối
│   ├── index()            → Trả về vị trí đầu tiên của phần tử
│   └── clear()            → Xóa tất cả phần tử
│
├── DICTIONARY
│   ├── copy()             → Tạo bản sao nông của dict
│   ├── clear()            → Xóa tất cả cặp key-value
│   ├── fromkeys()         → Tạo dict mới từ danh sách keys và giá trị mặc định
│   ├── items()            → Trả về view chứa các cặp (key, value)
│   ├── get()              → Lấy value theo key, trả None nếu không có
│   ├── keys()             → Trả về view chứa các key
│   ├── pop()              → Xóa & trả về value theo key
│   ├── values()           → Trả về view chứa các value
│   ├── update()           → Cập nhật dict từ dict khác hoặc iterable
│   ├── setdefault()       → Trả về value, nếu không có thì tạo key với default
│   └── popitem()          → Xóa & trả về cặp (key, value) cuối cùng (LIFO)
│
└── TUPLE
    ├── count()            → Đếm số lần xuất hiện của phần tử
    └── index()            → Trả về vị trí đầu tiên của phần tử (tương tự list)
    → ⚠️ Tuple là IMMUTABLE → Không có phương thức thay đổi nội dung (append, pop, sort…)


String Methods in Python
│
├── 🔤 1. Chuyển đổi chữ hoa/thường & định dạng
│   ├── capitalize()      → Viết hoa chữ đầu, còn lại thường
│   ├── lower()           → Chuyển toàn bộ sang chữ thường
│   ├── upper()           → Chuyển toàn bộ sang chữ hoa
│   ├── swapcase()        → Đảo ngược hoa ↔ thường
│   ├── title()           → Viết hoa chữ đầu mỗi từ
│   ├── casefold()        → Giống lower(), nhưng mạnh hơn (hỗ trợ Unicode)
│   └── zfill(width)      → Thêm số 0 ở đầu để đủ độ dài (dùng cho số)
│
├── 📏 2. Căn lề & điền ký tự
│   ├── center(width[, fillchar]) → Căn giữa, điền ký tự 2 bên
│   ├── ljust(width[, fillchar])  → Căn trái, điền bên phải
│   ├── rjust(width[, fillchar])  → Căn phải, điền bên trái
│   └── expandtabs([tabsize])     → Thay \t bằng khoảng trắng (mặc định tabsize=8)
│
├── 🔍 3. Tìm kiếm & thay thế
│   ├── find(sub[, start[, end]])     → Trả về vị trí đầu tiên, -1 nếu không tìm thấy
│   ├── rfind(sub[, start[, end]])    → Tìm từ phải sang
│   ├── index(sub[, start[, end]])    → Giống find(), nhưng ném lỗi nếu không tìm thấy
│   ├── rindex(...)                   → Giống rfind(), nhưng ném lỗi
│   ├── replace(old, new[, count])    → Thay thế chuỗi (có thể giới hạn số lần)
│   └── translate(table[, deletechars]) → Thay thế/xóa ký tự theo bảng ánh xạ
│
├── ✂️ 4. Tách & ghép chuỗi
│   ├── split([sep[, maxsplit]])       → Tách thành list (mặc định tách theo khoảng trắng)
│   ├── rsplit([sep[, maxsplit]])      → Tách từ phải sang
│   ├── splitlines([keepends])         → Tách theo dòng (xử lý \n, \r\n…)
│   ├── partition(sep)                 → Tách thành (trước, sep, sau) — chỉ tách 1 lần
│   ├── rpartition(sep)                → Tách từ phải
│   └── join(iterable)                 → Ghép các chuỗi trong iterable thành 1 chuỗi
│
├── 🧹 5. Loại bỏ ký tự thừa
│   ├── strip([chars])   → Xóa ký tự ở đầu & cuối (mặc định: khoảng trắng)
│   ├── lstrip([chars])  → Xóa ở đầu (left)
│   └── rstrip([chars])  → Xóa ở cuối (right)
│
├── ✅ 6. Kiểm tra nội dung (trả True/False)
│   ├── isalnum()        → Chỉ chứa chữ và số (không có khoảng trắng, ký tự đặc biệt)
│   ├── isalpha()        → Chỉ chứa chữ cái
│   ├── isdigit()        → Chỉ chứa chữ số (0-9, không có số La Mã, phân số…)
│   ├── isnumeric()      → Mở rộng hơn isdigit(): bao gồm số Unicode (⅕, ², ๓…)
│   ├── isdecimal()      → Chỉ số thập phân (0-9), nghiêm ngặt nhất
│   ├── isspace()        → Chỉ chứa khoảng trắng (space, \t, \n…)
│   ├── islower()        → Tất cả chữ thường
│   ├── isupper()        → Tất cả chữ hoa
│   └── istitle()        → Mỗi từ viết hoa chữ đầu (như tiêu đề)
│
├── 🔗 7. Kiểm tra đầu/cuối chuỗi
│   ├── startswith(prefix[, start[, end]]) → Bắt đầu bằng chuỗi nào đó?
│   └── endswith(suffix[, start[, end]])   → Kết thúc bằng chuỗi nào đó?
│
├── 🧾 8. Định dạng nâng cao
│   └── format(*args, **kwargs) → Định dạng chuỗi theo placeholder ({}.format(...))
│
└── 🌐 9. Mã hóa & giải mã (ít dùng trực tiếp)
    ├── encode([encoding[, errors]]) → Chuyển str → bytes (mặc định UTF-8)
    └── decode(...)                  → ⚠️ KHÔNG PHẢI phương thức của str!
                                     → Là phương thức của **bytes** (str không có decode)


String Formatting (Old-Style: % Operator)
│
├── 🔢 Số nguyên (Integers)
│   ├── %d  → Số nguyên thập phân có dấu (signed decimal)
│   ├── %i  → Tương tự %d (dùng trong C, Python giữ lại cho tương thích)
│   ├── %o  → Số nguyên bát phân (octal) có dấu → VD: %o % 10 → '12'
│   ├── %u  → ⚠️ LỖI THỜI! Giống %d, không dùng nữa (obsolete từ Python 3+)
│   ├── %x  → Thập lục phân thường (hex, lowercase) → VD: %x % 255 → 'ff'
│   └── %X  → Thập lục phân hoa (uppercase) → VD: %X % 255 → 'FF'
│
├── 📏 Số thực (Floating Point)
│   ├── %f  → Định dạng thập phân cố định → VD: %.2f % 3.14159 → '3.14'
│   ├── %F  → Giống %f, nhưng xử lý NaN/Inf khác (hiếm dùng)
│   ├── %e  → Ký hiệu khoa học (exponential, lowercase) → VD: %e % 123 → '1.230000e+02'
│   ├── %E  → Ký hiệu khoa học (uppercase) → VD: %E % 123 → '1.230000E+02'
│   ├── %g  → Tự động chọn giữa %f và %e (loại bỏ số 0 thừa, lowercase)
│   └── %G  → Tự động chọn giữa %F và %E (uppercase)
│
├── 🔤 Chuỗi & Ký tự (Strings & Characters)
│   ├── %c  → Ký tự đơn: nhận int (mã ASCII/Unicode) hoặc chuỗi 1 ký tự
│   │        → VD: %c % 65 → 'A';  %c % 'Z' → 'Z'
│   ├── %s  → Chuỗi: dùng str() để chuyển đổi đối tượng → thân thiện, dễ đọc
│   └── %r  → Chuỗi "đại diện": dùng repr() → có dấu nháy, dùng để debug
│
└── 🛑 Ký tự đặc biệt
    └── %%  → In ra ký tự '%' (escape ký tự %)
            → VD: "Tỷ lệ: %d%%" % 95 → "Tỷ lệ: 95%"

File Object in Python (from open())
│
├── 📌 PHƯƠNG THỨC (Methods)
│   │
│   ├── 🔒 Quản lý trạng thái file
│   │   ├── close()          → Đóng file (giải phóng tài nguyên)
│   │   └── flush()          → Ép ghi buffer ra đĩa ngay lập tức
│   │
│   ├── 🔢 Thông tin hệ thống
│   │   └── fileno()         → Trả về số file descriptor (dùng trong hệ điều hành)
│   │
│   ├── 🖥️ Tương tác terminal
│   │   └── isatty()         → Kiểm tra file có phải terminal (TTY)? → True/False
│   │
│   ├── 📖 Đọc dữ liệu
│   │   ├── read([size])           → Đọc toàn bộ hoặc `size` ký tự/byte
│   │   ├── readline([size])       → Đọc 1 dòng
│   │   ├── readlines([sizehint])  → Đọc tất cả dòng → trả về list
│   │   └── xreadlines()           → ⚠️ LỖI THỜI! (Python 2) → Dùng `for line in file` thay thế
│   │
│   ├── 🧭 Điều hướng con trỏ
│   │   ├── seek(offset[, whence]) → Di chuyển con trỏ đọc/ghi
│   │   │                          → whence: 0=đầu file, 1=vị trí hiện tại, 2=cuối file
│   │   └── tell()                 → Trả về vị trí hiện tại của con trỏ
│   │
│   ├── ✂️ Cắt/xóa nội dung
│   │   └── truncate([size])       → Cắt file tại vị trí con trỏ (hoặc `size`)
│   │
│   └── ✍️ Ghi dữ liệu
│       ├── write(str)             → Ghi chuỗi (text mode) hoặc bytes (binary mode)
│       └── writelines(sequence)   → Ghi list các chuỗi — ⚠️ KHÔNG tự thêm \n!
│
└── 🏷️ THUỘC TÍNH (Attributes)
    ├── closed       → True nếu file đã đóng
    ├── mode         → Chế độ mở file: 'r', 'w', 'a', 'rb', 'r+', v.v.
    ├── name         → Tên đường dẫn của file
    ├── encoding     → Mã hóa (UTF-8, cp1252…) — chỉ có ở text mode
    ├── errors       → Cách xử lý lỗi mã hóa (strict, ignore, replace…)
    ├── newlines     → Dấu ngắt dòng được phát hiện (None, '\n', '\r\n'…)
    └── softspace    → ⚠️ LỖI THỜI! (Python 2) → Không còn dùng trong Python 3


Random Module in Python (import random)
│
├── 🧬 1. Điều khiển trạng thái & hạt giống (Seeding & State)
│   ├── seed([x])            → Đặt hạt giống (seed) để tạo chuỗi ngẫu nhiên có thể lặp lại
│   ├── getstate()           → Lưu trạng thái hiện tại của generator
│   ├── setstate(state)      → Khôi phục trạng thái từ getstate()
│   └── jumpahead(n)         → ⚠️ LỖI THỜI! (Chỉ có trong Python 2, không dùng trong Python 3)
│
├── 🔢 2. Số nguyên ngẫu nhiên
│   ├── getrandbits(k)       → Trả về số nguyên có k bit ngẫu nhiên (dùng cho mật mã)
│   ├── randrange([start], stop[, step]) → Số nguyên trong range(start, stop, step)
│   └── randint(a, b)        → Số nguyên từ a đến b (bao gồm cả a và b)
│
├── 🎲 3. Lấy mẫu & xáo trộn
│   ├── choice(seq)          → Chọn ngẫu nhiên 1 phần tử từ chuỗi/danh sách
│   ├── shuffle(x[, random]) → Xáo trộn list **trực tiếp** (in-place), không trả về giá trị mới
│   └── sample(population, k)→ Lấy **k phần tử không lặp** từ population → trả về list mới
│
├── 📏 4. Số thực ngẫu nhiên — phân phối đều
│   ├── random()             → Số thực trong [0.0, 1.0)
│   ├── uniform(a, b)        → Số thực trong [a, b) hoặc [a, b] (tùy hệ thống)
│   └── triangular(low, high, mode) → Phân phối tam giác (mode = đỉnh)
│
└── 📊 5. Phân phối xác suất nâng cao
    ├── betavariate(alpha, beta)       → Phân phối Beta (0 ≤ x ≤ 1)
    ├── expovariate(lambd)             → Phân phối mũ (λ > 0: giá trị dương; λ < 0: giá trị âm)
    ├── gammavariate(alpha, beta)      → Phân phối Gamma
    ├── gauss(mu, sigma)               → Phân phối chuẩn (nhanh, nhưng ít chính xác hơn normalvariate)
    ├── normalvariate(mu, sigma)       → Phân phối chuẩn (chuẩn hơn gauss)
    ├── lognormvariate(mu, sigma)      → Log-normal: ln(x) ~ N(mu, sigma)
    ├── vonmisesvariate(mu, kappa)     → Phân phối von Mises (dữ liệu góc: 0–2π)
    ├── paretovariate(alpha)           → Phân phối Pareto (mô hình "80/20")
    └── weibullvariate(alpha, beta)    → Phân phối Weibull (độ tin cậy, thời gian hỏng hóc)


Math Module in Python (import math)
│
├── 🔢 1. Number Theoretic & Rounding (Lý thuyết số & Làm tròn)
│   ├── ceil(x)        → Làm tròn lên (trả về int nhỏ nhất ≥ x)
│   ├── floor(x)       → Làm tròn xuống (trả về int lớn nhất ≤ x)
│   ├── trunc(x)       → Cắt bỏ phần thập phân (giống int(x) nhưng không chuyển kiểu)
│   ├── fabs(x)        → Giá trị tuyệt đối của số thực (trả về float)
│   ├── factorial(x)   → Giai thừa của số nguyên không âm (x!)
│   ├── fmod(x, y)     → Phần dư của x / y (dành cho float, khác %)
│   ├── fsum(iterable) → Tính tổng chính xác cao (tránh lỗi làm tròn khi cộng float)
│   ├── modf(x)        → Trả về (phần_thập_phân, phần_nguyên) dưới dạng tuple
│   ├── frexp(x)       → Phân tích x = m * 2**e → trả về (m, e) (m ∈ [0.5, 1))
│   ├── ldexp(x, i)    → Tính x * (2 ** i) — ngược của frexp()
│   ├── copysign(x, y) → Trả về |x| với dấu của y
│   ├── isinf(x)       → Kiểm tra x có phải vô cực (∞) không?
│   └── isnan(x)       → Kiểm tra x có phải "Not a Number" (NaN) không?
│
├── ⚡ 2. Power & Logarithmic (Lũy thừa & Logarit)
│   ├── exp(x)         → e ** x
│   ├── log(x[, base]) → Logarit cơ số `base` của x (mặc định base = e → ln)
│   ├── log1p(x)       → log(1 + x) — chính xác hơn khi x ≈ 0
│   ├── log10(x)       → Logarit cơ số 10
│   ├── pow(x, y)      → x ** y (trả về float, khác built-in pow())
│   └── sqrt(x)        → Căn bậc hai (√x)
│
├── 📐 3. Trigonometric Functions (Lượng giác)
│   ├── sin(x)         → sin(x) — x tính bằng **radian**
│   ├── cos(x)         → cos(x)
│   ├── tan(x)         → tan(x)
│   ├── asin(x)        → arcsin(x) → kết quả ∈ [-π/2, π/2]
│   ├── acos(x)        → arccos(x) → kết quả ∈ [0, π]
│   ├── atan(x)        → arctan(x) → kết quả ∈ [-π/2, π/2]
│   └── atan2(y, x)    → arctan(y/x) nhưng xét đúng góc theo quadrant → kết quả ∈ [-π, π]
│
├── 📏 4. Angular Conversion (Chuyển đổi góc)
│   ├── degrees(x)     → Chuyển radian → độ
│   └── radians(x)     → Chuyển độ → radian
│
├── 🌊 5. Hyperbolic Functions (Hàm hyperbolic)
│   ├── sinh(x)        → sin hyperbolic
│   ├── cosh(x)        → cos hyperbolic
│   ├── tanh(x)        → tan hyperbolic
│   ├── asinh(x)       → arcsinh (nghịch đảo sinh)
│   ├── acosh(x)       → arccosh (nghịch đảo cosh)
│   └── atanh(x)       → arctanh (nghịch đảo tanh)
│
└── 🧮 6. Constants (Hằng số toán học)
    ├── math.pi        → π ≈ 3.141592653589793...
    └── math.e         → e ≈ 2.718281828459045... (cơ số logarit tự nhiên)


Datetime Module in Python (from datetime import date, datetime, time)
│
├── 📅 1. Date Object (chỉ ngày: năm-tháng-ngày)
│   ├── replace(year, month, day)     → Tạo bản sao với các thành phần được thay đổi
│   ├── timetuple()                   → Trả về time.struct_time (dùng với module time)
│   ├── toordinal()                   → Trả về số ngày từ ngày 1/1/1 (proleptic Gregorian)
│   ├── weekday()                     → Thứ trong tuần: 0=Thứ Hai, ..., 6=Chủ Nhật
│   ├── isoweekday()                  → Thứ theo ISO: 1=Thứ Hai, ..., 7=Chủ Nhật
│   ├── isocalendar()                 → Trả về (ISO year, ISO week, ISO weekday)
│   ├── isoformat()                   → Định dạng ISO 8601: "YYYY-MM-DD"
│   ├── __str__()                     → Tương tự isoformat()
│   ├── ctime()                       → Định dạng kiểu Unix: "Mon Jan 01 00:00:00 2024"
│   └── strftime(format)              → Định dạng ngày theo chuỗi mẫu (vd: "%d/%m/%Y")
│
├── 🕒 2. Datetime Object (ngày + giờ: năm-tháng-ngày giờ:phút:giây)
│   │
│   ├── 📅 Trích xuất thành phần
│   │   ├── date()                    → Trả về đối tượng date tương ứng
│   │   ├── time()                    → Trả về time (không có tzinfo)
│   │   └── timetz()                  → Trả về time (có tzinfo nếu có)
│   │
│   ├── 🌍 Múi giờ (timezone-aware)
│   │   ├── replace(...)              → Tạo bản sao với các thành phần được thay đổi (kể cả tzinfo)
│   │   ├── astimezone(tz)            → Chuyển sang múi giờ khác
│   │   ├── utcoffset()               → Trả về offset so với UTC (vd: +07:00)
│   │   ├── dst()                     → Trả về điều chỉnh DST (Daylight Saving Time)
│   │   └── tzname()                  → Tên múi giờ (vd: "ICT", "UTC")
│   │
│   ├── 📅 Các phương thức kế thừa từ date
│   │   ├── timetuple(), utctimetuple() → struct_time (utctimetuple() bỏ tzinfo)
│   │   ├── toordinal(), weekday(), isoweekday(), isocalendar()
│   │   ├── isoformat(), __str__(), ctime(), strftime()
│   │   └── ... (giống hệt date, nhưng bao gồm cả phần giờ)
│   │
│   └── ⏱️ Định dạng đặc biệt
│       └── isoformat(sep='T')        → "YYYY-MM-DDTHH:MM:SS.mmmmmm" (có thể đổi 'T' → ' ')
│
└── ⏰ 3. Time Object (chỉ giờ: giờ:phút:giây.microsecond)
    ├── replace(hour, minute, ...)    → Tạo bản sao với giờ/phút/giây được thay đổi
    ├── isoformat()                   → "HH:MM:SS.mmmmmm"
    ├── __str__()                     → Tương tự isoformat()
    ├── strftime(format)              → Định dạng giờ theo mẫu (vd: "%H:%M")
    ├── utcoffset()                   → Chỉ có nếu time có tzinfo
    ├── dst()                         → Chỉ có nếu time có tzinfo
    └── tzname()                      → Tên múi giờ (nếu có tzinfo)

Date & Time Formatting Codes (strftime / strptime)
│
├── 📅 1. Ngày trong tuần & Tháng
│   ├── %a  → Thứ rút gọn (Sun, Mon, ..., Sat)
│   ├── %A  → Thứ đầy đủ (Sunday, Monday, ..., Saturday)
│   ├── %b  → Tháng rút gọn (Jan, Feb, ..., Dec)
│   └── %B  → Tên tháng đầy đủ (January, February, ..., December)
│
├── 🗓️ 2. Ngày & Năm
│   ├── %d  → Ngày trong tháng (01–31) — có số 0 dẫn đầu
│   ├── %j  → Ngày trong năm (001–366)
│   ├── %y  → Năm 2 chữ số (00–99) → VD: 24 = 2024
│   └── %Y  → Năm 4 chữ số → VD: 2024
│
├── 🕒 3. Giờ, Phút, Giây
│   ├── %H  → Giờ 24h (00–23)
│   ├── %I  → Giờ 12h (01–12)
│   ├── %p  → AM hoặc PM
│   ├── %M  → Phút (00–59)
│   └── %S  → Giây (00–61) → 60/61 cho leap second (hiếm)
│
├── 📆 4. Số tuần trong năm
│   ├── %U  → Tuần tính từ Chủ Nhật (00–53)
│   ├── %W  → Tuần tính từ Thứ Hai (00–53)
│   └── %w  → Thứ trong tuần: 0=Chủ Nhật, 1=Thứ Hai, ..., 6=Thứ Bảy
│
├── 📦 5. Định dạng mặc định hệ thống
│   ├── %c  → Ngày + giờ đầy đủ (theo locale) → VD: "Sun Dec 25 14:30:00 2024"
│   ├── %x  → Chỉ ngày (theo locale) → VD: "12/25/24"
│   └── %X  → Chỉ giờ (theo locale) → VD: "14:30:00"
│
├── 🌍 6. Múi giờ
│   └── %Z  → Tên múi giờ (nếu có) → VD: "UTC", "ICT", "PST" (có thể rỗng nếu naive)
│
└── 🛑 7. Ký tự đặc biệt
    └── %%  → In ra ký tự '%' (dùng để escape)
            → VD: "Progress: %d%%" → "Progress: 75%"

Special (Magic) Methods in Python Classes
│
├── 🧬 1. Khởi tạo & Hủy đối tượng
│   ├── __new__(cls, ...)        → Tạo đối tượng mới (static method, trước __init__)
│   ├── __init__(self, ...)      → Khởi tạo đối tượng (sau khi __new__ tạo xong)
│   └── __del__(self)            → Hủy đối tượng (gọi khi garbage collector thu dọn)
│
├── ⚖️ 2. So sánh đối tượng (Rich Comparison)
│   ├── __eq__(self, other)      → self == other
│   ├── __ne__(self, other)      → self != other
│   ├── __lt__(self, other)      → self < other
│   ├── __le__(self, other)      → self <= other
│   ├── __gt__(self, other)      → self > other
│   └── __ge__(self, other)      → self >= other
│   ⚠️ Lưu ý: __cmp__ (Python 2) → ❌ KHÔNG DÙNG trong Python 3!
│
├── 📦 3. Biểu diễn & Chuyển đổi
│   ├── __repr__(self)           → Biểu diễn "chính thức" (dành cho dev/debug)
│   ├── __str__(self)            → Biểu diễn "thân thiện" (dành cho người dùng)
│   ├── __hash__(self)           → Trả về giá trị băm (nếu muốn dùng làm key trong dict/set)
│   └── __index__(self)          → Trả về int khi dùng trong slice, bin(), hex(), v.v.
│
├── 🔍 4. Truy cập & Thiết lập thuộc tính
│   ├── __getattr__(self, name)        → Gọi khi **thuộc tính KHÔNG TỒN TẠI**
│   ├── __getattribute__(self, name)   → Gọi **LUÔN** khi truy cập thuộc tính (cẩn thận!)
│   ├── __setattr__(self, name, value) → Gọi khi **gán** thuộc tính
│   └── __delattr__(self, name)        → Gọi khi **xóa** thuộc tính (`del obj.attr`)
│
├── 📞 5. Gọi đối tượng như hàm
│   └── __call__(self, *args, **kwargs) → Cho phép obj() — biến instance thành callable
│
└── ⚠️ 6. Các phương thức LỖI THỜI (Python 2)
    ├── __cmp__(self, other)     → ❌ ĐÃ LOẠI BỎ trong Python 3
    └── __nonzero__(self)        → ❌ Thay bằng __bool__(self) trong Python 3
        → Dùng __bool__ để kiểm tra truthiness (if obj: ...)
🖥️ OS Module in Python (`import os`)
│  
├── 🗂️ 1. Làm việc với đường dẫn (Path Operations)
│   ├── os.path.join(path, *paths)        → Ghép các phần thành đường dẫn hợp lệ (tự chọn '/' hay '\')
│   ├── os.path.abspath(path)             → Trả về đường dẫn tuyệt đối
│   ├── os.path.basename(path)            → Trả về tên file/folder cuối cùng (sau dấu '/')
│   ├── os.path.dirname(path)             → Trả về thư mục chứa (phần trước dấu '/')
│   ├── os.path.exists(path)              → Kiểm tra đường dẫn có tồn tại không?
│   ├── os.path.isfile(path)              → Kiểm tra có phải file?
│   ├── os.path.isdir(path)               → Kiểm tra có phải thư mục?
│   ├── os.path.getsize(path)             → Trả về kích thước file (byte)
│   └── os.path.split(path)               → Tách thành (head, tail) → (thư_mục, tên_file)
│
├── 📁 2. Quản lý thư mục & file
│   ├── os.listdir(path='.')              → Liệt kê nội dung thư mục (trả về list tên)
│   ├── os.mkdir(path)                    → Tạo 1 thư mục
│   ├── os.makedirs(path, exist_ok=False) → Tạo nhiều thư mục lồng nhau (như mkdir -p)
│   ├── os.remove(path)                   → Xóa file (⚠️ không xóa thư mục!)
│   ├── os.rmdir(path)                    → Xóa thư mục trống
│   ├── os.removedirs(path)               → Xóa thư mục lồng nhau (nếu trống)
│   ├── os.rename(src, dst)               → Đổi tên hoặc di chuyển file/thư mục
│   └── os.walk(top)                      → Duyệt đệ quy thư mục → (root, dirs, files)
│
├── 🌐 3. Thông tin hệ thống & môi trường
│   ├── os.getcwd()                       → Trả về thư mục làm việc hiện tại
│   ├── os.chdir(path)                    → Đổi thư mục làm việc
│   ├── os.environ                        → Dict chứa biến môi trường (vd: os.environ['PATH'])
│   ├── os.getenv(key, default=None)      → Lấy giá trị biến môi trường (an toàn hơn os.environ[key])
│   └── os.name                           → Tên hệ điều hành: 'posix' (Linux/macOS), 'nt' (Windows)
│
├── 🧪 4. Thực thi lệnh hệ thống (cẩn thận!)
│   ├── os.system(command)                → Chạy lệnh shell và trả về mã thoát (0 = thành công)
│   └── os.popen(command)                 → ⚠️ LỖI THỜI! → Dùng subprocess thay thế
│
└── 🚪 5. Hằng số & tiện ích hệ thống
    ├── os.sep                            → Ký tự phân cách đường dẫn: '/' (Unix), '\\' (Windows)
    ├── os.linesep                        → Ký tự ngắt dòng: '\n' (Unix), '\r\n' (Windows)
    ├── os.curdir                         → Tên thư mục hiện tại: '.'
    └── os.pardir                         → Tên thư mục cha: '..'

🐍 SYS Module in Python (`import sys`)
│  
├── 🧾 1. Thông tin & cấu hình Python
│   ├── sys.version                       → Chuỗi mô tả phiên bản Python đang chạy
│   ├── sys.version_info                  → Tuple: (major, minor, micro, releaselevel, serial)
│   ├── sys.platform                      → Tên nền tảng: 'linux', 'win32', 'darwin' (macOS)
│   ├── sys.executable                    → Đường dẫn đến trình thông dịch Python
│   └── sys.byteorder                     → Kiểu sắp xếp byte: 'little' hoặc 'big'
│
├── 📦 2. Quản lý module & đường dẫn import
│   ├── sys.path                          → List các thư mục tìm module khi import
│   ├── sys.modules                       → Dict chứa tất cả module đã được import
│   └── sys.meta_path                     → Danh sách các meta importers (custom import)
│
├── 🖥️ 3. Tương tác với dòng lệnh (CLI)
│   ├── sys.argv                          → List đối số dòng lệnh: argv[0] = tên script
│   ├── sys.stdin                         → Luồng đầu vào chuẩn (file-like object)
│   ├── sys.stdout                        → Luồng đầu ra chuẩn
│   ├── sys.stderr                        → Luồng lỗi chuẩn
│   └── sys.exit([code])                  → Thoát chương trình ngay (mã 0 = thành công)
│
├── ⚙️ 4. Cấu hình & giới hạn hệ thống
│   ├── sys.getsizeof(object)             → Trả về kích thước bộ nhớ (byte) của đối tượng
│   ├── sys.maxsize                       → Số nguyên lớn nhất mà Py_ssize_t có thể biểu diễn
│   ├── sys.getrecursionlimit()           → Giới hạn đệ quy mặc định (thường là 1000)
│   └── sys.setrecursionlimit(limit)      → Thay đổi giới hạn đệ quy (⚠️ cẩn thận!)
│
└── 🔁 5. Quản lý vòng đời chương trình
    ├── sys.ps1, sys.ps2                  → Chuỗi prompt của REPL (chỉ trong interactive mode)
    ├── sys.__stdin__, sys.__stdout__, sys.__stderr__ → Bản sao gốc của stdin/stdout/stderr
    └── sys.displayhook(value)            → Hàm được gọi khi in kết quả biểu thức trong REPL
```