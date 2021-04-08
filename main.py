import requests

import sys

import hashlib


def request_pwned(password_first, password_last):
    url = 'https://api.pwnedpasswords.com/range/' + password_first
    res = requests.get(url)
    hash_pass = (line.split(':') for line in res.text.splitlines())
    for hashes, count in hash_pass:
        if hash == password_last:
            return count
    return 0


def pass_check(password):
    password_hashed = hashlib.sha1(password.encode()).hexdigest().upper()
    first5_hash = password_hashed[:5]
    last_hash = password_hashed[5:]
    print(f'Checking password: {password}')
    occurrence = request_pwned(first5_hash, last_hash)
    if occurrence:
        print(f'It has been used {occurrence} times')
    else:
        print('You are safe, password never used before')


if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        pass_check(sys.argv[i])
