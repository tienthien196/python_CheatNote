# file: BacktrackingSolver.gd
class_name BacktrackingSolver

# --- CẤU HÌNH ---
var apply_in_place: bool = true
var find_one_only: bool = false          # Dừng sau lời giải đầu tiên?
var optimize_mode: bool = false          # Có đang tìm lời giải "tốt nhất"?
var max_solutions: int = -1              # -1 = vô hạn, >=0 = giới hạn số lời giải

# --- DỮ LIỆU ---
var solutions = []
var best_solution = null
var best_value = null  # càng nhỏ/càng lớn tùy logic (do người dùng định nghĩa)

# --- BẮT BUỘC GHI ĐÈ ---

func get_initial_state():
	push_error("Phải ghi đè get_initial_state()!")
	return null

func is_solution(state) -> bool:
	push_error("Phải ghi đè is_solution()!")
	return false

func get_choices(state):
	push_error("Phải ghi đè get_choices()!")
	return []

func apply_choice(state, choice):
	push_error("Phải ghi đè apply_choice()!")
	return state

func undo_choice(state, choice):
	pass  # chỉ cần nếu apply_in_place = true

func is_valid_choice(state, choice) -> bool:
	return true

# --- TUỲ CHỈNH NÂNG CAO (ghi đè nếu cần) ---

# Sao chép trạng thái — hỗ trợ cả custom object!
func copy_state(state):
	if state is Array:
		return state.duplicate(true)  # deep copy
	elif state is Dictionary:
		return state.duplicate(true)
	elif state.has_method("duplicate"):
		return state.duplicate()
	else:
		# fallback: clone bằng cách serialize (cẩn thận với Resource/Object phức tạp)
		return state  # ⚠️ NGUY HIỂM nếu không override!

# Trả về "giá trị" của lời giải (càng nhỏ/càng lớn càng tốt)
# Chỉ dùng khi optimize_mode = true
func evaluate_solution(solution):
	push_error("Khi optimize_mode=true, phải ghi đè evaluate_solution()!")
	return 0

# Điều kiện cắt tỉa: nếu true → bỏ nhánh này
# state: trạng thái hiện tại (chưa là lời giải)
func should_prune(state) -> bool:
	return false  # mặc định: không cắt

# --- HÀM PUBLIC ---

func solve():
	solutions.clear()
	best_solution = null
	best_value = null

	var initial = get_initial_state()
	if initial == null:
		push_error("Trạng thái ban đầu không hợp lệ!")
		return

	if apply_in_place:
		_backtrack_inplace(initial)
	else:
		_backtrack_copy(initial)

# Lấy lời giải tốt nhất (nếu optimize_mode = true)
func get_best_solution():
	return best_solution

# --- HÀM RIÊNG ---

func _should_stop() -> bool:
	if find_one_only and solutions.size() >= 1:
		return true
	if max_solutions >= 0 and solutions.size() >= max_solutions:
		return true
	return false

func _backtrack_inplace(state):
	if _should_stop():
		return

	if is_solution(state):
		var sol = copy_state(state)
		_process_solution(sol)
		if _should_stop():
			return

	if should_prune(state):
		return

	for choice in get_choices(state):
		if _should_stop():
			break
		if is_valid_choice(state, choice):
			apply_choice(state, choice)
			_backtrack_inplace(state)
			undo_choice(state, choice)

func _backtrack_copy(state):
	if _should_stop():
		return

	if is_solution(state):
		_process_solution(state)  # state đã là bản sao
		if _should_stop():
			return

	if should_prune(state):
		return

	for choice in get_choices(state):
		if _should_stop():
			break
		if is_valid_choice(state, choice):
			var new_state = apply_choice(state, choice)
			_backtrack_copy(new_state)

func _process_solution(solution):
	if optimize_mode:
		var value = evaluate_solution(solution)
		if best_solution == null or _is_better(value, best_value):
			best_solution = solution
			best_value = value
		# Không lưu vào solutions nếu chỉ quan tâm best
	else:
		solutions.append(solution)

# So sánh: giá trị mới có "tốt hơn" giá trị cũ?
# Mặc định: **càng nhỏ càng tốt** (minimization)
# Ghi đè hàm này nếu muốn maximization
func _is_better(new_val, old_val) -> bool:
	return new_val < old_val  # thay bằng `new_val > old_val` nếu tối đa hóa