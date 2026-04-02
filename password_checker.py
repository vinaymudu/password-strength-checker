# ============================================
#   Project 1 - Password Strength Checker
#   Built by: Vinay
#   Purpose: Cybersecurity Portfolio Project
# ============================================

def check_password(password):
    # Check each requirement
    has_length  = len(password) >= 16
    has_upper   = any(c.isupper() for c in password)
    has_number  = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

    # Count score
    score = 0
    if has_length  : score += 1
    if has_upper   : score += 1
    if has_number  : score += 1
    if has_special : score += 1

    # Rate strength
    if score == 4:
        strength = "🔥 STRONG"
    elif score == 3:
        strength = "⚠️  MEDIUM"
    elif score == 2:
        strength = "⚠️  WEAK"
    else:
        strength = "❌ VERY WEAK"

    return strength, score, has_length, has_upper, has_number, has_special


def save_result(password, strength, score):
    try:
        with open("password_results.txt", "a") as f:
            f.write("=" * 40 + "\n")
            f.write(f"Password : {password}\n")
            f.write(f"Strength : {strength}\n")
            f.write(f"Score    : {score}/4\n")
            f.write("=" * 40 + "\n")
        print("✅ Result saved to password_results.txt!")

    except Exception as e:
        print(f"❌ Could not save result: {e}")


def main():
    print("=" * 40)
    print("   Vinay's Password Strength Checker")
    print("=" * 40)

    while True:
        password = input("\nEnter password (or 'quit' to exit): ")

        if password == "quit":
            print("Goodbye! Stay secure! 🔐")
            break

        # Check the password
        strength, score, has_length, has_upper, has_number, has_special = check_password(password)

        # Show detailed results
        print("\n--- Results ---")
        print(f"Length 16+   : {'✅' if has_length  else '❌'}")
        print(f"Uppercase    : {'✅' if has_upper   else '❌'}")
        print(f"Number       : {'✅' if has_number  else '❌'}")
        print(f"Special char : {'✅' if has_special else '❌'}")
        print(f"\nStrength: {strength}")
        print(f"Score   : {score}/4")

        # Save result to file
        save_result(password, strength, score)

# Run the program
main()