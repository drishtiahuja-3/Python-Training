import hashlib
password = input("enter password")
print("password is :", password)
#sha = secure hash 256 technique
#or 512 technique
#utf universal transformation code
password = password.encode('utf-8')

password_encrypted = hashlib.sha256(password).hexdigest()
print("password is :", password_encrypted)