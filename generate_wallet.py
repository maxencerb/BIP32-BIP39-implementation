from create_seed import create_seed
from word_list import word_list
import hashlib
import sys
from utils import padd_binary
from ecdsa.util import PRNG
from ecdsa import SigningKey, NIST256p
G = (
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
)

def import_mnemonic(mnemonic):
    numbers = [word_list.index(word) for word in mnemonic.split(" ")]
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
    private_key = bytes(int(binary_string[:256], 2))
    chain_code = bytes(int(binary_string[256:], 2))
    hashlib.sha512(private_key)

    # Get master public key
    public_key = get_public_key(private_key)
    return private_key, chain_code

def get_public_key(master_private_key: bytes):
    public_key = pow(G, master_private_key, G)
    return public_key

# def getChildren(mnemonic):
#     code = get_masters(mnemonic)[1]
#     child_private = Hash512(code)[0]
     
mnemonic = "wire crucial lazy thunder dynamic pear merit abstract pluck pistol way music"
seed = import_mnemonic(mnemonic)
print(seed)
print(sys.byteorder)
print(is_seed_valid(seed))

def getkeys():
    pub_k = SigningKey.generate(curve = NIST256p, entropy = create_seed())
    prv_k = pub_k.verifying_key
