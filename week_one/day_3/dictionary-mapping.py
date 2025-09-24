grade = input("Enter grade (A, B, C, D, F): ").upper()

feedback = {
    "A": "Excellent",
    "B": "Good",
    "C": "Average",
    "D": "Below Average",
    "F": "Fail",
}

print(feedback.get(grade, "Invalid grade"))
