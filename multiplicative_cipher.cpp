#include <iostream>
#include <string>
using namespace std;

int inverse(int key) {
    for (int i = 1; i < 26; i++)
        if ((key * i) % 26 == 1) return i;
    return -1;
}

int main() {
    string pt, ct = "", dt = "";
    int key;

    cout << "Enter lowercase plaintext: ";
    cin >> pt;
    cout << "Enter key (coprime with 26): ";
    cin >> key;

    key = (key % 26 + 26) % 26;
    int inv = inverse(key);

    if (inv == -1) {
        cout << "Invalid key";
        return 0;
    }

    // Encryption
    for (char c : pt)
        ct += char(((c - 'a') * key) % 26 + 'A');

    // Decryption
    for (char c : ct)
        dt += char(((c - 'A') * inv) % 26 + 'a');

    cout << "Ciphertext: " << ct << endl;
    cout << "Plaintext: " << dt << endl;

    return 0;
}