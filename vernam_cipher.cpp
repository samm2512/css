#include <iostream>
#include <string>
using namespace std;

int main() {
    string pt, key, ct = "", dt = "";

    cout << "Enter lowercase plaintext: ";
    cin >> pt;

    cout << "Enter lowercase key: ";
    cin >> key;

    if (pt.size() != key.size()) {
        cout << "Key length must match";
        return 0;
    }

    // Encryption
    for (int i = 0; i < (int)pt.size(); i++)
        ct += char((pt[i] - 'a' + key[i] - 'a') % 26 + 'A');

    // Decryption
    for (int i = 0; i < (int)ct.size(); i++)
        dt += char((ct[i] - 'A' - (key[i] - 'a') + 26) % 26 + 'a');

    cout << "Ciphertext: " << ct << endl;
    cout << "Decrypted: " << dt << endl;

    return 0;
}