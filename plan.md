# Parser Plan

Lets plan out the steps to create the parser.

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

- add line items with numbers followed by periods
- list needs to start with 1
- the other numbers in lists dont have to be in numberial order
- for lists within lists:
  - new list needs to be indented 4 spaces or 1 tab more from parent list
```
- item one
    - list within
      - another list level deep
```
