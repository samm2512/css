#include <iostream>
#include <string>
using namespace std;

int main() {
    string pt, ct = "", dt = "";

    cout << "Enter plaintext: ";
    cin >> pt;

    // Take even positions first (2, 4, 6...)
    for (int i = 1; i < (int)pt.size(); i += 2)
        ct += pt[i];

    // Then take odd positions (1, 3, 5...)
    for (int i = 0; i < (int)pt.size(); i += 2)
        ct += pt[i];

    // Restore original positions
    int evenCount = pt.size() / 2, x = 0, y = evenCount;
    for (int i = 0; i < (int)ct.size(); i++)
        dt += (i % 2 == 0) ? ct[y++] : ct[x++];

    cout << "Ciphertext: " << ct << endl;
    cout << "Recovered plaintext: " << dt << endl;
    return 0;
}
