# Linux Task 1

**Category:** Linux | **Status:** Solved

## Challenge description
We receive an archive, `linux_chal.tar.gz`. Inside there is a chain of folders and files, and the goal is to follow the clues until we reach the flag.

## Approach
The challenge is a chain of small steps. Each folder name hints at what to do next.

### 1. Extract and look around
```bash
tar -xzvf linux_chal.tar.gz
cd cat
ls -a            # -a shows hidden files, which is how .pass.txt appears
cat .pass.txt
```
The hidden file `.pass.txt` only shows up with `ls -a`, because its name starts with a dot.

### 2. The `exec` folder
It contains an executable whose name is just `-`.
```bash
file ./-         # ELF 64-bit executable
./-              # prints: Here is your password: 'passforasciiii'
```
The `./` matters: a bare `-` is read as an option or as standard input by most commands, not as a file name.

### 3. The `ascii` folder
Nine files (`f0` to `f8`), but only one of them is readable text.
```bash
file *           # only f6 says "ASCII text", the others are "data"
cat f6           # thisisasciiiiiprintapleeeee
```

### 4. The `size37` folder
Seven small text files named `test1` to `test7`. The folder name is the clue: look for the file that is exactly 37 bytes.
```bash
find . -maxdepth 1 -type f -size 37c     # ./test5
cat test5                                # thissssisssthepasswordfornexxtfileeee
```

### 5. The `next` folder: cracking the ZIP
Two big text files (`nexttocybertalents` and `NumberOne/one`) are password wordlists. Next to them, `hash.txt` holds a ZIP hash (the format produced by `zip2john`) for `decodeme1.zip`.
```bash
john --wordlist=<wordlist> hash.txt      # try the wordlists from this challenge
john --show hash.txt                     # display the cracked password
```
This is a dictionary attack: John tries every word in the list until one opens the ZIP.

### 6. Decoding the last layer
Inside the ZIP there is a file `pass` containing a base64 string, and a second archive, `decodeme2`.
```bash
echo "dXNlbWVhc3Bhc3N3b3Jk" | base64 -d  # usemeaspassword
```
That password opens the last archive. It contains `flag.txt`, and the flag in it is encoded with ROT13:
```bash
cat flag.txt                             # synt{f1zcyr_yvahk_101}
echo "synt{f1zcyr_yvahk_101}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

## Solution
Flag: `flag{s1mple_linux_101}`

## Tools used
`tar`, `ls`, `cat`, `file`, `find`, `strings`, `zip2john`, `john`, `base64`, `tr`

## What I learned
- Hidden files start with a dot and need `ls -a`.
- A file named `-` must be called as `./-`.
- `file` and `find -size` are fast ways to pick the one useful file out of many.
- ZIP passwords can be recovered with a wordlist attack, using `zip2john` to extract the hash first.
- ROT13 is its own inverse, so the same `tr` command encodes and decodes.
