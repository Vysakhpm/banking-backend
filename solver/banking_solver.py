import re
import random

def solve_banking_question(question):
    try:
        p_match = re.search(r'(?:₹|Rs\.?|INR)?\s*(\d+(?:\.\d+)?)\s*per month', question, re.IGNORECASE)
        n_match = re.search(r'for\s+(\d+(?:\.\d+)?)\s*(months|years)', question, re.IGNORECASE)
        r_match = re.search(r'(\d+(?:\.\d+)?)\s*%\s*(?:p\.a\.|per annum)', question, re.IGNORECASE)

        if not (p_match and n_match and r_match):
            return "❗Sorry, the question format is not clear. Please ensure it includes monthly amount, time, and interest rate."

        P = float(p_match.group(1))
        n = float(n_match.group(1))
        time_unit = n_match.group(2).lower()
        r = float(r_match.group(1))

        if "year" in time_unit:
            n *= 12

        interest = P * n * (n + 1) / 2 * r / (12 * 100)
        maturity = P * n + interest

        explanation = (
            f"📘 Question: {question.strip()}\n\n"
            f"✅ Step-by-Step Solution:\n"
            f"1. Monthly Deposit (P) = ₹{P}\n"
            f"2. Number of Months (n) = {int(n)}\n"
            f"3. Rate of Interest (r) = {r}% p.a.\n\n"
            f"Step 1: Calculate Interest\n"
            f"I = (P × n(n+1) × r) / (2 × 12 × 100)\n"
            f"→ I = (₹{P} × {int(n)} × {int(n + 1)} × {r}) / 2400 = ₹{interest:.2f}\n\n"
            f"Step 2: Maturity Value = Total Deposit + Interest\n"
            f"→ M.V. = ₹{P} × {int(n)} + ₹{interest:.2f} = ₹{maturity:.2f}\n\n"
            f"🧠 Final Answer: ₹{maturity:.2f}\n\n"
            f"📝 Important Formula:\n"
            f"Interest = (P × n(n+1) × r) / (2 × 12 × 100)"
        )

        return explanation

    except Exception as e:
        return f"⚠️ An error occurred while solving: {str(e)}"

def get_summary():
    return (
        "📘 Banking Chapter Summary (Recurring Deposit Account)\n\n"
        "1. A Recurring Deposit (R.D.) Account allows regular monthly savings.\n"
        "2. Interest is calculated using:\n"
        "   I = (P × n(n + 1) × r) / (2 × 12 × 100)\n"
        "3. Maturity Value (M.V.) = (P × n) + I\n\n"
        "Where:\n"
        "- P = monthly deposit\n"
        "- n = number of months\n"
        "- r = annual rate of interest"
    )

def generate_question():
    sample_questions = [
        "Kiran deposits ₹200 per month for 36 months. What is the maturity value at 11% p.a.?",
        "Monica deposited ₹600 per month for 2 years. Find the maturity value at 10% p.a.",
        "Ravi saves ₹150 per month for 18 months in an R.D. account. Interest rate is 9% per annum. What will he get on maturity?",
        "Shalini deposited ₹1,000 monthly for 3 years at 8% p.a. What is the maturity amount?",
        "Find the maturity value if Rs. 350 is deposited every month for 2 years at 12% interest."
    ]
    return random.choice(sample_questions)

def generate_mock_test():
    questions = [
        {
            "question": "Manish deposited ₹600 per month for 20 months at 10% p.a. Find the maturity value.",
            "marks": 5,
            "marking_scheme": {
                "Identifying P, n, r": 1,
                "Correct use of formula": 2,
                "Correct interest calculation": 1,
                "Final M.V. calculation": 1
            },
            "answer": solve_banking_question("Manish deposited ₹600 per month for 20 months at 10% p.a.")
        },
        {
            "question": "Geeta deposited ₹350 per month for 15 months at 12% p.a. Find interest and maturity value.",
            "marks": 5,
            "marking_scheme": {
                "Correct substitution": 2,
                "Correct interest calculation": 2,
                "Final maturity value": 1
            },
            "answer": solve_banking_question("Geeta deposited ₹350 per month for 15 months at 12% p.a.")
        }
    ]
    return {"total_marks": 10, "questions": questions}
