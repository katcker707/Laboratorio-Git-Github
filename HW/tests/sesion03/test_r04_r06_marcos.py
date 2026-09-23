from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    round_score_to_ten,
    unique_tags,
    rotate_left,
)


def test_rotate_left_is_circular():
    """R-04: La rotación izquierda es circular."""
    assert rotate_left([1, 2, 3, 4], 6) == [3, 4, 1, 2]


def test_rotate_left_accepts_empty_list():
    """R-04: Se puede rotar una lista vacía."""
    assert rotate_left([], 100) == []


def test_rotate_left_interprets_negative_steps_as_right_rotation():
    """R-04: Los pasos negativos rotan hacia la derecha."""
    assert rotate_left([1, 2, 3, 4], -1) == [4, 1, 2, 3]

def test_round_score_rounds_halfway_values_up():
    """R-05: Los valores a mitad de camino se redondean hacia arriba."""
    assert round_score_to_ten(15) == 20



def test_round_score_accepts_zero():
    """R-05: Cero es una puntuación no negativa válida."""
    assert round_score_to_ten(0) == 0

def test_rank_teams_breaks_ties_alphabetically_without_case():
    """R-06: Los empates se ordenan alfabéticamente sin distinguir mayúsculas."""
    entries = [
        ("beta", 50),
        ("Alpha", 50),
        ("Gamma", 80),
    ]

    assert rank_teams(entries) == [
        ("Gamma", 80),
        ("Alpha", 50),
        ("beta", 50),
    ]