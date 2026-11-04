import hashlib

password = input("Enter password: ")
salt = "A7x9"                 # In practice, generate a unique random salt per user
pepper = "CollegeSecret"      # Keep pepper separate from the password database

# Demonstration hash: password + salt + pepper
stored_hash = hashlib.sha256((password + salt + pepper).encode()).hexdigest()
print("Salt:", salt)
print("Stored SHA-256 hash:", stored_hash)

attempt = input("Re-enter password: ")
check_hash = hashlib.sha256((attempt + salt + pepper).encode()).hexdigest()

if check_hash == stored_hash:
    print("Password verified")
else:
    print("Wrong password")
# Note: Production password storage should use Argon2id, scrypt or bcrypt.
