# Genfei

## 📝 Challenge Description
We are given a `flag.enc` file and an `encrypt.py` script. The script looks complicated. 
The goal is to decrypt the file.

## 🔍 My Approach
1.  I read `encrypt.py`. It's written in Python 2 (uses `xrange`). It encrypts the text in blocks of 16 bytes.
2.  It uses a custom function `F(w)` and does 32 rounds of XOR and OR operations.
3.  Since XOR is reversible, I wrote a decryption script. I reversed the order of the 32 rounds (from round 32 down to 1) and reversed the XOR operations.
4.  I also had to make sure my script runs on Python 3 (changing `xrange` to `range`).

## 🛠️ Tools Used
*   **Python 3**: To write the custom decryption script (`decrypt.py`).
*   **Basic Math logic**: Understanding how XOR and bitwise shifts work.

## 🚩 The Solution
I created the `decrypt.py` script. When I ran it against `flag.enc`, it printed the decrypted flag.

Run it yourself:
```bash
cd solve
python3 decrypt.py ```

The code looked scary at first, but breaking it down step-by-step made sense.
