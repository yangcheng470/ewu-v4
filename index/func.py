#!/usr/bin/env python
import hashlib
import random

def generate_salt():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    chars += '0123456789'
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    salt = ''
    for i in range(0, 64):
        index = random.randint(0, len(chars)-1)
        salt += chars[index]

    return salt

def encrypt_pwd(plain_pwd, salt):
    if not len(salt)==64:
        return None
    # First step should be md5 in order to be compatible
    plain_pwd = hashlib.md5(plain_pwd.encode()).hexdigest()
    plain_pwd += salt
    encrypt_pwd = hashlib.sha512(plain_pwd.encode()).hexdigest()
    return encrypt_pwd


if __name__ == '__main__':
    salt = generate_salt()
    print(salt)
    print(encrypt_pwd('hello', salt))
