import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "🔒 Strong"
    elif length >= 8 and score >= 3:
        return "🛡️ Medium"
    else:
        return "⚠️ Weak"

def main():
    print("="*35)
    print("🔐 PASSWORD GENERATOR & STRENGTH METER")
    print("="*35)

    try:
        length = int(input("Enter desired password length (min 6): "))
        if length < 6:
            print("❌ Length too short. Setting to 6.")
            length = 6
    except:
        print("⚠️ Invalid input. Using default length 12.")
        length = 12

    password = generate_password(length)
    strength = check_strength(password)

    print(f"\nGenerated Password: {password}")
    print(f"Password Strength: {strength}")
    print("="*35)

if __name__ == "__main__":
    main()
