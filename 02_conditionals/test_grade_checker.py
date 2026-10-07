# Automated tests for the grade checker in Exercise 2.

import pytest

from grade_checker import get_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (85, "A"),
        (70, "A"),
        (65, "B"),
        (60, "B"),
        (52, "C"),
        (50, "C"),
        (41, "D"),
        (40, "D"),
        (39, "F"),
        (0, "F"),
    ],
)
def test_valid_grades(score, expected):
    assert get_grade(score) == expected


@pytest.mark.parametrize("score", [-1, 101, 150])
def test_invalid_scores(score):
    assert get_grade(score) == "Invalid score"