import hashlib
import time

data = b"A" * 1024  # 1 KB message

start = time.perf_counter()
md5_hash = hashlib.md5(data).hexdigest()
md5_time = time.perf_counter() - start

start = time.perf_counter()
sha1_hash = hashlib.sha1(data).hexdigest()
sha1_time = time.perf_counter() - start

print("MD5:", md5_hash)
print("SHA-1:", sha1_hash)
print("MD5 time (seconds):", md5_time)
print("SHA-1 time (seconds):", sha1_time)
print("Note: MD5 and SHA-1 are obsolete for security-sensitive use.")
