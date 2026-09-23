from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)
def test_rotate_left_does_not_mutate_input():
    original = [1, 2, 3]
    resultado = rotate_left(original, 1)
    assert resultado == [2, 3, 1]
    assert original == [1, 2, 3]


def test_unique_tags_does_not_mutate_input():
    original = ["a", "b", "a"]
    resultado = unique_tags(original)
    assert resultado == ["a", "b"]
    assert original == ["a", "b", "a"]