# Exercise 2: Conditionals
# Turns a numeric score into a letter grade using if / elif / else.


def get_grade(score):
    """Return a letter grade for a score between 0 and 100."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    # Try it with a few different scores
    for test_score in [85, 65, 52, 41, 20, 150]:
        print(f"Score {test_score} -> Grade: {get_grade(test_score)}")