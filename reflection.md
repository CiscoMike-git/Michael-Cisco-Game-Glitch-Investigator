# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game appears to be a number guessing game with three difficulty settings. It proposes to allow the user to submit a guess, change difficulty, restart the game, and the option to get a hint after each guess. When opted-in, the post-guess hint will indicate to the user the direction their guesses should move, higher or lower.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    1. If the "show hint" option is on and the player inputs an incorrect number, the hint output will falsely prompt the user, causing their guesses to shift further away form the secret number rather than closer to it.
    2. If the "show hint" option is on and the player consecutively inputs two incorrrect numbers, with one on each side of the secret number, then a hint output will not be provided.
    3. "Normal" mode sets the secret number between 1-100 while providing the user eigth guesses while "Hard" mode does so between 1-50 with five guesses.
    4. Secret number does not change when moving difficulty, meaning secret number can be out of range when moving to a smaller ranged difficulty.
    5. "New Game" button does not change game state while resetting game, meaning if the user already won or lost, they are unable to submit any more guesses.
    6. "History" and "Score" data persists between games.
    7. User is able to input data outside of denoted range and the guess still counts against the user's attempts.
    8. The UI element under the "Make a guess" title has the text "Guess a number between 1 and 100..." irrelavent of the set difficulty.
    9. The secret number is always a random number between 1 and 100, irrelavent of the set difficulty.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

    
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
