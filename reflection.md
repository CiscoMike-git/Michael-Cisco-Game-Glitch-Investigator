# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game appears to be a number guessing game with three difficulty settings. It proposes to allow the user to submit a guess, change difficulty, restart the game, and the option to get a hint after each guess. When opted-in, the post-guess hint will indicate to the user the direction their guesses should move, higher or lower. However, there are significant bugs which prevent the software from executing as intended.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    1. If the "show hint" option is on and the player inputs an incorrect number, the hint output will falsely prompt the user, causing their guesses to shift further away from the secret number rather than closer to it.
    2. If the "show hint" option is on and the player submits two consecutive inputs that would each output a unique message type (i.e. st.success, st.error, st.warning), then a hint output will not be displayed contrary to intent.
    3. The various difficulty settings are as follows: "Easy" mode (Range: 1-20, Attempts: 6), "Normal" mode (Range: 1-100, Attempts: 8), and "Hard" mode (Range: 1-50, Attempts: 5). Difficulty should progressively increase as the setting does (i.e. easy range < normal range < hard range & easy attempts > normal attempts > hard attempts), not bounce around as it currently does.
    4. Game does not restart when changing difficulty, leading to a problematic mid-game rollover. When changing difficulty, game should completely reset and call a new secret number.
    5. The "New Game" button does not change the game's state while resetting the game, meaning if the user already won or lost, they are unable to play again as intended because they are locked out of submitting any more guesses.
    6. "history" and "score" data persists between games, despite the fact that they should reset instead.
    7. User is able to input erroneous data (outside of denoted range, non-numeric, non-integer decimal) and the guess still counts against the user's attempts. Erroneous data should not be allowed to be inputted, or should be handled, without decrementing the user's number of attempts left.
    8. The UI element under the "Make a guess" title has the text "Guess a number between 1 and 100..." irrelevant of the set difficulty. This display should be dynamic, showing the correct range for the selected difficulty.
    9. The secret number is always a random number between 1 and 100, irrelevant of the set difficulty. The secret number should be clamped to the range outlined by the selected difficulty.
    10. On even submission attempts (i.e. 0, 2, 4) when the player guesses too high, score is increased by 5 points instead of being decreased by that amount.
    11. On game's initialization, the "attempts" variable is set to 1 (i.e. the user has submitted one guess), number of attempts should always start at 0.
    12. When submitting a guess, the "history" data is not updated until the next page update. This variable should immediately update as to allow the user to know what guesses they have already provided.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    The AI's suggestion to fix Bug ID #1 correctly associated that the second index (string) of the return array for check_guess() was incorrectly coded (i.e. correct returns were inversed between the two possible outcomes for incorrect guesses). After reviewing the AI's suggestion, and deeming it a viable solution through logical deduction, I allowed the AI to make the alteration to the code. After the change was made, I reviewed the altered code to ensure no erroneous changes were made. Next, I relaunched the application and operated the software to confirm a change of behavior into the expected execution. Finally, I asked the AI to create a unit test for the bug fix, scrutinized and confirmed it, then ran the "pytest" command to assert that the code outputted the correct values.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    While originally attempting to fix Bug ID #2, the AI offered information that, while viable to the overall code structure, failed to provide an accurate outline and explanation of the problem causing an erroneous solution to be generated. During this instance, the AI affirmed that a purposeless bi-submission typecast led to incorrect string comparison evaluations allowing fall through and creating the straddle logic that prevented the hint element from showing. When the AI originally pointed out where the error was located, I was sceptical, marking it as such, as the suggested change appeared viable but unrelated to the bug. Upon making the alteration and executing the program again, I found no change of behavior regarding this bug, but decided to keep the alteration as it was objectively better code than the prior iteration. Later, I deduced we were both wrong, the bug had nothing to do with numeric straddling but with different message types being generated; my original bug report was incorrect, which in turn likely poisoned the well of the AI's response.
    
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    In order to assert that a bug was actually corrected, I utilized diverse redundancy via the engineer's logical deduction, AI generated unit tests (when possible), and player's quality assurance testing. For logical deduction, I analyzed the suggested and actual changes the AI made to the codebase. If the bug was truly corrected, I should be able to articulate what caused it and how the changes circumnavigated that original execution. Similarly, when operating the software, a fixed bug simply wouldn't be experienced post fix, allowing basic quality assurance testing to greatly facilitate testing and confirmation. Finally, the AI was able to generate unit tests which, with programmer's scrutiny, could offer a data-driven test of the execution.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    When I discovered Bug ID #4, I was looking at the Developer Debug Info while providing inputs to UI elements. When altering the index of the difficulty selection box, I discovered that the game will rollover without resetting. This had the potential to cause significant issues to the user experience, such as the secret number potentially not being in the denoted range, the user not getting their full number of attempts, and data variables, such as score and history, being persistent between runs. These issues would irritatingly force users to input an additional new game prompt if they decided their current difficulty was too easy or hard mid game. Through this test, I discovered that there was no branch in the codebase that directly handled inputs from the difficulty selection box, with any alterations to the game's settings being made as an afterthought rather than reactively as it should have.
- Did AI help you design or understand any tests? How?
    In order to increase my familiarity with AI and prompt engineering, I extensively utilized AI to create and modify unit tests. After fixing each bug, I would request the AI to propose a set of unit tests to thoroughly ensure the bug was taken care of. I would extensively scrutinize the yield from this prompt, which I took significant time to ensure was clear and detailed, taking time to understand the premise of the proposed unit test, what it tested, and its manner of execution. Typically, this process was completed through a single handshake but occasionally required several iterations to refine the tests, concluding with the AI being instructed to make their proposed alterations to the codebase.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    The secret number changed in the original app due to lines 92-93 and lines 134, 136 of app.py. Lines 92-93 initialized the persistent "secret" variable upon the application's opening, creating the variable at runtime and providing it with an initial value. During the program's execution, when the "New Game" button was pressed, the program would nest into line 134's if statement and execute line 136, which gave a new random value to the variable "secret".
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    A Streamlit rerun is a complete repeated execution of the associated script, without variable persistence. A rerun occurs when the application needs to update, such as when an input is registered or the "rerun" command is executed. Despite variables not persisting, state information for UI elements and data added, or modified, within the "session_state" object do persist. The session state can be thought of like a dictionary that persists between reruns, maintaining key/value pairs to be called and which can be overwritten and saved by the script during its execution. This allows the application to remember and react to user interactions while maintaining the page's layout and critical data.
- What change did you make that finally gave the game a stable secret number?
    The secret number was stable at the point of my initial testing, it did not change unless a "New Game" prompt was submitted. However, the claim could be made that it was overly stable, not being altered when the difficulty setting was changed, or erroneous, as it always pulled from the range of 1-100. The prior bug was fixed with Bug ID #4 in Commit ID #14, where difficulty was added to the "session_state" object (lines 47-48 - app.py) along with a change trigger on line 77 of app.py (after the commit). The later one was fixed with Bug ID #9 in Commit ID #10, when line 110 of app.py was changed to utilize the low, high variables for the selected range.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
        In future endeavors, I would like to reimplement bug triaging when I begin to debug my code. During this project, the AI and I both found Bug ID #2 to be a difficult one to understand and hammer down, spending significant time and thought on it. After extensive testing, I believed that the problem may have been a culmination of other bugs, prompting me to triage this bug for a later time, fixing the others first then returning to it. By operating in this manner, I allow myself to spend less time on a single bug that I don't understand while removing additional variables from the problem when I do attempt to figure out or solve it.
