print("📘 AUTOMATIC STUDY PLANNER\n")


subjects = [s.strip() for s in input("Enter subjects (comma separated): ").split(",")]

difficulties = []
for subject in subjects:
    diff = input(f"Enter difficulty for {subject} (easy/medium/hard): ").lower()
    difficulties.append(diff)

days = int(input("Enter number of days until exam: "))
daily_hours = float(input("Enter study hours available per day: "))


weights = []
valid_diff = ["easy", "medium", "hard"]

for diff in difficulties:
    if diff not in valid_diff:
        print(f"Warning: '{diff}' is invalid. Defaulting to 'medium'.")
        diff = "medium"
        
    if diff == "easy":
        weights.append(1)
    elif diff == "medium":
        weights.append(2)
    elif diff == "hard":
        weights.append(3)

total_weight = sum(weights)

print("\n📊 Generating your study plan...\n")


subject_hours_daily = []
subject_hours_total = []

for w in weights:
    daily = (w / total_weight) * daily_hours
    total = daily * days
    subject_hours_daily.append(daily)
    subject_hours_total.append(total)


print("📘 STUDY PLAN\n")
print(f"{'Subject':<12}{'Daily Hours':<15}{'Total Hours':<15}{'Priority'}")
print("-" * 55)

for i, subject in enumerate(subjects):
    sub = subject
    daily = round(subject_hours_daily[i], 2)
    total = round(subject_hours_total[i], 2)

    # Priority
    if weights[i] == 3:
        priority = "HIGH"
    elif weights[i] == 2:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    print(f"{sub:<12}{daily:<15}{total:<15}{priority}")

print("\n💡 RECOMMENDATIONS:")
hardest = subjects[weights.index(max(weights))]
print(f"- Focus more on {hardest} — it is your most difficult subject.")
print("- Keep the last 1–2 days only for revision.")
print("- Study hard subjects earlier in the day for better focus.")
print("- Take short breaks every 45–50 mins.\n")

print("✅ Your study plan is ready! Good luck! 🚀")
