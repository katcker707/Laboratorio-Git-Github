from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)
def test_normalize_answer_supports_turkish_dotted_i():
    assert normalize_answer(" İstanbul ") == "i̇stanbul"

def test_normalize_answer_keeps_internal_spaces():
    assert normalize_answer("  P y t h o n  ") == "p y t h o n"