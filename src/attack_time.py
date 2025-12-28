# src/attack_time.py

def _format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"


def estimate_attack_times(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32

    combinations = charset ** len(password)

    attack_speeds = {
        "Brute-force (CPU)": 1_000_000_000,
        "Brute-force (GPU)": 100_000_000_000,
        "Dictionary attack": 10_000_000,
        "Hybrid attack": 5_000_000_000
    }

    attack_times = {}

    for attack, speed in attack_speeds.items():
        seconds = combinations / speed
        attack_times[attack] = _format_time(seconds)

    return attack_times
