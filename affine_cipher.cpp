#include <iostream>
#include <string>
using namespace std;

int inverse(int a) {
    for (int i = 1; i < 26; i++)
        if ((a * i) % 26 == 1) return i;
    return -1;
}

int main() {
    string pt, ct = "", dt = "";
    int a, b;

    cout << "Enter lowercase plaintext: ";
    cin >> pt;
    cout << "Enter keys a and b: ";
    cin >> a >> b;

    int inv = inverse((a % 26 + 26) % 26);
    if (inv == -1) {
        cout << "Key a must be coprime with 26";
        return 0;
    }

    // Encryption: C = (aP + b) mod 26
    for (char x : pt)
        ct += char(((a * (x - 'a') + b) % 26 + 26) % 26 + 'a');

    // Decryption: P = a inverse * (C - b) mod 26
    for (char x : ct)
        dt += char(((inv * ((x - 'a' - b + 26) % 26)) % 26) + 'a');

    cout << "Ciphertext: " << ct << endl;
    cout << "Plaintext: " << dt << endl;
    return 0;
}
