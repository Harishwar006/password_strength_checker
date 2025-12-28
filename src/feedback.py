# src/feedback.py

def generate_feedback(results):
    feedback = []

    if results["length"] < 8:
        feedback.append("Use at least 8 characters")
    if not results["has_upper"]:
        feedback.append("Add uppercase letters")
    if not results["has_lower"]:
        feedback.append("Add lowercase letters")
    if not results["has_digit"]:
        feedback.append("Add digits")
    if not results["has_special"]:
        feedback.append("Add special characters")
    if results["is_common"]:
        feedback.append("Avoid common passwords")

    return feedback
