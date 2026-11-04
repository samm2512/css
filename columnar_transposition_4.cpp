#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string pt, ct = "";
    int cols = 4;

    cout << "Enter plaintext (no spaces): ";
    cin >> pt;

    // Convert plaintext to uppercase
    for (char &ch : pt)
        ch = toupper(ch);

    int rows = (pt.size() + cols - 1) / cols;
    char grid[100][4];
    int k = 0;

    // Fill matrix row-wise and add X if needed
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (k < (int)pt.size()) grid[r][c] = pt[k++];
            else grid[r][c] = 'X';
        }
    }

    // Read matrix column-wise
    for (int c = 0; c < cols; c++)
        for (int r = 0; r < rows; r++)
            ct += grid[r][c];

    cout << "Ciphertext: " << ct << endl;
    return 0;
}