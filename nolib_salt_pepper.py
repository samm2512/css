def hash_password(text):
    h = 0

    for ch in text:
        h = (h * 31 + ord(ch)) % 1000000007

    return str(h)


password = input("Enter password: ")

salt = "A7x9"
pepper = "CollegeSecret"

# Add password, salt and pepper
combined = password + salt + pepper

# Generate hash
stored_hash = hash_password(combined)

print("Salt:", salt)
print("Stored Hash:", stored_hash)

# Verify password
attempt = input("Re-enter password: ")

check_hash = hash_password(attempt + salt + pepper)

if check_hash == stored_hash:
    print("Password verified")
else:
    print("Wrong password")