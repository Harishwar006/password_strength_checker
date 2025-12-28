# src/scorer.py

def calculate_score(results):
    score = 0

    if results["length"] >= 8:
        score += 20
    if results["has_upper"]:
        score += 20
    if results["has_lower"]:
        score += 20
    if results["has_digit"]:
        score += 20
    if results["has_special"]:
        score += 20
    if results["is_common"]:
        score -= 30

    return max(0, min(score, 100))
