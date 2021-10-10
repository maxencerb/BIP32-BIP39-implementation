from word_list import word_list
import hashlib
from utils import padd_binary, byte_to_binary
from ecdsa import ECDH, SECP256k1, SigningKey, VerifyingKey

def import_mnemonic(mnemonic: str):
    mnemonic_list = mnemonic.split(" ")
    if mnemonic_list[-1] == "":
        mnemonic_list = mnemonic_list[:-1]
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
    seed_bytes = from_bitstring_to_byte(first_bits, 16)
    hash = hashlib.sha256(seed_bytes).digest()
    hash_bits = byte_to_binary(hash, 256)
    return hash_bits[:4] == seed_bits[128:]


def from_bitstring_to_byte(bitstring, size=32):
    number = int(bitstring, 2)
    return number.to_bytes(size, byteorder='big')


def get_masters(mnemonic):
    bitstring = import_mnemonic(mnemonic)[:128]
    seed = from_bitstring_to_byte(bitstring, 16)

    # Get master private key and chaincode
    sha = hashlib.sha512(seed).digest()
    private_key = sha[:32]
    chain_code = sha[32:]
    # Get master public key
    public_key = get_public_key(private_key)
    return private_key, public_key, chain_code

def get_public_key(private_key: bytes):
    signing_key = SigningKey.from_string(private_key, curve=SECP256k1, hashfunc=hashlib.sha256)
    ecdh = ECDH(curve = SECP256k1, private_key=signing_key)
    public_key: VerifyingKey = ecdh.get_public_key()
    print(len(public_key.to_string()))
    return public_key.to_string()

def child_key(private_key: str, public_key: str, chain_code: str, index: int,extended = False):
    n = 5 #n = ?
    hash = hashlib.pbkdf2_hmac('sha512', public_key, chain_code,index)
    chain_code_child = hash[:32] +bytes(index)
    child_private_key = private_key + hash[32:] %n
    return child_private_key,chain_code_child 