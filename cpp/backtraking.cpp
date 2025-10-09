#include <iostream>
using namespace std;

const int N = 4; // Thử với N=4 trước (nhỏ, dễ theo dõi)
char board[N][N];

// Hàm in bàn cờ - minh họa rõ ràng
void printBoard(const char board[N][N], const char* title) {
    cout << "\n=== " << title << " ===\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << (board[i][j] == 'Q' ? 'Q' : '.') << " ";
        }
        cout << "\n";
    }
    cout << "-------------------\n";
}

// Kiểm tra xem có thể đặt hậu tại (row, col) không
bool isSafe(int row, int col) {
    // 1. Kiểm tra cột trên
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 'Q') return false;
    }

    // 2. Kiểm tra đường chéo trái trên
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q') return false;
    }

    // 3. Kiểm tra đường chéo phải trên
    for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++) {
        if (board[i][j] == 'Q') return false;
    }

    return true;
}

// Hàm quay lui chính
bool solveNQueens(int row) {
    // Điều kiện dừng: đã đặt đủ N quân (từ hàng 0 đến N-1)
    if (row == N) {
        printBoard(board, "✅ TÌM THẤY LỜI GIẢI!");
        return true; // Dừng sau 1 lời giải
    }

    // Thử từng cột ở hàng `row`
    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            // --- CHỌN: đặt quân hậu ---
            board[row][col] = 'Q';
            printBoard(board, "👉 Đặt Q tại hàng");

            // --- ĐỆ QUY: sang hàng tiếp theo ---
            if (solveNQueens(row + 1)) {
                return true; // Truyền kết quả thành công lên trên
            }

            // --- QUAY LUI: xóa quân hậu ---
            board[row][col] = '.';
            printBoard(board, "🔙 Quay lui: xóa Q tại hàng");
        }
    }

    // Nếu thử hết cột mà không được → quay lui
    return false;
}

// Khởi tạo bàn cờ trống
void initBoard() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            board[i][j] = '.';
        }
    }
}

// MAIN
int main() {
    initBoard();
    cout << "Bắt đầu giải bài toán " << N << "-Queen...\n";
    if (!solveNQueens(0)) {
        cout << "❌ Không tìm thấy lời giải!\n";
    }
    return 0;
}