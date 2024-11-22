# Password Generator
import random
import string

def generate_password(length):
    characters_pool = string.printable  # define characters like uppercase, lowercase, digits, and special characters
    secure_password = ''.join(random.choices(characters_pool, k =length))
    return secure_password

# the main function
def main():
    print("Simple Password Generator")
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length < 8:
            print("Password length should be at least 8.")
        else:
            new_password = generate_password(desired_length)
            print(f"Generated Password is: {new_password}")
    except ValueError:
        print("Invalid input. Please enter a number.")

# run the program
if __name__ == "_main_":
    main()