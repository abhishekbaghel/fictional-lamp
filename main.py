import requests
import hashlib

# All python string are unicode
# Add your password here
password = b"password"

hash_object = hashlib.sha1(password)
digest = hash_object.hexdigest()

headers = {"Add-Padding": "true"}
x = requests.get(f"https://api.pwnedpasswords.com/range/{digest[:5]}", headers=headers)

suffix = str(digest[5:]).upper()

for record in x.text.split('\n'):
	if suffix in record:
		print(f"Occurances : {record.split(':')[1]}")
