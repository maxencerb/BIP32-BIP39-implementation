import os
from word_list import word_list
import hashlib
import sys
from utils import padd_binary

def create_seed(entropy_size=16):
    entropy_bytes = os.urandom(entropy_size)
    entropy = bin(int.from_bytes(entropy_bytes, byteorder='big'))[2:]
    entropy = padd_binary(entropy, 128)
    entropy_hash = bin(int.from_bytes(hashlib.sha256(entropy_bytes).digest(), byteorder='big'))[2:]
    entropy_hash = padd_binary(entropy_hash, 256)
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
    print(seed, len(seed))
    print(get_mnemonic(seed))
    print(get_hex(seed), len(get_hex(seed)))

if __name__ == '__main__':
    main()