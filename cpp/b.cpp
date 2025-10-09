#include <iostream>
using namespace std;

int main() {
    int t, x;
    cin >> t >> x;

    bool board[9][9] = {false}; 


    for (int i = 0; i < t; ++i) {
        int tx, ty;
        cin >> tx >> ty;


        board[tx][ty] = true;


        for (int d = 1; tx + d <= 8 && ty + d <= 8; ++d) {
            board[tx + d][ty + d] = true;
        }

        for (int d = 1; tx - d >= 1 && ty + d <= 8; ++d) {
            board[tx - d][ty + d] = true;
        }

        for (int d = 1; tx + d <= 8 && ty - d >= 1; ++d) {
            board[tx + d][ty - d] = true;
        }

        for (int d = 1; tx - d >= 1 && ty - d >= 1; ++d) {
            board[tx - d][ty - d] = true;
        }
    }


    for (int i = 0; i < x; ++i) {
        int xx, xy;
        cin >> xx >> xy;


        board[xx][xy] = true;


        for (int r = 1; r <= 8; ++r) {
            board[xx][r] = true;
        }

        for (int c = 1; c <= 8; ++c) {
            board[c][xy] = true;
        }
    }

    int count = 0;
    for (int i = 1; i <= 8; ++i) {
        for (int j = 1; j <= 8; ++j) {
            if (board[i][j]) {
                count++;
            }
        }
    }

    cout << count << endl;

    return 0;
}