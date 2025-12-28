🔐 Password Strength Checker (Offline Brute‑Force Model)

📌 Overview

The Password Strength Checker is a security analysis tool that evaluates password strength based on offline brute‑force attack resistance.

Unlike common online checkers, this tool assumes a worst‑case scenario where an attacker already has access to the password hash and can perform unlimited guesses using high‑performance hardware.

This makes the tool suitable for academic projects, security audits, and defensive analysis.

---

🎯 Key Features

Evaluates password strength based on:

Length

Character diversity


Calculates:

Character set size

Total possible combinations

Estimated crack time using:

CPU brute‑force

GPU brute‑force


Uses offline attack assumptions

No password storage or transmission

---

⚙️ Attack Model Assumptions

This tool assumes:

Offline brute‑force attack

No rate limiting

No account lockout

Attacker has password hash

High‑performance hardware


Guessing Speeds

Attack Type	Speed

CPU brute‑force	100 million guesses/sec

GPU brute‑force	10 billion guesses/sec

---

🧮 Crack Time Calculation

Total Combinations = (Character Set Size) ^ (Password Length)

Crack Time (seconds) = Total Combinations / Guesses Per Second

Time is converted into years for readability.

---

📊 Example Output

Password Strength: Strong
Password Length: 12
Character Set Size: 94
Total Combinations: 4.7e+23

Estimated Crack Time:
- Brute-force (CPU): 1.5e+15 years
- Brute-force (GPU): 1.5e+13 years

---

⚠️ Important Note

> Crack time estimates represent offline attacks.

Online password checkers calculate login‑based attacks, which result in much smaller time estimates.

Both models are correct but represent different threat scenarios.

---

🧠 Strength Classification

Condition	Strength

Length < 8	Weak

Length ≥ 8	Medium

Length ≥ 12 + high charset	Strong

---

🛠️ Usage

1. Run the tool from the command line


2. Enter a password when prompted


3. View strength analysis and crack time estimates

---

🎓 Use Cases

Cybersecurity academic projects

Password policy evaluation

Defensive security training

Offline attack modeling

---

🔒 Security & Privacy

Passwords are processed locally

No data is stored or transmitted

Tool is for educational and defensive use only

---


