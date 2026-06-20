# python_development_good_practices

**A little project to show the different way to improve Python code with tools and environment**

Readable, clean, organized code is very important when you're beginning projects and when you're collaborating in a team.

A little overview of this repo which will be organized by branch. For each new branch you will get a new version of the basic app to finish with a Pythonic, linted, formatted, containerized app with a bunch of good practices of development that can help you to facilitate things when something breaks.

The purpose of the app is just printing a text in ASCII art from the user.

### Overview of the covered topics

A little overview to have some landmarks on the covered concepts:
- [Why readability is important?](notes/readability.md)
- [Writing Pythonic code](pythonic_code/writing_pythonic_code.md)
- Linting and formatting with Flake8 and Black
- Virtual environments
- Automation tools like pre-commit hooks and testing with git
- Packaging/Containerizing your app

Feel free to retrieve all this subjects in the `notes/` folder

#### ***Who is this repository for?***

It's going to be helpful to take your code and get it to the next level.

It can be useful for *Data Analysts* or *Data Scientists* that aren't going to come from Software engineering or development background .
You will learn some tools to enhance your coding skills and have better impression on interviewers to stand out whether live coding or take home assignments.

**Overview of the app:**

Branch | Description
--- | ---
`v1` | The starting point
`v2` | Code becomes Pythonic
`v3` | Linting and formatting gets added
`v4` | Venv module from standard library
`v5` | The new alternative: uv
`v6` | Automation tools: pre-commit hooks
`v7` | Docker containerization of the app
`whl` | Information about building a whl file for package distribution

***Browse the branches to see changes of the app according to the incorporation of tools and concepts of good practices development***

### How to use it in local

**Clone the repo in the directory of your choice:**
```bash
git clone  https://github.com/DataScienceMyLove/python_development_good_practices
```
**Enter in the git repository:**
```bash
cd python_development_good_practices
```
**List all branches:**
```bash
git branch -a
```
**Go on the version of the app you want to explore:**
```bash
git checkout v1
```
It will create the branch which doesn't exist still.



