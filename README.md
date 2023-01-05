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

Here is the syntax currently supported by the parser.

If you encounter unexpected results refer to this guide.

### Headers

1. Number if hashes `#` correspond to the heading level. Use a single hash `#` for the main title and siz hashes for the lowest level title.
2. There has to be a single space between hash and first letter of the title
3. The hash sign can not be preceeded by any empty space or character

```md
# Main heading

###### lowest level heading
```

### Paragraphs

1. Use blank lines to separate one paragraph from the next
2. Do not indent paragraphs with tabs or spaces
3. Text inside paragraphs can contain bold text and links

```md
The first paragraph goes here.
This line will be put together with the one above.

Now the second starts with a space in between the previous paragraph and this one.
```

### Bold text

1. Append and prepend words with double underscores or asterisks without any space inbetween
2. Don't mix symbols together. The start and end tags must be created with the same symbol.

```md
__ONE-WORD__` OR `**ONE-WORD**
Using __many words__ is fine
It can also be used be**wee**n letters in a word
```

```md
// Please don't do this

This sentence uses **asterisks__ at beginning and ends with underscores

// Do this

Now this will work way **better** with no side effects
Using __many words__ is fine
It can also be used be**wee**n letters in a word
```

### Links

1. The text which is linked is wrapped in square brackets `[link]`
2. The url for the linked text is wrapped in round brackets `(url)`
3. There are no spaces between the link and the url. If you put spaces between the the square and round brackets then the parser will just treat it a normal text.
4. Checking that both the link and url are in correct format is not the parsers responsibility!

```md
A [link](www.wiki.com) can live within a paragraph.

A link can also be on its own.
[My business site](https://supersalon.co.uk)
```

### Lists

**Note:** Currently the parser only supports unordered lists.

#### Unordered lists

1. An unordered list is created using one of these markers `+ - *`. A new list is not create for each marker you use, they can be used interchangeably.
2. The first list item can only be placed at the beginning of the line, 2 spaces, 4 spaces or a tab away from the left margin.
3. To create nested lists you place the list marker 2 spaces, 4 spaces of 1 tab from the list marker above it.
4. To separate lists from each other you just leave one empty line between the list markers.
5. If you start spacing a list using Tabs you must indent the rest of the same list with Tabs and the same goes for spaces. When Tabs and spaces are mixed the list will not be created.

```md
All of these are valid ways to create a simple list, without nesting other lists.

- item one
- item two

* item one
* item two

+ item one
+ item two

- item one
+ item two
* item three

  - item starting 2 paces away
  - item two

    - item starting 4 spaces or a tab away from the left margin
    - item two
```

```md
To create nested lists indent the list marker by 2 spaces, 4 spaces or a tab from the list marker above it.

- item one
- item two
  - nested list item one with 2 spaces from the list marker above it
  - nested list item two
- item three

- item one
- item two
    * nested list item one with 4 spaces or 1 tab from the list marker on the line above
    * nested list item two
+ item three

```

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
