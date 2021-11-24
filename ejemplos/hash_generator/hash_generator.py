import hashlib
password = "hpylpf10TW#"
hash_list = []
algoritmo = hashlib.sha256()
#algoritmo = hashlib.md5()
algoritmo.update(password.encode())
digest = algoritmo.digest()
print(digest.hex())