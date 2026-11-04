# Diffie-Hellman MITM Attack

# Function to calculate (base^exp) % mod
def powerMod(base, exp, mod):
    result = 1

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        base = (base * base) % mod
        exp = exp // 2

    return result


# Input prime number and primitive root
p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))

# Input private keys
alicePrivate = int(input("Enter Alice's private key: "))
bobPrivate = int(input("Enter Bob's private key: "))
evePrivate = int(input("Enter Eve's private key: "))

# Generate public keys
alicePublic = powerMod(g, alicePrivate, p)
bobPublic = powerMod(g, bobPrivate, p)
evePublic = powerMod(g, evePrivate, p)

# Display public keys
print("\nAlice's Public Key =", alicePublic)
print("Bob's Public Key =", bobPublic)
print("Eve's Public Key =", evePublic)

# Alice receives Eve's public key instead of Bob's
aliceKey = powerMod(evePublic, alicePrivate, p)

# Bob receives Eve's public key instead of Alice's
bobKey = powerMod(evePublic, bobPrivate, p)

# Eve creates separate secret keys with Alice and Bob
eveAliceKey = powerMod(alicePublic, evePrivate, p)
eveBobKey = powerMod(bobPublic, evePrivate, p)

# Display secret keys
print("\nAlice's Secret Key =", aliceKey)
print("Eve's Key with Alice =", eveAliceKey)

print("\nBob's Secret Key =", bobKey)
print("Eve's Key with Bob =", eveBobKey)

# Check whether MITM attack is successful
if aliceKey == eveAliceKey and bobKey == eveBobKey:
    print("\nMITM Attack Successful!")
    print("Eve has established separate keys with Alice and Bob.")
else:
    print("\nMITM Attack Failed!")