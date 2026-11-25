GRADE_POINTS = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

def calculate_gpa(courses):
    total_points = 0
    total_credits = 0
    for name, credits, grade in courses:
        total_points += GRADE_POINTS[grade] * credits
        total_credits += credits
    return total_points / total_credits if total_credits else 0.0

def show_result(gpa):
    print(f"Your GPA is: {gpa:.2f}")

def get_remark(gpa, max_scale=4.0):
    percent = gpa / max_scale
    if percent >= 0.9:
        return "Excellent"
    elif percent >= 0.7:
        return "Good"
    return "Needs improvement"

if __name__ == "__main__":
    courses = [("Maths", 4, "A"), ("Physics", 3, "B"), ("English", 2, "A")]
    show_result(calculate_gpa(courses))