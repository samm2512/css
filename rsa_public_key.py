def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

p, q = map(int, input("Enter prime numbers p and q: ").split())
m = int(input("Enter plaintext number (less than n): "))

if not is_prime(p) or not is_prime(q) or p == q:
    print("Enter two distinct prime numbers")
else:
    n = p*q
    phi = (p-1)*(q-1)
    if not 0 <= m < n:
        print("Plaintext must be between 0 and n-1")
    else:
        # Choose e coprime to phi(n)
        e = next(x for x in range(2, phi) if __import__("math").gcd(x, phi) == 1)
        # Find d such that e*d = 1 mod phi(n)
        d = next(x for x in range(1, phi) if (e*x) % phi == 1)
        ct = pow(m, e, n)
        recovered = pow(ct, d, n)
        print("Public key:", (e, n))
        print("Private key:", (d, n))
        print("Ciphertext:", ct)
        print("Decrypted:", recovered)
