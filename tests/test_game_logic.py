from logic_utils import check_guess, get_range_for_difficulty, update_score

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

def test_difficulty_ranges_scale_progressively():
    # Easy < Normal < Hard: each difficulty must have a strictly larger range than the one before
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high

def test_update_score_win_early_attempt():
    # Winning on attempt 1 should give 100 - 10*(1+1) = 80 points
    assert update_score(0, "Win", 1) == 80

def test_update_score_win_minimum_points():
    # Win points floor at 10 regardless of late attempt number
    assert update_score(0, "Win", 100) == 10

def test_update_score_too_high_penalizes():
    # "Too High" should always deduct 5, not reward +5 on even attempts (Bug #10 fix)
    assert update_score(50, "Too High", 2) == 45

def test_update_score_too_low_penalizes():
    # "Too Low" should always deduct 5
    assert update_score(50, "Too Low", 1) == 45

def test_update_score_unknown_outcome_unchanged():
    # Unrecognized outcome should leave score unchanged
    assert update_score(100, "Draw", 3) == 100