import os
from word_list import word_list
import hashlib
from utils import byte_to_binary

def create_seed(entropy_size=16):
    entropy_bytes = os.urandom(entropy_size)
    entropy = byte_to_binary(entropy_bytes, 128)
    hash = hashlib.sha256(entropy_bytes).digest()
    entropy_hash = byte_to_binary(hash, 256)
    return entropy + entropy_hash[:4]

def get_mnemonic(seed_bits):
    mnemonic = ''
    for i in range(0, len(seed_bits), 11):
        mnemonic += word_list[int(seed_bits[i:i+11], 2)] + ' '
    return mnemonic

def get_hex(seed_bits):
    return hex(int(seed_bits, 2))