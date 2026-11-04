import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

p, q = map(int, input("Enter two distinct primes p and q: ").split())
message = int(input("Enter message number (< n): "))

if not is_prime(p) or not is_prime(q) or p == q:
    print("Invalid prime numbers")
else:
    n = p*q
    phi = (p-1)*(q-1)
    if not 0 <= message < n:
        print("Message must be between 0 and n-1")
    else:
        # Generate public and private exponents
        e = next(x for x in range(2, phi) if math.gcd(x, phi) == 1)
        d = next(x for x in range(1, phi) if (e*x) % phi == 1)

        # Sign with private key and verify with public key
        signature = pow(message, d, n)
        verified = pow(signature, e, n)
        print("Signature:", signature)
        print("Verified message:", verified)
        print("Signature is VALID" if verified == message else "Signature is INVALID")
# Classroom RSA demonstration; real signatures sign a cryptographic hash using secure padding.
