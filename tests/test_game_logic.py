from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # Bug fix: check_guess returns a (outcome, message) tuple, not a bare string.
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix tests ---

# Bug: parse_guess stub in logic_utils raised NotImplementedError.
# Fix: real implementation was moved from app.py into logic_utils.py.
def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


# Bug: secret was cast to str on even attempts, causing lexicographic comparison
# in check_guess. E.g. str "9" > str "10" is True (wrong), but int 9 < int 10.
# Fix: secret is always passed as int to check_guess.
def test_check_guess_integer_comparison_not_lexicographic():
    # With string comparison "9" > "10" is True, returning "Too High" (wrong).
    # With correct integer comparison 9 < 10, so result must be "Too Low".
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"

def test_check_guess_large_numbers_integer_comparison():
    # "100" < "20" lexicographically (wrong), but 100 > 20 numerically (correct).
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"


# --- Scoring tests ---

def test_score_correct_on_first_attempt():
    # First attempt win: 100 - 10*(1-1) = 100
    new_score = update_score(0, "Win", 1)
    assert new_score == 100

def test_score_correct_on_second_attempt():
    # Second attempt win: 100 - 10*(2-1) = 90
    new_score = update_score(0, "Win", 2)
    assert new_score == 90

def test_score_correct_on_third_attempt():
    # Third attempt win: 100 - 10*(3-1) = 80
    new_score = update_score(0, "Win", 3)
    assert new_score == 80

def test_score_decreases_by_10_each_wrong_attempt():
    # Verify the -10 per attempt pattern: attempt 1=100, 2=90, 3=80, 4=70
    scores = [update_score(0, "Win", attempt) for attempt in range(1, 5)]
    for i in range(len(scores) - 1):
        assert scores[i] - scores[i + 1] == 10

def test_score_minimum_is_10():
    # After many wrong attempts, score should floor at 10, not go negative
    new_score = update_score(0, "Win", 100)
    assert new_score == 10

def test_score_accumulates_across_rounds():
    # Score carries over: 0 + 100 (round 1, attempt 1) + 90 (round 2, attempt 2)
    score = update_score(0, "Win", 1)    # 100
    score = update_score(score, "Win", 2)  # 100 + 90 = 190
    assert score == 190
