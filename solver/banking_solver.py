import re
import random

def solve_banking_question(question):
    try:
        # Extract Principal (P)
        p_match = re.search(r"(?:₹|Rs\.?)\s?(\d+)", question)
        P = int(p_match.group(1)) if p_match else None

        # Extract Time (n in months)
        n_match = re.search(r"(\d+)\s*(?:months|month)", question, re.IGNORECASE)
        n = int(n_match.group(1)) if n_match else None

        # Extract Interest Rate (r)
        r_match = re.search(r"(\d+\.?\d*)\s*%|at\s*(\d+\.?\d*)\s*p\.a\.", question, re.IGNORECASE)
        r = float(r_match.group(1) or r_match.group(2)) if r_match else None

        if not all([P, n, r]):
            return "❗Sorry, the question format is not clear. Please ensure it includes monthly amount, time, and interest rate."

        # Calculate Interest
        I = (P * n * (n + 1) * r) / (2 * 12 * 100)

        # Maturity Value
        M = P * n + I

        return (
            f"📘 Step-by-step Solution:\n\n"
            f"Given:\n"
            f"Monthly Deposit (P) = ₹{P}\n"
            f"Number of Months (n) = {n}\n"
            f"Rate of Interest (r) = {r}% p.a.\n\n"
            f"Formula for Interest:\n"
            f"I = (P × n(n+1) × r) / (2 × 12 × 100)\n"
            f"I = ({P} × {n} × {n+1} × {r}) / (2 × 12 × 100)\n"
            f"I = ₹{I:.2f}\n\n"
            f"Maturity Value = P × n + I = ₹{P} × {n} + ₹{I:.2f} = ₹{M:.2f}"
        )

    except Exception as e:
        return f"❌ Error: {str(e)}"


def get_summary():
    return (
        "📚 Banking Chapter Summary (ICSE Class 10):\n\n"
        "1. Recurring Deposit (RD) accounts involve depositing a fixed amount monthly.\n"
        "2. Interest is calculated using:\n"
        "   I = (P × n(n+1) × r) / (2 × 12 × 100)\n"
        "   where:\n"
        "     P = Monthly deposit\n"
        "     n = Number of months\n"
        "     r = Rate of interest per annum\n"
        "3. Maturity Value = Total Deposit + Interest = P × n + I\n"
        "4. Interest is computed on reducing balance method.\n"
        "5. Deposits are made in fixed intervals — usually monthly."
    )


def generate_question():
    P = random.choice([200, 300, 500, 1000])
    n = random.choice([6, 12, 24, 36])
    r = random.choice([6, 7, 8, 9, 10])
    return (
        f"A person deposits ₹{P} per month for {n} months "
        f"in a bank at {r}% per annum. What will be the maturity value?"
    )


def generate_mock_test():
    questions = []
    for i in range(5):
        q_text = generate_question()
        p_match = re.search(r"₹(\d+)", q_text)
        n_match = re.search(r"(\d+)\s*months", q_text)
        r_match = re.search(r"at\s*(\d+)%", q_text)

        if p_match and n_match and r_match:
            P = int(p_match.group(1))
            n = int(n_match.group(1))
            r = int(r_match.group(1))
            I = (P * n * (n + 1) * r) / (2 * 12 * 100)
            M = P * n + I

            answer = (
                f"Monthly deposit = ₹{P}\n"
                f"Number of months = {n}\n"
                f"Rate = {r}%\n"
                f"I = (P × n(n+1) × r) / (2 × 12 × 100)\n"
                f"I = ₹{I:.2f}\n"
                f"Maturity Value = ₹{P*n} + ₹{I:.2f} = ₹{M:.2f}"
            )

            questions.append({
                "question": q_text,
                "marks": 5,
                "marking_scheme": {
                    "Correct formula": 1,
                    "Correct substitution": 1,
                    "Correct interest calculation": 1,
                    "Correct total deposit": 1,
                    "Final maturity value": 1
                },
                "answer": answer
            })

    return {"questions": questions}
