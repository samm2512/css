#include <iostream>
#include <string>
using namespace std;

int main()
{
    string pt, ct = "", dt = "";
    int key;

    cout << "Enter plaintext: ";
    cin >> pt;

    cout << "Enter key (number of rails): ";
    cin >> key;

    int len = pt.length();

    // Create rail matrix
    char rail[100][100];

    // Initialize matrix with blank spaces
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            rail[i][j] = '\n';

    // Encryption: Fill characters in zigzag pattern
    int row = 0, dir = 1;

    for (int col = 0; col < len; col++)
    {
        rail[row][col] = pt[col];

        if (row == 0)
            dir = 1;
        else if (row == key - 1)
            dir = -1;

        row += dir;
    }

    // Read row by row to get ciphertext
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            if (rail[i][j] != '\n')
                ct += rail[i][j];

    cout << "\nEncrypted Text: " << ct;

    // Decryption: Mark zigzag positions
    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            rail[i][j] = '\n';

    row = 0;
    dir = 1;

    for (int col = 0; col < len; col++)
    {
        rail[row][col] = '*';

        if (row == 0)
            dir = 1;
        else if (row == key - 1)
            dir = -1;

        row += dir;
    }

    // Fill marked positions with ciphertext
    int index = 0;

    for (int i = 0; i < key; i++)
        for (int j = 0; j < len; j++)
            if (rail[i][j] == '*' && index < len)
                rail[i][j] = ct[index++];

    // Read zigzag pattern to recover plaintext
    row = 0;
    dir = 1;

    for (int col = 0; col < len; col++)
    {
        dt += rail[row][col];

        if (row == 0)
            dir = 1;
        else if (row == key - 1)
            dir = -1;

        row += dir;
    }

    cout << "\nDecrypted Text: " << dt;

    return 0;
}