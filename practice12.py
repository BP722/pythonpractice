password = input("Enter a Password to Test: ")
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char in "!@#$%^&*()-+" for char in password):
            score += 1
    else:
        print("Error: Password must be at least 8 characters long.")
        return 0
    return score

score = password_strength(password)
print("===================================")
print(f"Your password score is: {score}")
print("===================================")
