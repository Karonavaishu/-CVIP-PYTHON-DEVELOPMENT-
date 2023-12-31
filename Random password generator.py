import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the desired password length: "))
    if password_length < 6:
        print("Password length should be at least 6 characters.")
        return

    generated_password = generate_random_password(password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
