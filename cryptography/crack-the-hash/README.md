# Crack the Hash

## 📝 Challenge Description
The challenge says a hacker leaked a password hash online. We need to crack it to find the CEO's password. 
The hash is: `1ab566b9fa5c0297295743e7c2a6ec27`

## 🔍 My Approach
1.  First, I looked at the hash. It has 32 characters (hex). This means it is an **MD5** hash.
2.  Instead of using brute force, I used online databases first. It's faster.

## 🛠️ Tools Used
*   **md5hashing.net**: I searched for the hash here.
*   **hashes.com**: Another good database for cracking hashes.

## 🚩 The Solution
I pasted the hash into `md5hashing.net` and it found the result immediately. 
The plain text password is: `Iamtheflag`

*(Note: The challenge asked for the password, not a standard FLAG{} format, so the answer is just the password).*
