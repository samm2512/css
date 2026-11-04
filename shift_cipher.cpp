#include <iostream>
#include <string>
using namespace std;

int main() {
    string pt, ct = "", dt = "";
    int key;

    cout << "Enter lowercase plaintext: ";
    cin >> pt;
    cout << "Enter key: ";
    cin >> key;
    key = (key % 26 + 26) % 26;

    // Encryption
    for (char c : pt)
        ct += char((c - 'a' + key) % 26 + 'a');

    // Decryption
    for (char c : ct)
        dt += char((c - 'a' - key + 26) % 26 + 'a');

    cout << "Ciphertext: " << ct << endl;
    cout << "Decrypted: " << dt << endl;
    return 0;
}
