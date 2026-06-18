def get_range_for_difficulty(difficulty: str):
    """
    Return the numeric range for the given difficulty level.

    Maps a difficulty string to a (low, high) tuple representing the
    inclusive bounds of the secret number range used during gameplay.

    Args:
        difficulty (str): One of "Easy", "Normal", or "Hard".

    Returns:
        tuple[int, int]: A (low, high) pair where low <= secret <= high.
            - "Easy"   -> (1, 20)
            - "Normal" -> (1, 100)
            - "Hard"   -> (1, 200)
            - unknown  -> (1, 100) as a safe default
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # Bug fix: return 1, 50 for Hard and replaced it with 1, 200
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse raw user input into an integer guess.

    Accepts whole numbers as strings and converts decimal strings (e.g.
    "7.0") by truncating the fractional part via int(float(raw)).

    Args:
        raw (str | None): The raw text entered by the user.

    Returns:
        tuple: A three-element tuple (ok, guess, error) where:
            - ok (bool): True if parsing succeeded, False otherwise.
            - guess (int | None): The parsed integer on success, else None.
            - error (str | None): A human-readable error message on
              failure, else None.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare the player's guess against the secret number.

    Handles both numeric and string comparisons gracefully via a TypeError
    fallback so mixed-type inputs do not crash the game.

    Args:
        guess (int | str): The value the player submitted.
        secret (int | str): The target value the player is trying to guess.

    Returns:
        tuple[str, str]: A (outcome, message) pair where outcome is one of:
            - "Win"      — the guess matches the secret exactly.
            - "Too High" — the guess is greater than the secret.
            - "Too Low"  — the guess is less than the secret.
        message is a short feedback string suitable for display in the UI.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    # Fixed opposite logic for too high/too low; TypeError fallback handles
    # mixed str/int comparisons without crashing.
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Calculate and return the new score after a guess attempt.

    Scoring rules:
        - Win:      awards (100 - 10 * (attempt_number - 1)) points,
                    with a minimum award of 10 points to prevent zeroing out.
        - Too High: deducts 5 points as a penalty for overshooting.
        - Too Low:  deducts 5 points as a penalty for undershooting.
        - Other:    score is unchanged (no-op for unrecognised outcomes).

    Args:
        current_score (int): The player's score before this attempt.
        outcome (str): Result of the guess — "Win", "Too High", or "Too Low".
        attempt_number (int): 1-based count of how many guesses have been made,
            used to scale the win bonus (earlier wins earn more points).

    Returns:
        int: The updated score after applying the relevant rule.
    """
    if outcome == "Win":
        # Bug fix: remove unecessary +1
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # Bug fix: remove nested if and simply remove points
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
