import random
import string
def get_user_input():
    length = int(input("Enter the total length of the password: "))
    upper_length = int(input("Enter the length of uppercase letters: "))
    lower_length = int(input("Enter the length of lowercase letters: "))
    symbol_length = int(input("Enter the length of symbols: "))
    number_length = int(input("Enter the length of numbers: "))
    return length, upper_length, lower_length, symbol_length, number_length

def generate_random_password(length, upper_length, lower_length, symbol_length, number_length):
    upper_chars = ''.join(random.choices(string.ascii_uppercase, k=upper_length))
    lower_chars = ''.join(random.choices(string.ascii_lowercase, k=lower_length))
    symbol_chars = ''.join(random.choices(string.punctuation, k=symbol_length))
    number_chars = ''.join(random.choices(string.digits, k=number_length))
    
    chars = upper_chars + lower_chars + symbol_chars + number_chars
    if len(chars) < length:
        chars += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - len(chars)))
        
    password = ''.join(random.sample(chars, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length, upper_length, lower_length, symbol_length, number_length = get_user_input()
    password = generate_random_password(length, upper_length, lower_length, symbol_length, number_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
