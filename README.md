# CyberTalent CTF Writeups

My solutions and notes for the CyberTalent challenges I have solved so far (cryptography and Linux).
I write each one the way I would explain it to a classmate: what I saw, what I tried, what worked, and what I learned.

## Challenges

| Category | Challenge | Skills practiced | Status |
|----------|-----------|------------------|--------|
| Cryptography | [Crack the Hash](./cryptography/crack-the-hash/) | Hash identification, MD5 lookup | Solved |
| Cryptography | [Guess The Password](./cryptography/guess_the_password/) | SHA-1 lookup | Solved |
| Cryptography | [Genfei](./cryptography/genfei/) | Reading Python 2 code, inverting a custom block cipher | Solved |
| Cryptography | [Arithmetic](./cryptography/arithmetic/) | Analysing a custom cipher | In progress |
| Linux | [Linux Task 1](./bash/task_1/) | Hidden files, `file`, `find`, ZIP cracking with John, base64, ROT13 | Solved |

## Repository layout

```
.
├── bash/
│   └── task_1/              # Linux challenge: writeup
├── cryptography/
│   ├── arithmetic/          # challenge/ + solve/ (in progress)
│   ├── crack-the-hash/
│   ├── genfei/              # challenge/ + solve/decrypt.py
│   └── guess_the_password/
└── README.md
```

Each challenge folder has its own `README.md` with the description, my approach, the solution and what I learned.

## Tools I used

- **Python 3**: custom decryption scripts
- **John the Ripper** (`zip2john`, `john`): cracking a ZIP password in the Linux challenge
- **hashes.com** and **md5hashing.net**: online hash lookups
- **CyberChef**: quick decoding
- **Linux basics**: `ls`, `cat`, `file`, `find`, `strings`, `tar`, `base64`

## How to run the scripts

The solve scripts use **Python 3**. The original challenge scripts are written in Python 2 and are kept only for reference.
Every writeup shows the exact command to run, for example:

```bash
cd cryptography/genfei/challenge
python3 ../solve/decrypt.py
```

## Disclaimer

The challenges belong to CyberTalent. These writeups are shared for learning only.
If you are still working on one of them, try it yourself first, then come back here when you are stuck.

## Author

**Youssef Bouyzourn**, engineering student at ENSA Khouribga.
[LinkedIn](https://www.linkedin.com/in/youssef-bouyzourn-047b4b339/) · [GitHub](https://github.com/youssefbz60)

## License

MIT. See [LICENSE](LICENSE).
