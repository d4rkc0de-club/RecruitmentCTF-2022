#!/usr/bin/env python3

import random
# pip install pycryptodome
from Crypto.Util.number import getPrime

with open('flag.txt', 'rb') as f:
    flag = f.read()

msgs = [
    b'Never gonna give you up!',
    b'Never gonna let you down!',
    b'Never gonna run around and desert you!'
        ]

e = 3
msgs.append(flag)
msgs *= e
random.shuffle(msgs)

for msg in msgs:
    n = getPrime(1024) * getPrime(1024)
    m = int.from_bytes(msg, 'big')
    c = pow(m, 3, n)
    with open('encrypted-messages.txt', 'a') as f:
        f.write(f'n: {n}\n')
        f.write(f'e: {e}\n')
        f.write(f'c: {c}\n\n')
