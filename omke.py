import time

# ---------------- MD5 IMPLEMENTATION ----------------

def left_rotate(x, n):
    x &= 0xFFFFFFFF
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


def md5(message):

    # Convert message into bytes
    data = bytearray(message)

    original_length = len(data) * 8

    # Padding
    data.append(0x80)

    while len(data) % 64 != 56:
        data.append(0)

    data += original_length.to_bytes(8, 'little')

    # Initial hash values
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Shift amounts
    S = [
        7,12,17,22, 7,12,17,22, 7,12,17,22, 7,12,17,22,
        5,9,14,20, 5,9,14,20, 5,9,14,20, 5,9,14,20,
        4,11,16,23, 4,11,16,23, 4,11,16,23, 4,11,16,23,
        6,10,15,21, 6,10,15,21, 6,10,15,21, 6,10,15,21
    ]

    # MD5 constants
    K = [
        0xd76aa478,0xe8c7b756,0x242070db,0xc1bdceee,
        0xf57c0faf,0x4787c62a,0xa8304613,0xfd469501,
        0x698098d8,0x8b44f7af,0xffff5bb1,0x895cd7be,
        0x6b901122,0xfd987193,0xa679438e,0x49b40821,
        0xf61e2562,0xc040b340,0x265e5a51,0xe9b6c7aa,
        0xd62f105d,0x02441453,0xd8a1e681,0xe7d3fbc8,
        0x21e1cde6,0xc33707d6,0xf4d50d87,0x455a14ed,
        0xa9e3e905,0xfcefa3f8,0x676f02d9,0x8d2a4c8a,
        0xfffa3942,0x8771f681,0x6d9d6122,0xfde5380c,
        0xa4beea44,0x4bdecfa9,0xf6bb4b60,0xbebfbc70,
        0x289b7ec6,0xeaa127fa,0xd4ef3085,0x04881d05,
        0xd9d4d039,0xe6db99e5,0x1fa27cf8,0xc4ac5665,
        0xf4292244,0x432aff97,0xab9423a7,0xfc93a039,
        0x655b59c3,0x8f0ccc92,0xffeff47d,0x85845dd1,
        0x6fa87e4f,0xfe2ce6e0,0xa3014314,0x4e0811a1,
        0xf7537e82,0xbd3af235,0x2ad7d2bb,0xeb86d391
    ]

    # Process 512-bit blocks
    for offset in range(0, len(data), 64):

        block = data[offset:offset + 64]

        M = [
            int.from_bytes(block[i:i+4], 'little')
            for i in range(0, 64, 4)
        ]

        a, b, c, d = A, B, C, D

        for i in range(64):

            if i < 16:
                F = (b & c) | (~b & d)
                g = i

            elif i < 32:
                F = (d & b) | (~d & c)
                g = (5*i + 1) % 16

            elif i < 48:
                F = b ^ c ^ d
                g = (3*i + 5) % 16

            else:
                F = c ^ (b | ~d)
                g = (7*i) % 16

            F = (F + a + K[i] + M[g]) & 0xFFFFFFFF

            a, d, c, b = (
                d,
                c,
                b,
                (b + left_rotate(F, S[i])) & 0xFFFFFFFF
            )

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    result = (
        A.to_bytes(4, 'little') +
        B.to_bytes(4, 'little') +
        C.to_bytes(4, 'little') +
        D.to_bytes(4, 'little')
    )

    return result.hex()


# ---------------- SHA-1 IMPLEMENTATION ----------------

def sha1(message):

    data = bytearray(message)

    original_length = len(data) * 8

    # Padding
    data.append(0x80)

    while len(data) % 64 != 56:
        data.append(0)

    data += original_length.to_bytes(8, 'big')

    # Initial hash values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Process 512-bit blocks
    for offset in range(0, len(data), 64):

        block = data[offset:offset + 64]

        W = [
            int.from_bytes(block[i:i+4], 'big')
            for i in range(0, 64, 4)
        ]

        # Extend to 80 words
        for i in range(16, 80):
            value = W[i-3] ^ W[i-8] ^ W[i-14] ^ W[i-16]
            W.append(
                ((value << 1) | (value >> 31)) & 0xFFFFFFFF
            )

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):

            if i < 20:
                f = (b & c) | (~b & d)
                k = 0x5A827999

            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1

            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (
                ((a << 5) | (a >> 27)) +
                f + e + k + W[i]
            ) & 0xFFFFFFFF

            e = d
            d = c
            c = ((b << 30) | (b >> 2)) & 0xFFFFFFFF
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return (
        f"{h0:08x}{h1:08x}{h2:08x}"
        f"{h3:08x}{h4:08x}"
    )


# ---------------- MAIN PROGRAM ----------------

# Create a 1 KB text file
with open("sample.txt", "wb") as file:
    file.write(b"A" * 1024)

# Read file
with open("sample.txt", "rb") as file:
    data = file.read()

print("File size:", len(data), "bytes")

# MD5 timing
start = time.perf_counter()
md5_hash = md5(data)
md5_time = time.perf_counter() - start

# SHA-1 timing
start = time.perf_counter()
sha1_hash = sha1(data)
sha1_time = time.perf_counter() - start

# Results
print("\nMD5 HASH:", md5_hash)
print("MD5 TIME:", md5_time, "seconds")

print("\nSHA-1 HASH:", sha1_hash)
print("SHA-1 TIME:", sha1_time, "seconds")

print("\nPerformance Comparison")

if md5_time < sha1_time:
    print("MD5 is faster for this run")
else:
    print("SHA-1 is faster for this run")