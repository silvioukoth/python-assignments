marks = int(input("Enter the student's marks (0-100): "))

if marks > 70:
    print("Grade: Distinction 🥇")
elif marks >= 60:
    print("Grade: Credit 🥇")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: fail ❌")