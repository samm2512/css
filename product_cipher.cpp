// Product Cipher: Affine substitution followed by transposition
#include <iostream>
#include <string>
using namespace std;

int inverse(int a) {
    for (int i = 1; i < 26; i++)
        if ((a * i) % 26 == 1) return i;
    return -1;
}

int main() {
    string pt, sub = "", ct = "", rev = "", recovered = "";
    int a, b;

    cout << "Enter lowercase plaintext: ";
    cin >> pt;
    cout << "Enter key a and key b: ";
    cin >> a >> b;

    if (inverse(a) == -1) {
        cout << "Invalid key a";
        return 0;
    }

    // Affine substitution
    for (char ch : pt)
        sub += char(((a * (ch - 'a') + b) % 26) + 'a');

    // Transposition: even indexes first, then odd indexes
    for (int i = 0; i < (int)sub.size(); i += 2) ct += sub[i];
    for (int i = 1; i < (int)sub.size(); i += 2) ct += sub[i];

    // Reverse transposition
    int first = (ct.size() + 1) / 2, x = 0, y = first;
    for (int i = 0; i < (int)ct.size(); i++)
        rev += (i % 2 == 0) ? ct[x++] : ct[y++];

    // Reverse affine substitution
    int inv = inverse(a);
    for (char ch : rev)
        recovered += char(((inv * ((ch - 'a' - b + 26) % 26)) % 26) + 'a');

    cout << "Substitution: " << sub << endl;
    cout << "Ciphertext: " << ct << endl;
    cout << "Recovered plaintext: " << recovered << endl;
    return 0;
}
