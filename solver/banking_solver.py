import re
import random

def solve_banking_question(question):
    try:
        # Extract monthly deposit (P)
        p_match = re.search(r"(?:₹|Rs\.?)\s?(\d+)", question)
        P = int(p_match.group(1)) if p_match else None

        # Extract time (n) in months
        n_match = re.search(r"(\d+)\s*(months|month)", question, re.IGNORECASE)
        n = int(n_match.group(1)) if n_match else None

        # Extract interest rate (r)
        r_match = re.search(r"(\d+\.?\d*)\s*%|at\s*(\d+\.?\d*)\s*p\.a", question, re.IGNORECASE)
        r = float(r_match.group(1) or r_match.group(2)) if r_match else None

        # Ensure all values are extracted
        if not all([P, n, r]):
            return "❗ Please ensure the question includes deposit, time (months), and rate."

        # Calculations
        total_deposit = P * n
        interest = (P * n * (n + 1) * r) / (2 * 12 * 100)
        maturity = total_deposit + interest

        # Step-by-step calculation values
        n_n1 = n * (n + 1)
        pn_n1 = P * n_n1
        numerator = pn_n1 * r
        denominator = 2 * 12 * 100

        return (
            f"✅ **Step-by-Step Solution**\n\n"
            f"**Given:**\n"
            f"Monthly Deposit (P) = ₹{P}\n"
            f"Number of Months (n) = {n}\n"
            f"Rate of Interest (r) = {r}% per annum\n\n"
            f"👉 **Total Deposit** = ₹{P} × {n} = ₹{total_deposit}\n\n"
            f"👉 **Interest Calculation**\n"
            f"Formula: I = (P × n(n + 1) × r) / (2 × 12 × 100)\n"
            f"        = ({P} × {n} × {n + 1} × {r}) / 2400\n"
            f"        = {numerator:.0f} / 2400 = ₹{interest:.0f}\n\n"
            f"👉 **Maturity Value** = ₹{total_deposit} + ₹{interest:.0f} = ₹{maturity:.0f}\n\n"
            f"🟩 **Final Answer: ₹{maturity:.0f}**"
        )

    except Exception as e:
        return f"❌ Error: {str(e)}"

def get_summary():
    return (
        "📘 **Banking Chapter Summary (ICSE Class 10)**\n\n"
        "1. A Recurring Deposit (RD) is where a fixed amount is deposited monthly.\n"
        "2. Interest is calculated using:\n"
        "   I = (P × n(n + 1) × r) / (2 × 12 × 100)\n"
        "   where P = monthly deposit, n = number of months, r = annual interest rate.\n"
        "3. Maturity Value (MV) = Total Deposit + Interest = P × n + I\n"
        "4. Always convert years to months if needed.\n"
        "5. Use the formula steps to avoid mistakes in exams."
    )

def generate_question():
    P = random.choice([100, 200, 300, 500])
    n = random.choice([12, 24, 36])
    r = random.choice([7, 8, 9, 10, 11])
    return f"A person deposits ₹{P} every month for {n} months in a bank at {r}% per annum. What will be the maturity value?"

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
                f"I = ({P} × {n} × {n + 1} × {r}) / 2400\n"
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
