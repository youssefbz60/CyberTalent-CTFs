# Genfei

**Category:** Cryptography | **Status:** Solved

## Challenge description
We get an encrypted file, `flag.enc`, and the script that created it, `encrypt.py`. The goal is to decrypt the flag.

```
genfei/
├── challenge/
│   ├── encrypt.py     # original script (Python 2)
│   └── flag.enc       # 32 bytes = 2 blocks of 16 bytes
└── solve/
    └── decrypt.py     # my solution (Python 3)
```

## Approach

### 1. Read the encryption code
- It is **Python 2** (`xrange`).
- The plaintext is padded with `#` until its length is a multiple of 16, then encrypted **block by block** (16 bytes = four 32-bit numbers `a, b, c, d`).
- There is **no key**. The security only depends on the algorithm staying secret, so if we understand it, we can undo it.
- Each block goes through **32 rounds**, and each round has **two transformations** built from a helper function `F(w)`.

### 2. The key idea: every step can be undone
In each transformation, every new value is an old value XOR-ed with `F(...)` of other values. XOR is reversible, so we only need to recover the other values first, in the right order.

For the first transformation (the second one follows the same idea with `1337`, and the roles of the variables are shifted, so there the recovery starts with `d`):

| New value | Formula | How to recover the old one |
|-----------|---------|-----------------------------|
| `d_new` | `a ^ 31337` | `a = d_new ^ 31337` |
| `c_new` | `d ^ F(a \| F(a) ^ a)` | now `a` is known, so `d = c_new ^ F(a \| F(a) ^ a)` |
| `b_new` | `c ^ F(a ^ F(d) ^ (a \| d))` | `a` and `d` are known, so recover `c` |
| `a_new` | `b ^ F(a \| F(c ^ F(d)) ^ F(a \| c) ^ d)` | `a`, `c`, `d` are known, so recover `b` |

So the recovery order is **a, then d, then c, then b**. To decrypt, I apply the two transformations in **reverse order**, 32 times.

### 3. Write the decryption script
`solve/decrypt.py` does exactly this for each 16-byte block, then removes the `#` padding.
It is written for Python 3, so `xrange` became `range` and files are read in binary mode.

## How to run
The script reads `flag.enc` from the current folder, so run it from `challenge/`:

```bash
cd cryptography/genfei/challenge
python3 ../solve/decrypt.py
```

Output:
```
Decrypted bytes: b'FLAG{G3N3R4L123D_F31573L_EZ!}'
Flag: FLAG{G3N3R4L123D_F31573L_EZ!}
```

## Solution
Flag: `FLAG{G3N3R4L123D_F31573L_EZ!}`

## Tools used
Python 3 (`struct` module for packing and unpacking 32-bit integers)

## What I learned
- A cipher with no secret key is only obscurity: reading the code is enough to break it.
- XOR-based constructions are easy to invert when each step uses values you can already recover.
- Python 2 code needs small changes to run on Python 3 (`xrange`, bytes vs strings).
