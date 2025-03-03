from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

text = "hello"
print(text, len(text))
for i in range(1,12):

    text = text+"A"
    cipher = AES.new(b64decode(b"YrJGzJOtABiGd2lzhHyvKw=="), AES.MODE_ECB)
    ct = cipher.encrypt(pad(text.encode(), 16))
    print(len(text), ct)