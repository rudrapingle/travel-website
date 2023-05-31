def evaluate_employee_performance(deadlines_met, expectations_exceeded, initiative_taken, absences, performance_below_expectations):
    score = 0
    score += 20 if deadlines_met else 0
    score += 30 if expectations_exceeded else 0
    score += 15 if initiative_taken else 0
    score -= 25 if absences else 0
    score -= 35 if performance_below_expectations else 0
    return score

employee_data = {}
n = int(input("Enter the number of employees you want to evaluate: "))
for _ in range(n):
    name = input("Enter the name of the employee: ")
    data = {
        "deadlines_met": bool(int(input("Enter the performance of deadlines met (0 or 1): "))),
        "expectations_exceeded": bool(int(input("Enter the performance of expectations exceeded (0 or 1): "))),
        "initiative_taken": bool(int(input("Enter the performance of initiative taken (0 or 1): "))),
        "absences": bool(int(input("Enter the performance of absences (0 or 1): "))),
        "performance_below_expectations": bool(int(input("Enter the performance of performance below expectations (0 or 1): "))),
    }
    employee_data[name] = data

print("\nRules for employee evaluation:")
print("- If the employee meets all project deadlines, add 20 points to their score.")
print("- If the employee consistently exceeds expectations, add 30 points to their score.")
print("- If the employee shows initiative and takes on additional responsibilities, add 15 points to their score.")
print("- If the employee is frequently absent or misses deadlines, subtract 25 points from their score.")
print("- If the employee consistently performs below expectations, subtract 35 points from their score.\n")

for name, data in employee_data.items():
    score = evaluate_employee_performance(data["deadlines_met"], data["expectations_exceeded"],
                                          data["initiative_taken"], data["absences"],
                                          data["performance_below_expectations"])
    print(f"Employee {name} scored {score} points")
