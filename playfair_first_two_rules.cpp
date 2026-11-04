#include <iostream>
using namespace std;

int main() {
    char key[100], pt[100], mat[5][5];
    int used[26] = {0};

    cout << "Enter key: ";
    cin >> key;
    cout << "Enter plaintext: ";
    cin >> pt;

    used['J' - 'A'] = 1;
    int k = 0;

    for (int i = 0; key[i] != '\0'; i++) {
        char ch = key[i];
        if (ch >= 'a' && ch <= 'z') ch -= 32;
        if (ch == 'J') ch = 'I';

        if (ch >= 'A' && ch <= 'Z' && !used[ch - 'A']) {
            mat[k / 5][k % 5] = ch;
            used[ch - 'A'] = 1;
            k++;
        }
    }

    for (int i = 0; i < 26; i++)
        if (!used[i]) {
            mat[k / 5][k % 5] = 'A' + i;
            k++;
        }

    cout << "Ciphertext: ";

    for (int i = 0; pt[i] != '\0'; i += 2) {
        char a = pt[i], b = pt[i + 1];

        if (a >= 'a' && a <= 'z') a -= 32;
        if (b >= 'a' && b <= 'z') b -= 32;
        if (a == 'J') a = 'I';
        if (b == 'J') b = 'I';

        int r1, c1, r2, c2;

        for (int r = 0; r < 5; r++)
            for (int c = 0; c < 5; c++) {
                if (mat[r][c] == a) r1 = r, c1 = c;
                if (mat[r][c] == b) r2 = r, c2 = c;
            }

        if (r1 == r2)
            cout << mat[r1][(c1 + 1) % 5]
                 << mat[r2][(c2 + 1) % 5];
        else if (c1 == c2)
            cout << mat[(r1 + 1) % 5][c1]
                 << mat[(r2 + 1) % 5][c2];
        else
            cout << a << b;
    }

    return 0;
}