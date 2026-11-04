// Hill Cipher: Encrypt plaintext DONE using a 2x2 key matrix
#include <iostream>
#include <string>
using namespace std;

int main() {
    string pt = "DONE", ct = "";
    int a, b, c, d;

    cout << "Enter 2x2 key matrix: ";
    cin >> a >> b >> c >> d;

    // Encrypt two letters at a time
    for (int i = 0; i < 4; i += 2) {
        int x = pt[i] - 'A';
        int y = pt[i + 1] - 'A';

        ct += char(((a * x + b * y) % 26) + 'A');
        ct += char(((c * x + d * y) % 26) + 'A');
    }

    cout << "Plaintext: " << pt << endl;
    cout << "Ciphertext: " << ct << endl;

    return 0;
}