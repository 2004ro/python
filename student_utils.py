def calculate_avg(*marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def get_grade(avg, pass_marks=40):
    if avg < pass_marks:
        return "F grade"
    elif avg >= 90:
        return "A"
    elif avg >= 80: 
        return "B"
    elif avg >= 70:  
        return "C"
    else:
        return "Pass"