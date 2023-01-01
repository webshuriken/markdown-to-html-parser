# Parser Plan

Lets plan out the steps to create the parser.

## Issues

- List items
The first item of a list are not following the rules properly. An item can be placed 1 space away from the margin and the parser says its valid. This causes a domino effect that can affect all subsequent list items. The issue can end up creating unwanted lists.
So if the first item sits next to the margin a list is created for it and for the second item which sits only 1 space away from the margin another list is created. What should have been a single list with two items is now two lists with one item each.
```js
- the first item
 - the second item
```

- paragraphs ✅ (SOLVED)
Paragraphs are meant to be separated using a space between two lines. Currently if the user presses 'Enter' to carry on below the current line, without any space between them, it treats it as a separate paragraph which is not the case.. The regex separating the document lines into a list needs looking into..

## Global Plan

1. Find the markdown file
  - create function get_md_file ✅
  - import the exists() function from the os.path module to check the files existence ✅
  - using ternary operator check for popular .md extension first ✅
    - if does not exist, check for the .markdown extension ✅
    - if neither exists, store 'False' ✅
  - if the file exists:
    - open, read, save to memory and close the fileb ✅
  - else
    - return 'File Not Found' ✅

2. create function to organise it all in order
  - call it init_parser ✅
  - invoke get_md_file and store its return value in variable f ✅
  - import regex module ✅
  - use regex to split the file text at each line ✅
  - place the split file list into a while loop until it reaches 0 length ✅
Because all files start with a title, that is the first thing we will look for
  - call get_header() and store its result in 'header' variable ✅
  - if header is True:
    - a header was found and must be added to the global html_list ✅
    - now pop the first item from the md_file_lines list ✅
    - continue to next loop iteration ✅
  
3. check for headers
  - create function called get_header ✅
  - function takes one parameter, file_line ✅
  - use regex to match the use of header ✅
  - store the result of match in header variable ✅
  - check if the header was found, returns a tuple with True/False and the value from regex ✅
  - if so:
    - use the end() method to find the header level ✅
    - create html string ✅
  - else:
    - return false ✅

4. check for lists. This step is a bit more complicated because lists can contain other lists so we must track each item and its indentation to know in which list they belong.
  - create function called get_ul_lists that takes one parameter all_file_lines ✅
  - create a list that holds dictionaries {level: number, end: number}. 'list_levels' ✅
  - create a variable 'current_level' to store the current list level ✅
  - create variable to hold the 'html_list' as array ✅
  - use regex to match beginning of list, only 4 spaces or 1 tab is allowed ✅
  - if there is a match: ✅
    - add `<ul>` as first item to the html_list ✅
    - **WHILE LOOP**
    - use while 'current_level' is more than or = 0 ✅
      - append the first line from the 'all_file_lines' as we know this is valid list item `<li>some text`, leave the closing li tag incase of nested list ✅
      - remove the first item from the `all_file_lines` list ✅
      - use regex to match the next line. It will look for the first occurrence of the marker at the beginning of the text. ✅
      - if match and match is equals to the current level ✅
        - concat `</li>` to end of the last list item in html_list ✅
      - else if match and match is equals to current level plus two (we have a nested list) ✅
        - append `<ul>` to the html_list ✅
        - increment 'current_level' by 1 ✅
        - append current level info to 'list_levels' array
      - else if match and match is less than current 'current_level' ✅
        - concat `</li>` to end of the last list item in html_list ✅
        - append `</ul>` to the html_list ✅
        - append `</li>` to the html_list ✅
        - decrement 'current_level' by 1 ✅
        - create counter for while loop i = 'current_level' ✅
        - **while loop** while i > 1 ✅
          - if match is equal to list_level[i] match ✅
            - set counter to 1 ✅
          - else
            - append `</ul>` to the html_list to close this list level ✅
            - append `</li>` to the html_list ✅
            - decrement 'current_level' by 1 ✅
            - decrement counter by 1 ✅
      - else, there are no more matches
        - create counter for while loop i = 'current_level' ✅
        - **while loop** i > 0 ✅
          - append `</li>` to the html_list ✅
          - append `</ul>` to the html_list ✅
          - decrement counter by 1 ✅
        - set 'current_level' to zero ✅

``` js
// TEST ONE - PASSED
- item One
  - item Two
    - item Three
      - item Four
    - item Three One
      - item Four One

// TEST TWO - PASSED
- item One
- item Two
  - item Three
  - item Four
    - item Five
  - item Six
- item Seven

// TEST THREE - PASSED
- item One
  - item Two
    - item Three
- item Four
  - item Five
    - item Six
      - item Seven
```

5. Check for paragraphs
Because we are checking for headers and list items first, if neither one was a match, we can savely assume that the line is a paragraph, therefore:
- when we arrive at this point in the code, just add the line to the 'html_list' ✅
- remove the item from 'md_file_lines' ✅
**New paragraph iteration**
Paragraphs needs to be separated by a blank line between them. If there is no blank line then the text is assumed to be part of the same paragraph, even if its anything other like a header or list item.
- create function 'get_paragraphs' that takes parameter 'md_file_lines' to check for all lines ✅
- create variable 'html_p' to hold the paragraph, with initial value of '<p>' ✅
- **WHILE** loop until you find an empty space '' ✅
  - concat current md_file_lines[0] with 'html_p' variable ✅
  - remove the first item in the md_file_lines array ✅
- close the paragraph tag by appending it to the 'html_p' variable, remove any leading spaces ✅
- return a tuple with (True, html_p, md_file_lines) ✅

## Rules

### Header rules

- Number if signs `#` correspond to the heading level
- a single `#` for h1 and six `######` for h6
- there has to be a single space between hash and firt letter of title
- the hash sign can not be preceeded by any empty spacer or character
- Syntax: `# THE TITLE`

### Bold rules

- add 2 asterisks `**WORD**` or underscores `__Many Words__` beofre and after the text
- the symbols can not have any space between them and the text they are targeting
- dont mix symbols together. The start and end tags must be performed with the same symbol.
- Syntax:
`__ONE-WORD__` OR `**ONE-WORD**`
`Using __many words__ is fine`
`It can also be used be**wee**n letters in a word`

### Link rules

- syntax: `[link](url)`
- checking that both the link and urlare in correct format is not the parsers responsibility
- Parser needs to ensure to encode white spaces
- links do not need space before or after

## Paragraphs rules

- use blank lines to separate one or many lines of text
- Do not indent paragraphs with tabs or spaces

### List rules

**Unordered lists**
- lists starts with any of these `- * +` 
```
+ list item
- also a valid list item
* another valid item
```
- The very first list item must have 0 to 4 spaces or single tab to be valid. Otherwise it is treated as a paragraph.
```
- valid list start
      - list started to far out and is treated as a paragraph
```
- to nest a list, the marker for the next level list must appear below the first character of the parent list item.
```
- First item of parent list
  - Nested list
the marker must sit below the first character of previous item
    - First item
      - nested item
```
