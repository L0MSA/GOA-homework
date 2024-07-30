lessons = {
    'math': 90,
    'science': 85,
    'history': 88,
    'english': 92
}

average = sum(lessons.values()) / len(lessons)

for subject, points in lessons.items():
    print(f"{subject.capitalize()}: {points} points")

print(f"Average score: {average:.2f} points")
