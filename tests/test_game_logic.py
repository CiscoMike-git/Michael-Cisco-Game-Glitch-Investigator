from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
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

def test_hint_says_go_lower_when_guess_too_high():
    # Guess above the secret should hint to go lower
    _, message = check_guess(75, 50)
    assert "LOWER" in message

def test_hint_says_go_higher_when_guess_too_low():
    # Guess below the secret should hint to go higher
    _, message = check_guess(25, 50)
    assert "HIGHER" in message