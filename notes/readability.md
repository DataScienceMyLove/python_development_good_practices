# Why Readability is Important?

## The Question: Why Care About Code Readability?

We tend to think: why should I take efforts about the readability of my code if the code works?

Who really cares what it looks like?

This perspective starts to deteriorate when **we start working with a team** or when a person is telling you **sorry no context, no docstrings, no time for you** when sharing your code.

## Three Real Reasons Why Readability Matters

### 1. Collaboration

**Code reflects skills level & respectability.**

Consider that other people will work on your code. They need to understand it, and it's respectful to write code that's easy to read. It helps people save time.

> ***The code you will write will be read more often by others than yourself.***

You will thank yourself when you browse an old codebase and think: "Fortunately I added context to my code for my LLM to understand it better".

### 2. Standardization

**Code that meets standards is easier to integrate.**

Standardization is important because it ties into automation and scripting.

**Key concepts from standardization:**
- Naming conventions
- Reusable code  
- Don't Repeat Yourself (DRY)

#### Naming Conventions
**Naming conventions** is one of the hardest problems in computer science—to name things like variables. When you start building systems and automation around them, naming conventions become very important.

#### Reusability & DRY
**Reusability** and **DRY** can be represented with the same concept: **functions**. When you have to repeat the same logic more than once, it's time to think about writing one or more functions, or simply a whole package to reuse the logic through methods. It will avoid boring DRY blocks.

### 3. Professional Side

**Clean code makes a positive impact on coworkers & interviewers.** That leaves an impression on them.

You have an opportunity to leave a good impression on your interviewers if you:
- write clean code
- use automation tools that make sense
- build a system of reproducibility to prevent break events

**Team respect and growth:** This also has an effect on your coworkers gaining more respect and tending to new responsibilities in a team—work on new projects, get a promotion, improve the onboarding process of new team members.

**Avoid deployment issues:** You will avoid deployment issues such as stupid syntax errors and tab or space indentation problems. If you're working on a system with CI/CD pipelines and after a lot of work with merges and PR reviews, your pipeline breaks because of a tab or a space indentation that was incorrect—painful!

Those types of errors can be easily avoided earlier in the process with a shift left mentality.

## Conclusion

There are few reasons why readability is important, and while browsing your app through steps, we will see how much it can save time for yourself and the people who work with us.




