# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like The first time you ran it?

The hint button was checked immedietly but no hint was given. I am told to guess number between 1 and 100 with 7 attempts left. There is submit button, new game and the hint button as well as a "developer debug info" dropdown menu

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

As stated in the example the hints tell me lower when its higher, and higher when its lower. The score in the debug window and the final out put do not match. The new game button does not start new game under some curcumstance,  have to reload web page. Edge case of not putting in number does not cause game over. The website starts with 7 attempts but new games give 8 attempts and Attempts run out 1 to early

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 7 | go Higher | go lower | none |
| u | out of attempts/or not change to remaining attempts | game continues | none |
| 7 (secret value of 12) | go higher | fluxates between go higher and go lower | none |
| 7 | score of 100 | 70 | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When asked to explain to me the check guess function ai accurately explained that the advice was swapped. I verified this by reading the code snippet highlighted to verifiy the underlying logic and came to the same conclsuion. It suggested simply rewriitng the output text which would be the the correct advice before any logic before any refacotring.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I had asked the ai how to correct the point score system. The ai correctly identified a 2 errors such as the formula being written wrong on line 53 and an intention condition to add points for the wrong reason on line 58-61 which I verified simply by checking the code. This was misleading though because it did not take into account that the attempt counter was also buggy so even if these changes were implemented the score counter would not be fully fixed.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Firts I created a pytest using claude to check for if the bug was present. After reviewing the tests to make sure it should do what I want I implemented the changes and ran the test. Finally I would use streamlit to check the website personal to ensure the bug was no longer able to be recreated and no other bugs had shown in its place.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran was to make sure the scoring system works. The goal was for it to have a max score at 100 and go down by 10 for each incorrect answer. The test showed the changes made were successful and after running I was given a summary of how the tests worked to prove the code worked correctly.

- Did AI help you design or understand any tests? How?

Since I am unfamiliar with pytest I had ai help me create them. The overall syntax made it easier me to grasp since I have done test before in a different language 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

When streamlit is used to create a web application it treats the code like a linear script meaning the code is read top to bottom to figure out how to work the website. Because of this streamlit is "rerun" for every interaction on the website to ensure everything works. Because streamlit creates websites in a very simplified way it uses "session states" to remember the way things were before the interaction so that you interaction can have lasting effects.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One habit I want to reuse is making sure to clarify the ai what it is telling me. When code is suggested i have to be careful to not always accepts and read it carefully. During this project a lot of hassle was saved by simply finding something weirs in the suggestion and then asking the ai about it to make sure which usually resulted in a correction.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I will put more effort into being specific when prompting so I can try to catch things the first time instead of wasting tokens.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

Beofre I was generally overly cautious on using AI code for any large amount of work but after this I feel more confiedent to use AI safeley and efficently.
