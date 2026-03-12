def get_range_for_difficulty(difficulty: str):
    # FIX: Bug ID #3 - Swapped Normal/Hard ranges via Claude Code, Progressive difficulty: Easy (smallest
    # range) → Hard (broadest range)
    """Return (low, high) inclusive range for a given difficulty."""
    match difficulty:
        case "Easy":
            return 1, 20
        case "Normal":
            return 1, 50
        case _:
            return 1, 100  # Hard, or any unrecognized difficulty

def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    # FIX: Bug ID #1 - Swapped return[2] strings for incorrect guesses via Claude Code
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

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
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5  # FIX: Bug ID #10 - Removed incorrect even/odd branching that rewarded +5 on even attempts via Claude Code, "Too High" should always penalize identical to "Too Low"

    if outcome == "Too Low":
        return current_score - 5

    return current_score
