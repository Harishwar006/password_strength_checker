# main.py

from src.checks import analyze_password
from src.scorer import calculate_score
from src.attack_time import estimate_attack_times
from src.feedback import generate_feedback

def main():
    password = input("Enter password to analyze: ")

    results = analyze_password(password)
    score = calculate_score(results)
    attack_times = estimate_attack_times(password)
    feedback = generate_feedback(results)

    print("\n🔐 Password Strength Report")
    print("---------------------------")
    print(f"Score           : {score}/100")
    print("\n⏱ Attack Time Estimates:")
    for attack, time in attack_times.items():
     print(f"- {attack}: {time}")

    if score >= 80:
        print("Strength        : Strong 💪")
    elif score >= 50:
        print("Strength        : Medium ⚠️")
    else:
        print("Strength        : Weak ❌")

    print("\nSuggestions:")
    if feedback:
        for f in feedback:
            print(f"- {f}")
    else:
        print("- Excellent password!")

if __name__ == "__main__":
    main()
