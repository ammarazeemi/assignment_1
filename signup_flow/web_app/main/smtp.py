import random

# Generate a random 4-digit number
verification_code = random.randint(1000, 9999)
print(f"Generated 4-digit number: {verification_code}")

# Check the length of the generated number
print(f"Length of the number: {len(str(verification_code))}")
