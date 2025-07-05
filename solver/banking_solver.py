import re
import random

def solve_banking_question(question):
    try:
        # Extract monthly deposit (P)
        p_match = re.search(r"(?:₹|Rs\.?)\s?(\d+)", question)
        P = int(p_match.group(1)) if p_match else None

        # Extract time in months or years
        n = None
        n_match_months = re.search(r"(\d+)\s*(months|month)", question, re.IGNORECASE)
        n_match_years = re.search(r"(\d+\.?\d*)\s*(years|year)", question, re.IGNORECASE)

        if n_match_months:
            n = int(n_match_months.group(1))
        elif n_match_years:
            n = int(float(n_match_years.group(1)) * 12)

        # Extract rate of interest (r)
        r_match = re.search(r"(\d+\.?\d*)\s*%|at\s*(\d+\.?\d*)\s*p\.a\.", question, re.IGNORECASE)
        r = float(r_match.group(1) or r_match.group(2)) if r_match else None

        # Validate
        if not all([P, n, r]):
            return "❗Please ensure the question contains the monthly amount, time (in months or years), and interest rate."

        # Calculate interest and maturity value
        I = (P * n * (n + 1) * r) / (2 * 12 * 100)
        M = P * n + I

        return (
            f"✅ **Step-by-step Solution (ICSE Format)**:\n\n"
            f"Let the monthly deposit = ₹{P}\n"
            f"Number of months (n) = {n}\n"
            f"Rate of interest (r) = {r}% per annum\n\n"
            f"👉 **Total Deposit** = ₹{P} × {n} = ₹{P * n}\n\n"
            f"👉 **Interest Formula**:\n"
            f"I = (P × n(n + 1) × r) / (2 × 12 × 100)\n"
            f"I = ({P} × {n} × {n + 1} × {r}) / (2 × 12 × 100)\n"
            f"I = ₹{I:.2f}\n\n"
            f"👉 **Maturity Value** = Total Deposit + Interest\n"
            f"                     = ₹{P * n} + ₹{I:.2f}\n"
            f"                     = ₹{M:.2f}\n\n"
            f"🟩 **Final Answer: ₹{M:.2f}**"
        )

    except Exception as e:
        return f"❌ Error: {str(e)}"


def get_summary():
    return (
        "📘 **Banking Chapter Summary (ICSE Class 10)**\n\n"
        "1. Recurring Deposit (RD) is a scheme where a fixed amount is deposited every month.\n"
        "2. Formula for Interest:\n"
        "   I = (P × n(n + 1) × r) / (2 × 12 × 100)\n"
        "     where:\n"
        "       P = Monthly deposit\n"
        "       n = Number of months\n"
        "       r = Annual rate of interest (%)\n\n"
        "3. Maturity Value = Total Deposits + Interest = P × n + I\n"
        "4. Time may be given in years; always convert to months.\n"
        "5. The deposit earns interest for decreasing periods each month."
    )


def generate_question():
    P = random.choice([100, 200, 300, 500, 1000])
    n = random.choice([6, 12, 24, 36])
    r = random.choice([6, 7, 8, 9, 10])
    return (
        f"A person deposits ₹{P} every month for {n} months in a bank "
        f"at {r}% per annum. What will be the maturity value?"
    )


def generate_mock_test():
    questions = []
    for _ in range(5):
        question_text = generate_question()
        p_match = re.search(r"₹(\d+)", question_text)
        n_match = re.search(r"(\d+)\s*months", question_text)
        r_match = re.search(r"at\s*(\d+)%", question_text)

        if p_match and n_match and r_match:
            P = int(p_match.group(1))
            n = int(n_match.group(1))
            r = int(r_match.group(1))
            I = (P * n * (n + 1) * r) / (2 * 12 * 100)
            M = P * n + I

            answer = (
                f"Monthly deposit = ₹{P}\n"
                f"Number of months = {n}\n"
                f"Rate of interest = {r}%\n\n"
                f"I = (P × n(n + 1) × r) / (2 × 12 × 100)\n"
                f"I = ({P} × {n} × {n + 1} × {r}) / (2 × 12 × 100)\n"
                f"I = ₹{I:.2f}\n\n"
                f"Maturity Value = ₹{P * n} + ₹{I:.2f} = ₹{M:.2f}"
            )

            questions.append({
                "question": question_text,
                "marks": 5,
                "marking_scheme": {
                    "Identifies P, n, r": 1,
                    "Correct substitution in formula": 1,
                    "Correct interest calculation": 1,
                    "Correct total deposit": 1,
                    "Final maturity value": 1
                },
                "answer": answer
            })

    return {"questions": questions}
