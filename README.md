# Diffie-Hellman Key Exchange Protocol (Python Simulation)

This project demonstrates the logic, mathematical foundation, and Python implementation of the **Diffie-Hellman (DH) Key Exchange Protocol** for educational purposes in a Cryptography course.

The script simulates how two parties (Alice and Bob) can securely agree on a shared secret key over an insecure network without ever revealing their private keys.

## Table of Contents

- [Overview](#-overview)
- [How it Works (The Color Analogy)](#-how-it-works-the-color-analogy)
- [Mathematical Foundation](#-mathematical-foundation)
- [Installation & Usage](#-installation--usage)
- [Key Concepts & FAQ](#-key-concepts--faq-exam-prep)

---

## Overview

Published by Whitfield Diffie and Martin Hellman in 1976, this protocol is a cornerstone of modern cryptography. 

> **Core Concept:** It allows two parties who have never met before to jointly establish a shared secret key over an insecure channel (like the internet). This key can then be used to encrypt subsequent communications using symmetric encryption (like AES).

---

## How it Works (The Color Analogy)

Before diving into the math, the logic is best understood using the famous "Paint Mixing" analogy:

1.  **Public Color:** Alice and Bob agree on a public color, e.g., **Yellow**.
2.  **Secret Colors:** Alice picks a secret color (**Red**), and Bob picks a secret color (**Blue**).
3.  **Mixing & Exchange:**
    * Alice: Yellow + Red = **Orange** (Sends to Bob).
    * Bob: Yellow + Blue = **Green** (Sends to Alice).
4.  **Final Secret:**
    * Alice takes Bob's **Green** and adds her secret **Red** → **Brown**.
    * Bob takes Alice's **Orange** and adds his secret **Blue** → **Brown**.

*Result: Both have the same color (Brown), but an eavesdropper who only saw Yellow, Orange, and Green cannot determine the secret components to recreate Brown.*

---

## Mathematical Foundation

In cryptography, we replace colors with **Modular Arithmetic**.

**Parameters:**
* $p$: A large prime number (Modulus).
* $g$: A primitive root modulo $p$ (Generator).

**The Process:**

| Step | Alice (A) | Bob (B) |
| :--- | :--- | :--- |
| **1. Private Key** | Chooses a secret integer $a$. | Chooses a secret integer $b$. |
| **2. Public Key Calc** | Calculates $A = g^a \pmod p$ <br> Sends $A$ to Bob. | Calculates $B = g^b \pmod p$ <br> Sends $B$ to Alice. |
| **3. Shared Secret** | Receives $B$. Computes: <br> $s = B^a \pmod p$ | Receives $A$. Computes: <br> $s = A^b \pmod p$ |

**Why are they equal?**
According to the laws of exponentiation:
$$s = (g^a)^b = g^{ab} = g^{ba} = (g^b)^a \pmod p$$

---

## 🚀 Installation & Usage

This project runs on standard Python 3 and requires no external libraries.

1.  **Clone the repository** or download `diffie_hellman.py`.
2.  **Run the script** via terminal:

```bash
python diffie_hellman.py
