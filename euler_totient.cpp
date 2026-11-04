#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

int phi(int n) {
    if (n == 1) return 0;
    if (isPrime(n)) return n - 1;

    int result = n, temp = n;
    // Apply Euler's formula for each distinct prime factor.
    for (int p = 2; p * p <= temp; p++) {
        if (temp % p == 0) {
            while (temp % p == 0) temp /= p;
            result -= result / p;
        }
    }
    // Handle a prime factor left after the loop.
    if (temp > 1) result -= result / temp;
    return result;
}

int main() {
    int n;

    cout << "Enter n: ";
    cin >> n;

    if (n < 1) {
        cout << "Enter a positive integer";
        return 0;
    }

    cout << "Phi(" << n << ") = " << phi(n) << endl;
    return 0;
}

/*
How the program works:
1. The user enters a positive integer n.
2. The program finds the distinct prime factors of n.
3. For each prime factor p, it applies:
       result = result - result / p
4. The final result is Euler's totient phi(n), which counts the numbers
   from 1 to n that are relatively prime to n.
*/
