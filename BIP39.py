import os
from word_list import word_list
import hashlib

def create_seed(entropy_size=16):
    entropy_bytes = os.urandom(entropy_size)
    entropy = bin(int.from_bytes(entropy_bytes, byteorder='big'))[2:]
    for _ in range(128 - len(entropy)):
        entropy = '0' + entropy
    entropy_hash = bin(int.from_bytes(hashlib.sha256(entropy_bytes).digest(), byteorder='big')).zfill(256)[2:]
    for _ in range(256 - len(entropy_hash)):
        entropy_hash = '0' + entropy_hash
    return entropy + entropy_hash[:4]

def get_mnemonic(seed_bits):
    mnemonic = ''
    for i in range(0, len(seed_bits), 11):
        mnemonic += word_list[int(seed_bits[i:i+11], 2)] + ' '
    return mnemonic

def get_hex(seed_bits):
    return hex(int(seed_bits, 2))

def main():
    seed = create_seed()
    print(get_mnemonic(seed))
    print(get_hex(seed))

if __name__ == '__main__':
    main()