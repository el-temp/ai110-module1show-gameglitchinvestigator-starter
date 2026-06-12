# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like The first time you ran it?
The hint button was checked immedietly but no hint was given. I am told to guess number between 1 and 100 with 7 attempts left. There is submit button, new game and the hint button as well as a "developer debug info" dropdown menu
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
As state in the example the hints tell me lower when its higher, and higher when its lower. The score in the debug window and the final out put do not match. The new game button does not start new game under some curcumstance,  have to reload web page. Edge case of not putting in number does not cause game over. The website starts with7 attempts but new games give 8 attempts and Attempts run out 1 to early

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 7 | go Higher | go lower | none |
| u | out of attempts/or not change to remaining attempts | game continues | none |
| new game | attempt number reset & unlocking submission button| exact opposite but only if all attempts are used. New game while there are remaining attempts works *(causes problems with attempt counter and registering of higher and lower) | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When asked to explain to me the check guess function ai accurately explained that the advice was swapped
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
