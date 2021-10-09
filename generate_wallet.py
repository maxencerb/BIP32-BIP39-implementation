from word_list import word_list
import hashlib
import sys
from utils import padd_binary
from ecdsa import ECDH, SECP256k1, SigningKey, VerifyingKey
import binascii

def import_mnemonic(mnemonic):
    mnemonic_list = mnemonic.split(" ")

    if len(mnemonic_list) != 12:
        raise ValueError("Invalid mnemonic length")
    
    for word in mnemonic_list:
        if word not in word_list:
            raise ValueError(f"{word} is not a valid word for an english mnemonic")

    numbers = [word_list.index(word) for word in mnemonic_list]
    result = ""
    for n in numbers:
        bin_number = bin(n)[2:]
        result += padd_binary(bin_number, 11)
    return result

def is_seed_valid(seed_bits: str):
    first_bits = seed_bits[:128]
    seed_bytes = from_bitstring_to_byte(first_bits)
    hash = hashlib.sha256(seed_bytes).digest()
    hash_bits = bin(int.from_bytes(hash, 'big'))[2:]
    return hash_bits[:4] == seed_bits[128:]


def from_bitstring_to_byte(bitstring):
    number = int(bitstring, 2)
    return number.to_bytes(32, byteorder='big')


def get_masters(mnemonic):
    bitstring = import_mnemonic(mnemonic)
    seed =  from_bitstring_to_byte(bitstring)

    # Get master private key and chaincode
    sha = hashlib.sha512(seed).digest()
    binary_string = bin(int.from_bytes(sha, sys.byteorder))[2:]
    for _ in range(512 - len(binary_string)):
        binary_string = "0" + binary_string
    private_key = from_bitstring_to_byte(binary_string[:256])
    chain_code = from_bitstring_to_byte(binary_string[256:])
    hashlib.sha512(private_key)

    # Get master public key
    public_key = get_public_key(private_key)
    return private_key, public_key, chain_code

def get_public_key(private_key: bytes):
    signing_key = SigningKey.from_string(private_key, curve=SECP256k1, hashfunc=hashlib.sha256)
    ecdh = ECDH(curve = SECP256k1, private_key=signing_key)
    public_key: VerifyingKey = ecdh.get_public_key()
    return public_key.to_string()

# import random
# def generate_key(self):
#     big_int = self.__generate_big_int()
#     big_int = big_int % (self.CURVE_ORDER - 1) # key < curve order
#     big_int = big_int + 1 # key > 0
#     key = hex(big_int)[2:]
#     return key

# def __generate_big_int(self):
#     if self.prng_state is None:
#         seed = int.from_bytes(self.pool, byteorder='big', signed=False)
#         random.seed(seed)
#         self.prng_state = random.getstate()
#     random.setstate(self.prng_state)
#     big_int = random.getrandbits(self.KEY_BYTES * 8)
#     self.prng_state = random.getstate()
#     return big_int