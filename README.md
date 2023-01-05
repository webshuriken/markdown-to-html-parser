# Markdown to HTML parser

A simple markdown to html parser, module, written in Python. It is for the CS50W course project built with Django.

[![MIT License](https://img.shields.io/github/license/webshuriken/markdown-to-html-parser)](https://choosealicense.com/licenses/mit/)

## Table of Contents

- [Installation](#installation)
- [Run Locally](#run-locally)
- [Basic syntax](#basic-syntax)
- [Screenshots](#screenshots)
- [Features](#features)
- [Markdown Syntax](#markdown-syntax)
- [Lessons](#lessons)
- [Feedback](#feedback)
- [Future implementations](#future-implementations)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Installation

This project required Python version 3 to work. How to install it will depend on your operating system.
Here is the link to the [Python Installation page](https://www.python.org/downloads/).

## Run Locally

This instructions will run the program using the markdown file, demo.md, that was provided. Feel free to edit or change this file. The parser was made to be integrated with my Django app.

Clone the project

```bash
git clone https://github.com/webshuriken/markdown-to-html-parser
```

Using the command prompt, terminal, go to the project directory

```bash
cd my-project
```

In the command prompt, terminal, run Python

```bash
python
```

Now with Python running, import the module and use it.

```python
import mk2html

# You can call the demo function to use the demo markdown
print(mk2html.demo())

# Or you can create a markdown file inside the /docs folder, '/docs/example.md'
# then pass the name of the file you created to the function 'parse_file'.
# no need to add the file extension as the parser will auto check for a valid extension
print(mk2html.parse_file('example'))
```

## Screenshots

![markdown to html screenshot](/screenshot.png)

## Features

- Headers, Links, Lists, Bold text and Paragraphs support
- Made to be used as a module
- Search file system for file name provided by user
- Try and catches any errors produced when accessing the markdown file.

## Markdown Syntax

[Basic markdown rules](/baisc_markdown_syntax.md)

## Lessons

At first, I thought that creating this parser would be easy until I read the documentation. It thought me that creating something like a list, is not as simple as just checking for the list marker. You need to take into account if tabs or spaces were used to build the list. Then you need to check where the current list marker sits according to the marker above it. It provide a nice learning curve which was fun.

Apart from learning a lot about markdown I also had the pleasure of increasing my Python knowledge. Further improved my understanding of lambda function and list comprehensions. There is also the use of `strip()` to remove white spaces which I kept getting confused with the JS version called `trim()`. Python seems to have a function for everything.

## Feedback

If you have any feedback, please reach out to me at webshuriken@gmail.com

## Future implementations

**paragraphs**
- ability to handle line breaks.

**links**
- ability to handle white spaces in the url.

**Emphasis**
- handles italic text

**Horizontal rules**
- creates a horizontal line, from the left to the right margin

## Authors

- [Carlos E Alford](https://www.github.com/web-shuriken)

## Acknowledgements

 - [W3schools](https://www.w3schools.com/python/)
 - [Python regex Docs](https://docs.python.org/3/howto/regex.html)
 - [Markdown guide](https://www.markdownguide.org/basic-syntax#ordered-lists)

## License

[MIT](/LICENSE)
