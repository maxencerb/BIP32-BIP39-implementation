from word_list import word_list

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def import_mnemonic(mnemonic):
    numbers = [word_list.index(word) for word in mnemonic]
    result = ""
    for n in numbers:
        result += str(bin(n)[2:].zfill(11))
    return bitstring_to_bytes(result)

def main():
    mnemonic = input("Enter your mnemonic: ").split(" ")
    
    

print()
    