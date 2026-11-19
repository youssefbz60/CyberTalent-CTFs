# Linux Task 1

## 📝 Challenge Description
We are given a file called `linux_chal.tar.gz`. We need to explore it and find the hidden flag.

## 🔍 My Approach
1.  First, I extracted the archive using the `tar` command.
2.  After extracting, I saw a lot of folders and weird files.
3.  I used the `tree` command to see the structure, and `find` to look for interesting files.
4.  I noticed some files looked like they had hidden data. I used `cat` and `strings` to read them.
5.  I kept following the folders until I found a file containing the flag.

## 🛠️ Tools Used
*   **tar**: To extract the file (`tar -xzvf linux_chal.tar.gz`).
*   **ls, cd, find**: To explore the folders.
*   **cat, file**: To read what's inside the files.

## 🚩 The Solution
(Here you can put the flag you found, and a small tip on where exactly it was hidden, like inside a file named `real_flag.txt`).
