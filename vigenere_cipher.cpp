#include <iostream>
#include <string>
using namespace std;

int main() {
    string pt, key, ct = "", dt = "";

    cout << "Enter lowercase plaintext: ";
    cin >> pt;

    cout << "Enter lowercase key: ";
    cin >> key;

    // Encryption using repeated key
    for (int i = 0; i < (int)pt.size(); i++)
        ct += char((pt[i] - 'a' + key[i % key.size()] - 'a') % 26 + 'A');

    // Decryption
    for (int i = 0; i < (int)ct.size(); i++)
        dt += char((ct[i] - 'A' - (key[i % key.size()] - 'a') + 26) % 26 + 'a');

    cout << "Ciphertext: " << ct << endl;
    cout << "Plaintext: " << dt << endl;

    return 0;
}