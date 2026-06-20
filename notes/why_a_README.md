# Why a README?

## Understanding the Purpose of a README

When we arrive on your repo, we have to understand why we are here and what we are supposed to do for using your project.

The README.md is such a convention to say: **when you arrive in my repository or in a subfolder of the project, come here to understand what we do here.**

---

## What Should Your README Include?

It should explain if your repository is an app:
- what the application is
- how to run it
- how to install it
- prerequisites (technical or level of the student)

Any requirements should have an example of **"how to use it"** (like a Death Note haha)

---

## Documentation in Software Development

### The Value of Comprehensive Documentation

Documentation with a lot of examples is a great plus in software development. Even more when the project is big, messy, with nested directories.

You can save a lot of time to the users by explaining the functionalities, the use cases and explaining how your project is built to those who want to reproduce it for their own use cases.

### The Challenge: Keeping Documentation Updated

Maintain documentation for a software is a main issue: software is always evolving, dependencies too, people are developing, iterating, and your application becomes already obsolete.

So docs often fall in the wayside and become old: it can be very frustrating for someone who gets on board.

**Update your documentation by the README is tedious, it's not the most exciting part but it's essential when you want your app to endure over time.**

---

## FastAPI: Documentation Done Right

### A Modern Approach

**FastAPI** is an API framework in Python that has revolutionized the field precisely because of this feature: it generates and updates your API documentation in real time, automatically, without you having to write a single line of HTML or JSON for the spec.

### How Does It Work?

FastAPI is built on two pillars of modern Python that we mentioned earlier:

**Type Hints** (PEP 484): You declare the type of your variables (e.g. `id: int`).

**Pydantic**: You define the structure of your data as classes.

### Automatic Documentation Generation

By reading your native Python code, FastAPI automatically generates a specification file in the global OpenAPI standard. It then injects this file into interactive graphical interfaces.

By default, without any configuration, your project provides you with two ready-to-use documentation tools:

- **Swagger UI** (accessible via the URL `/docs`): Allows you to test the API directly from your browser.

- **ReDoc** (accessible via the URL `/redoc`): Crystal-clear, production-ready documentation.

**Note for the course**: you will see the evolution of a README.md through the versions of our app beginning to [v1 branch](https://github.com/DataScienceMyLove/python_development_good_practices/tree/v1)


**Another way to keep a project/software in a healthy state is: [Testing](/notes/testing.md)**