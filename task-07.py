names = ["Sita", "Ram", "Gita"]
marks = [[90, 85, 78], [45, 38, 60], [70, 65, 80]]
def get_average(student_marks):
    """Calculates and returns the arithmetic mean of a list of marks, rounded to 2 decimal places."""
    return round(sum(student_marks) / len(student_marks), 2)
def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"
def report(name, student_marks, pass_mark=40):
    avg = get_average(student_marks)
    grade = get_grade(avg)
    best = max(student_marks)
    worst = min(student_marks)
    passed_all = all(mark >= pass_mark for mark in student_marks)
    print(f"{name}: avg {avg:.2f}, grade {grade}")
    print(f"  Best: {best} | Worst: {worst}")
    print(f"  Passed all? {passed_all}")
    
    return avg
all_averages = []
for name, student_marks in zip(names, marks):
    student_avg = report(name, student_marks)
    all_averages.append(student_avg)
sorted_averages = sorted(all_averages, reverse=True)

for index, avg in enumerate(sorted_averages, start=1):
    print(f"Rank {index}: {avg:.2f}")