
import sys
from struct import pack, unpack

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32


def decrypt_block(block):

    a2, b2, c2, d2 = unpack("<4I", block)

    # Reverse the 32 rounds
    for _ in range(32):

        # Reverse the second transformation

        d1 = d2 ^ 1337

        a1 = c2 ^ F(d1 | F(d1) ^ d1)

        b1 = b2 ^ F(d1 ^ F(a1) ^ (d1 | a1))

        c1 = a2 ^ F(d1 | F(b1 ^ F(a1)) ^ F(d1 | b1) ^ a1)

        # Reverse the first transformation

        a0 = d1 ^ 31337

        d0 = c1 ^ F(a0 | F(a0) ^ a0)

        c0 = b1 ^ F(a0 ^ F(d0) ^ (a0 | d0))

        b0 = a1 ^ F(
            a0 | F(c0 ^ F(d0)) ^ F(a0 | c0) ^ d0
        )

        a2, b2, c2, d2 = a0, b0, c0, d0

    return pack("<4I", a2, b2, c2, d2)


# Read encrypted file as binary
with open("flag.enc", "rb") as f:
    ciphertext = f.read()

# Decrypt each 16-byte block
plaintext = b""

for i in range(0, len(ciphertext), 16):
    plaintext += decrypt_block(ciphertext[i:i+16])

# Remove '#' padding
plaintext = plaintext.rstrip(b"#")

print("Decrypted bytes:", plaintext)
print("Flag:", plaintext.decode("utf-8", errors="replace"))

