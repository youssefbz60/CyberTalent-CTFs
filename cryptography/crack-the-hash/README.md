# Crack the Hash

**Category:** Cryptography | **Status:** Solved

## Challenge description
A hacker leaked the password hash of a company CEO. The goal is to recover the password.

```
1ab566b9fa5c0297295743e7c2a6ec27
```

## Approach
1. **Identify the hash.** It is 32 hexadecimal characters. That length matches MD5, so MD5 was my first guess. Other algorithms (MD4, NTLM) have the same length, so a tool such as `hashid` can confirm the type.
2. **Look it up.** MD5 hashes of common passwords are stored in public databases, which is much faster than brute force. I searched the hash on `md5hashing.net` and `hashes.com`, and the plaintext came back immediately.
3. **Verify the answer.** Never trust a lookup blindly: hash the plaintext yourself and compare.

```bash
printf 'Iamtheflag' | md5sum
# 1ab566b9fa5c0297295743e7c2a6ec27  -
```
The output matches the challenge hash, so the answer is correct. Use `printf` (or `echo -n`) so that no newline gets hashed with the password.

## Solution
Password: `Iamtheflag`

The challenge asked for the password itself, not a `FLAG{...}` format.

## Tools used
`md5hashing.net`, `hashes.com`, `md5sum`

## What I learned
- The length of a hash gives a first guess, but not a proof.
- Online databases only work for passwords that were already cracked by someone. A strong or unique password would need a real attack with Hashcat or John and a wordlist.
- Always verify a result by hashing it again.

## Going further
To practice the offline way, the same hash can be attacked with Hashcat (`-m 0` is MD5) and a wordlist such as `rockyou.txt`. Whether this password is in that list is something to test.
