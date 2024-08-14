import random
import string


def random_password(length):
    # password data
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    # combined characters
    # older code
    # char_set = [lowercase, uppercase, digits, symbols]
    # improved code
    char_set = lowercase + uppercase + digits + symbols
    # for each character in password
    password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(symbols)

    password += ''.join(random.choice(char_set) for _ in range(length - 4))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


while True:
    password_length = int(input("Enter desired password length: "))

    generated_password = random_password(password_length)

    print(f"Your generated password is:  {generated_password}")

    again = input("if you want another password press y else press enter to exit:")
    if again != "y":
        break

print("Thanks for using random password generator")
