# Basic markdown syntax

A basic set of rules supported by the mk2html parser when creating markdown files.

## Basic syntax

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