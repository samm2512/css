p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))
x = int(input("Enter Alice private key x: "))
y = int(input("Enter Bob private key y: "))

# Public keys: A = g^x mod p and B = g^y mod p
A = pow(g, x, p)
B = pow(g, y, p)

# Both parties independently calculate the shared secret
alice_key = pow(B, x, p)
bob_key = pow(A, y, p)

print("Alice public key:", A)
print("Bob public key:", B)
print("Alice shared key:", alice_key)
print("Bob shared key:", bob_key)
print("Key exchange successful" if alice_key == bob_key else "Key exchange failed")
