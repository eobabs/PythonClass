

import random
import string

def generate_password(length=random.randrange(16, 50)):
    if length < 16:
        raise ValueError("Password length must be at least 16 characters")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(symbols)]

    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
