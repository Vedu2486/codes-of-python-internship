import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (default is 12): "))
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return
    except ValueError:
        length = 12  # Set to default length if user doesn't input a number

    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
