# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

Prompt 1: Add proffesion docstring to every function in logic_utils.py
Prompt 2: Make sure pep8 style guidlines are used and make edits where neccessary

**Linting output before:**

The warning on pep8 violations given where regards to previous comments I made to highlight bugs. The problems it caught where lack of indentation and proper spacing for comments. Additionally while not cited as a pep8 violation it also fixed grammar mistake I made in comments.

**Changes applied:**

I applied every change so as said before proper grammer like capitlization was added to both comments. As far as pep8 rules are concerned spaces where add afetr the pound sign, indentation was added to one comment, and it turned one long comment into two seperate line comments that was more proffesionally worded. It did not see any problems with the docstrings it added even after a third prompt to check.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**


Promt given to each model
"There is an error in the scoring system for the following code. Please offer solution to fix the scoring system:" followed by a copy pasted version of the entire original code in app.py

| | Model A | Model B |
|-|---------|---------|
| **Model name** | GPT | Gemeni |
| **Response summary** | Fixes all probelsm it thinks has to do with the scoring system. Missed how the attempt counter is set incorrectly and mistook the debug score tracker for the actual score but did successfully fix the issues. Response was sigmented and only showed the parts that needed to change. | Outputed the entire editied code instead of just the nessecary parts. Did not update the scoring system but instead updated the debug score checker. Also solved unasked for bug where the hint would be incorrect |
| **More Pythonic?** | equally pythonic | equally pythonic |
| **Clearer explanation?** | GPT was cleaer as it explained the individual parts that made up the probelms and broke up the code more for easier reading | Less cleaer since output was one large lump of clode that didn't do what it was asked to. |

**Which did you prefer and why?**

I prefer GPT since it was clearer and more focussed where as Gemeni just seemd to hav eless efort put into it's output.
