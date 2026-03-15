# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   The game's purpose is for users to guess a randomly generated secret number within a set amount of attempts and range based on one of the three potential difficulty choices: "Easy", "Normal", or "Hard".
- [ ] Detail which bugs you found.
   I logged a total of 12 bugs through the testing of the application outlined as follows:
      Bug ID #1: Hint UI element displaying the incorrect prompt after a submission.
      Bug ID #2: Hint UI element not displaying when two different message types are generated in succession.
      Bug ID #3: Numerics assigned to difficulty-related variables don't progress as expected when changing the difficulty setting.
      Bug ID #4: The game doesn't reset when the difficulty setting changes.
      Bug ID #5: Game state persists between games, blocking runs after a game completion.
      Bug ID #6: Score and history persist between games.
      Bug ID #7: The inputting of erroneous data is permitted and counts against the user's attempts.
      Bug ID #8: Select UI elements always display a range of 1-100 irrelevant of the difficulty setting.
      Bug ID #9: The secret number is always generated between 1-100 irrelevant of the difficulty setting.
      Bug ID #10: Even submission attempts above the secret number increase the user's score.
      Bug ID #11: The "attempts" variable is initialized to 1, meaning the player gets 1 less guess on the first game.
      Bug ID #12: The "history" display does not update immediately after a guess is inputted.
- [ ] Explain what fixes you applied.
   I fixed every discovered bug, as outlined above and in reflection.md, except for Bug ID #2 and Bug ID #12. The fixes applied are as follows:
      Bug ID #1: Changed each instance of "📉 Go LOWER!" to "📈 Go HIGHER!", and vice versa, in check_guess() (lines 52-63 - logic_utils.py) so the hint display would prompt users to guess closer to the secret number rather than further away as the initial layout would imply.
      Bug ID #3: Swapped the integer values associated with "Easy" and "Normal" in attempt_limit_map (lines 21-22 - app.py) and the second index of the "Normal" and "Hard" ranges in get_range_for_difficulty() (lines 8-11 - logic_utils.py) to ensure the difficulty of the game progressively scaled with the set difficulty.
      Bug ID #4: Added boolean logic to the "new_game" block (line 77 - app.py) to trigger if the difficulty setting was changed and made difficulty a variable in st.session_state (lines 47-48 - app.py), preventing mid-game rollover issues and out-of-range secret numbers.
      Bug ID #5: Added a "playing" assignment to the st.session_state.status variable on game reset (line 81 - app.py) repriming the game for continued play.
      Bug ID #6: Added a []/0 assignment to the st.session_state.history and st.session_state.score variables, respectively, on game reset (line 82-83 - app.py) thus setting them back to their initial values, preventing erroneous data persistence.
      Bug ID #7: Added range validation and integer verification to parse_guess() (lines 25-37 - logic_utils.py) to ensure only reasonable numerics, or numeric adjacents, could parse into the application, otherwise the input was appropriately handled and discarded. Moved the st.session_state.attempts increment to be within the input accepted block (lines 99-100 - app.py), causing only viable inputs to cause a loss of attempts.
      Bug ID #8: Replaced f-string's (line 53 - app.py) hardcoded range with the low, high variables, in their respective places, to ensure the range displayed to the interface was the one associated with the difficulty setting.
      Bug ID #9: Replaced the hardcoded 1-100 range assignment of st.session_state.secret (line 80 - app.py) with the difficulty-based low, high variables, ensuring the range of the randomly generated secret number matches the display and intentions as outlined in the logic_utils.
      Bug ID #10: Removed the erroneous even branch of the "too high" block in update_score() (lines 74-75 - logic_utils.py), preventing unexpected behavior derived from this code.
      Bug ID #11: Corrected the initial assignment of st.session_state.attempts (line 36 - app.py) from 1 to 0, ensuring each user gets the correct number of attempts when launching the application.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
   ![Winning Game](<Winning Game.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 1, insert a screenshot of your pytest execution here]
   ![Pytest Run](<Pytest Run.png>)
- [ ] If you choose to complete Challenge 2, explain how the agent contributed to the changes here.

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
