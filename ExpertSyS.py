def score_factor(value, scale):
    """Convert qualitative input to numerical score based on predefined scale."""
    return scale.get(value.lower(), 0)

def evaluate_performance(experience, punctuality, communication, task_completion, teamwork, leadership):
    # Convert qualitative attributes to scores
    punctuality_score = score_factor(punctuality, {"excellent": 3, "good": 2, "average": 1, "poor": 0})
    communication_score = score_factor(communication, {"excellent": 3, "good": 2, "average": 1, "poor": 0})
    teamwork_score = score_factor(teamwork, {"excellent": 3, "good": 2, "average": 1, "poor": 0})
    leadership_score = score_factor(leadership, {"excellent": 3, "good": 2, "average": 1, "poor": 0})

    # Combine all scores
    total_score = (
        (experience * 1.5) +
        (task_completion * 2) +
        punctuality_score +
        communication_score +
        teamwork_score +
        leadership_score
    )

    # Decision logic
    if total_score >= 35:
        return "Outstanding"
    elif total_score >= 25:
        return "Exceeds Expectations"
    elif total_score >= 15:
        return "Meets Expectations"
    else:
        return "Needs Improvement"

def main():
    print("=== Expert System: Employee Performance Evaluation ===")

    try:
        experience = int(input("Years of Experience: "))
        task_completion = int(input("Avg Tasks Completed per Month (0–10): "))
        punctuality = input("Punctuality (Excellent/Good/Average/Poor): ")
        communication = input("Communication Skills (Excellent/Good/Average/Poor): ")
        teamwork = input("Teamwork (Excellent/Good/Average/Poor): ")
        leadership = input("Leadership (Excellent/Good/Average/Poor): ")

        result = evaluate_performance(
            experience,
            punctuality,
            communication,
            task_completion,
            teamwork,
            leadership
        )

        print("\nFinal Performance Rating:", result)

    except ValueError:
        print("Please enter numeric values where required.")

if __name__ == "__main__":
    main()
