
# Google Auto Complete Text

> A simple CLI for text auto completion using Trie Data Structure with cooperation with Google company.

<div align="center"><img src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Autocomplete_1.max-1100x1100.png
" width="400" height="300"/></div>

<br>

---

### Table of Contents

- [Google Auto Complete Text](#google-auto-complete-text)
    - [Table of Contents](#table-of-contents)
  - [Description](#description)
    - [Technologies](#technologies)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Updating/The Development Cycle](#updatingthe-development-cycle)
    - [Releasing](#releasing)
    - [Back-end](#back-end)
  - [References](#references)
  - [License](#license)
  - [Author Info](#author-info)

---

## Description

CLI that can process big amount of data in a Trie data structure and find auto completion for the user's text and get top-k suggestions.
The system does that with preprocessing and cleaning the data from unnecessary and redundant text.
It can do 2 ways of completion:
  1. Full auto completion.
  2. Auto completion with spelling error correction:
    2.1. Substitution correction.
    2.2. Removal correction.
    2.3. Add correction.
The system searches for a completion **smartly**, only using the trie data structure, if there is no full auto completion it tries to find the most appropriate completion and then substitute the missing one, after that removing the not matched characters and at the end trying to add more characters from the trie data structure.

### Technologies

- Python
- Pycharm

[Back To Top](#Google_auto_complete)

---

## How To Use

### Installation

- Copy this link ***https://github.com/loayjb96/Google_auto_complete.git*** then on cmd or bash do:

		cd ~/Desktop
		git clone {{the link you just copied}} auto-complete

- This creates a directory named "Project", clones the repository there and adds a remote named "origin" back to the source.

		cd auto-complete
		git checkout develop

- If that last command fails

		git checkout -b develop

------------
### Updating/The Development Cycle

You now have a git repository, likely with two branches: main and develop. Now bake these laws into your mind and process:

You will never commit to ***main*** or ***develop*** directly .

Instead, you will create ***feature branches*** on your machine that exist for the purpose of solving singular issues. You will always base your features off the develop branch.

		git checkout develop
		git checkout -b my-feature-branch

This last command creates a new branch named "my-feature-branch" based off of develop. You can name that branch whatever you like. You should not have to push it to Github unless you intend to work on multiple machines on that feature.

Make changes.

	git add .
	git commit -am "I have made some changes."

This adds any new files to be tracked and makes a commit. Now let's add them to develop.

	git checkout develop
	git merge --no-ff my-feature-branch
	git push origin develop
------------
### Releasing

Finished with your project?

- Create a feature branch as normal.
- Update the version history in the README.md file
- Update this to develop as normal.

		git checkout master
		git merge --no-ff develop
		git push origin master
		git tag v1.0.0
		git push origin v1.0.0
------------

### Back-end

To run locally, do the following on Backend directory:

1. Create a Python 3.5 virtualenv

2. Install dependencies:
	
```
pip install -r requirements/dev.txt
npm install
```

   Alternatively, use the make task:

```
make install
```
    

in auto-complete directory you can run:

```
python main.py
```
then start to type input for the system in order to get top 5 suggestions, you can type # in order to finish the line and start new line, or #q in order to exit the program.

[Back To  Top](#Google_auto_complete)

---

## References

[`Python`](https://www.python.org/)
[`Pycharm`](https://www.jetbrains.com/pycharm/)

[Back To  Top](#Google_auto_complete)

---
## License

GPL License

Copyright (c) [2021] [Loay Jaber & Aseel Nassar]

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

[Back To The Top](#Google_auto_complete)

---
## Author Info

- Github - [loayjb96](https://github.com/loayjb96) | [AseelNa](https://github.com/Aseelna)
- Linkedin - [Loay Jaber](https://www.linkedin.com/in/loay-jaber/) | [Aseel Nassar](https://www.linkedin.com/in/aseel-nassar-739457160/
)




[Back To The Top](#Google_auto_complete)