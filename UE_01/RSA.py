import doctest
from sympy import randprime
import math
import argparse


def get_e(phi):
    # nach angaben aus diesem viedeo https://www.youtube.com/watch?v=X2yDcLE77To ist 65537 Standartwert für e
    e = 65537
    # e muss -> 1 < e < phi(N) und ggt(e und phi(N) ) muss 1 sein
    if math.gcd(e, phi) == 1:
        return e

    #fallback falls sich ergibt das 65537 nicht funkt
    for e in range(3, phi, 2):
        if math.gcd(e, phi) == 1:
            return e


def generate_keys(number_of_bits):
    halfbits = number_of_bits / 2
    q = randprime(pow(2,halfbits -1), pow(2,halfbits))
    p = randprime(pow(2,halfbits -1), pow(2,halfbits))
    while q == p:
        p = randprime(pow(2,halfbits -1), pow(2,halfbits))
    
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(phi)
    d = pow(e, -1, phi)

    keylength = n.bit_length()
    public_key = (e, n, keylength)
    private_key = (d, n, keylength)
    return public_key, private_key

def save_key(path, key):
    with open(path, "w") as f:
        f.write("\n".join(map(str, key)))

def load_key(path):
    with open(path, "r") as f:
        e, n, l = f.read().splitlines()
        return int(e), int(n), int(l)

def files2blocks(path, length):#
    max_block_size = (length // 8) - 1
    #red a file as a stream of bytes
    with open(path, "rb") as f:
        #read a "block" of bytes as long as it exists
        while block := f.read(max_block_size):
            #return the "block" as an iterable
            yield int.from_bytes(block, byteorder="big")

def encrypt_blocks(blocks, e,n):
    #encrypts a stream of blocks 1 by 1 and returns them as an iterable
    for block in blocks:
        yield pow(block, e, n)

def encrypt(path, public_key, out):
    e, n, length = public_key
    with open(out, "w") as f:
        for block in encrypt_blocks(files2blocks(path, length), e,n):
            f.write(str(block) + "\n")



def read_dirty(path):
    with open(path, "r") as f:
        return f.readlines()

def lines_to_blocks(lines):
    for line in lines:
        yield int(line)

def decrypt_blocks(blocks,d,n):
    for block in blocks:
        yield pow(block, d, n)

def decrypt(path, private_key, out):
    d, n, length = private_key
    maxblock_size = (length // 8) - 1
    lines = read_dirty(path)
    blocks = lines_to_blocks(lines)
    decrypted_blocks = decrypt_blocks(blocks,d,n)
    with open(out, "wb") as f:
        for block in decrypted_blocks:
            f.write(block.to_bytes((block.bit_length() + 7) // 8, 'big'))









#stack overflow: (LINK)[https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python]
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def powcustom(base, exponent, modulo)-> int:
    """
    test the multiplicative inverse
    >>> powcustom(3,-1,7)
    5

    test big numbers
    >>> powcustom (115,223,27)
    16

    """

    #calculate the multiplicative inverse
    if exponent < 0:
        base = modinv(base, modulo)
        exponent = -exponent
    #if the exponent is set to 0  return 1 % <modulo>
    if exponent == 0:
        return 1 % modulo
    #if the expnent is 1 return 
    if exponent == 1:
        return base % modulo

    if (exponent%2 == 0):
        half = powcustom(base, exponent // 2, modulo)
        return (half * half) % modulo
    else:
        half = powcustom(base, (exponent-1) // 2, modulo)
        return (half * half * base) % modulo

#readfile("clean.txt")
#publickey, privatekey = generate_keys(1024)
#encrypt("clean.txt",publickey, out="dirty.txt")
#decrypt("dirty.txt", privatekey, out="burger.txt")

def main():
    parser = argparse.ArgumentParser(description="Simple RSA CLI Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-k", "--keygen", type=int, help="generate new keys with given length")
    group.add_argument("-e", "--encrypt", help="encrypt file")
    group.add_argument("-d", "--decrypt", help="decrypt file")

    args = parser.parse_args()

    if args.keygen:
        pub, priv = generate_keys(args.keygen)
        save_key("public.key", pub)
        save_key("private.key", priv)
        print(f"✅ Generated {args.keygen}-bit key pair:")
        print("  → public.key")
        print("  → private.key")

    elif args.encrypt:
        pub = load_key("public.key")
        outfile = args.encrypt + ".enc"
        encrypt(args.encrypt, pub, outfile)
        print(f"✅ Encrypted file written to {outfile}")

    elif args.decrypt:
        priv = load_key("private.key")
        outfile = args.decrypt + ".dec"
        decrypt(args.decrypt, priv,outfile)
        print(f"✅ Decrypted file written to {outfile}")


if __name__ == "__main__":
    main()


#cli usage:
# Generate keypair
#python rsa.py -k 1024

# Encrypt plaintext
#python rsa.py -e message.txt

# Decrypt ciphertext
#python rsa.py -d message.txt.enc

