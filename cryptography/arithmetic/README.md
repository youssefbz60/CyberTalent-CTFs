# Arithmetic

**Category:** Cryptography | **Status:** In progress

## Challenge description
We get a script that encrypts a flag with a random 32-byte key, and the resulting ciphertext.

```
arithmetic/
├── challenge/
│   ├── encrypt.py     # original script (Python 2)
│   └── ciphertext     # hex string, 22 bytes
└── solve/
    └── solve.py       # work in progress
```

## What the script does
- A 256-bit `state` is created by hashing the random key.
- For each character, 32 mini-steps run. Each mini-step picks an operation (`+`, `^`, `-` or `*`) and a value from the current `state`, applies it to the character, then updates `state` with a polynomial function (`STEP`).
- After each character, the result is XOR-ed back into `state`.

## Notes so far
- The key is random, so a plain brute force on the key is not an option.
- Next step: look at which bits of `state` actually decide the operation and the value used on the character, and how that changes the number of possibilities to try.

## Status
Not solved yet. I will update this page with the approach, the script and the flag once it is done.
