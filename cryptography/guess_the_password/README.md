# Guess The Password

**Category:** Cryptography | **Status:** Solved

## Challenge description
Another leaked hash, and again the goal is to recover the password.

```
06f8aa28b9237866e3e289f18ade19e1736d809d
```

## Approach
1. **Identify the hash.** It is 40 hexadecimal characters, which matches **SHA-1**. (RIPEMD-160 has the same length, so a tool such as `hashid` helps to double-check.)
2. **Look it up.** I searched the hash on `hashes.com`, which has a large database of SHA-1 hashes, and it returned the plaintext.
3. **Verify the answer** by hashing it myself:

```bash
printf 'jrahyn+' | sha1sum
# 06f8aa28b9237866e3e289f18ade19e1736d809d  -
```
The output matches the challenge hash.

## Solution
Password: `jrahyn+`

## Tools used
`hashes.com`, `sha1sum`

## What I learned
- Same method as [Crack the Hash](../crack-the-hash/): identify, look up, verify.
- SHA-1 is longer than MD5 (40 characters instead of 32), but it is just as weak against dictionary lookups when the password is simple.
- A special character at the end of a password (`+`) does not protect it if the hash is already in a public database.