- What is one thing you would do differently next time you work with AI on a coding task?
    The next time I work with AI on a coding task, especially if it's a project or exercise, I want to preface the AI to not give me answers before I ask for them. I found that upon doing the initial "#file:app.py" command, the AI appeared to give me the predetermined answers, as outlined by CodePath, to the project. This made trying to earnestly find and repair additional bugs in a learning manner difficult as I suddenly knew CodePath's intentions rather than needing to critically think myself.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    Prior to this project, I interpeted "Vibe/AI Coding" as asking an AI to generate code and going with whatever it produced. I am pleasantly surprised to learn it is, when used correctly, a tool to assist coding rather than a solution generator.

---

## 6. Challenge 5

- Explain the bug and AI models that were utilized for the comparison?
    The bug in question was Bug ID #7, which covered erroneous data being accepted while still decrementing the number of attempts left. The two AI models called on to solve this problem were Claude Code during the bug fixing stage and Github Copilot after the bug was fixed, reflecting on it.
- How did the prompting between the two models differ?
    As I was attempting to figure out the bug, Claude Code was faced with less user derived information during prompting and wasn't explicitly told to explain the bug. On the other hand, as Github Copilot was reflecting on the bug after the fact, it was able to pull the full updated bug report and was explicitly told to explain the bug. 
- How did each model's answers compare?
    While the totality of each model's suggestions were identical in solving the problem, it appears that Github Copilot required more prompting to explain the bug over Claude Code which needed more information to diagnose. Additionally, Claude Code presented the suggestion in a more concise and readable manner, providing lists and modifying format when applicable. Github Copilot, on the other hand, created a wall of text that was difficult to read in select places. Between the two, I definitely preferred Claude Code over Github Copilot as Claude Code required less, gave more, and was easier to comprehend.