import random

def power(base, exp, mod):
    """
    Modular exponentiation function: (base^exp) % mod
    It does the same job as Python's built-in pow(base, exp, mod) function
    but can be written explicitly to show the logic, or pow() can be used.
    """
    return pow(base, exp, mod)

# STEP 1: Determining Shared Parameters (Public)
# In real life, these numbers are 2048-bit or 4096-bit long.
# We are choosing small numbers for clarity.
prime_p = 27644437   # Prime Number (Modulus)
generator_g = 5 # Generator (Base)

print(f"--- Public Parameters ---")
print(f"Prime number (p): {prime_p}")
print(f"Generator (g): {generator_g}\n")

# STEP 2: Selecting Private Keys
# Only the individuals themselves know these numbers.
alice_private_a = random.randint(1, prime_p-1)  # Alice's secret number (a)
bob_private_b = random.randint(1, prime_p-1)   # Bob's secret number (b)

print(f"--- Secret Keys (Not to be shared with anyone) ---")
print(f"Alice's Secret Key (a): {alice_private_a}")
print(f"Bob's Secret Key (b): {bob_private_b}\n")

# STEP 3: Calculating Public Keys
# A = g^a mod p
alice_public_A = power(generator_g, alice_private_a, prime_p)

# B = g^b mod p
bob_public_B = power(generator_g, bob_private_b, prime_p)

print(f"--- Public Keys (Sent to Each Other) ---")
print(f"Alice is sending to Bob (A): {alice_public_A}")
print(f"Bob is sending to Alice (B): {bob_public_B}\n")

# STEP 4: Calculating the Shared Secret
# Alice performs the operation B^a mod p.
shared_secret_Alice = power(bob_public_B, alice_private_a, prime_p)

# Bob performs the operation A^b mod p.
shared_secret_Bob = power(alice_public_A, bob_private_b, prime_p)

print(f"--- Result: Calculated Shared Secret ---")
print(f"The secret Alice discovered: {shared_secret_Alice}")
print(f"The secret Bob discovered: {shared_secret_Bob}")

if shared_secret_Alice == shared_secret_Bob:
    print("\nSUCCESSFUL! Both parties agreed on the same key.")
else:
    print("\nERROR! The keys don't match.")
