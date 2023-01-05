# Parser Plan

Lets plan out the steps to create the parser.

## Issues

**List items**:
- Add the `+` as a valid list item marker ✅ (SOLVED)
- follow rule 2 of unordered lists. First list item marker can only be 0, 2, 4 spaces from the left margin. ✅(SOLVED)
- follow rule 3 of unordered lists. Nested lists are create by placing the list marker 2, 4 spaces away from the list marker on the line above. ✅ (SOLVED)
- handle tab usage. Currently the parser can not handle the use of tabs. ✅ (SOLVED)

**boldness**
- Missed the fact that I have to remove the markers which indicated the texts is to be bold.  ✅ (SOLVED)

**paragraphs**
- Paragraphs are meant to be separated using a space between two lines. Currently if the user presses 'Enter' to carry on below the current line, without any space between them, it treats it as a separate paragraph which is not the case.
The regex separating the document lines into a list needs looking into. ✅ (SOLVED)
- When there is a list item that does not follow the rules, the parser moves on to the paragraph checker as it is now treated as a paragraph, however if the next list item is correctly placed but it sites on the line below the list item which failed, it is also treated as a paragraph. This is an unwanted effect and goes against the rules. If the rules are followed properly the described event should create a paragraph for the list item that was not indented properly and then create a list with any number of items for the line that has the list item that was indented properly.
- It seems paragraphs are not removing any left trailing white space. These need removing.

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
The list did not take into account how to properly check when spaces or Tabs are being used. The use of a function to hide the intricacies of checking for Tabs or spaces.
- create a function named 'valid_list_marker' ✅
  - the function will take parameters: 
  - `match = regex_match, list_levels = list_levels, current_level, list_type = start | current | previous | nested` ✅
  - create var 'marker_is_valid' and set to false. It will be return by the function after checks ✅
  - count the number of tabs in matched text and store in 'matched_tabs' ✅
  - first lets check for the basic list marker, level 0. ✅
    - if matched_tabs == 1 or match.end is 2, 4 or 6 then its is a valid list start ✅
    - marker_is_valid = True ✅
  - lets check if next item is on the same level as previous one ✅
    - first check for the list_type == 'current ✅
    - and does the previous level number of tabs match the number of tabs found in this level? ✅
    - or does the previous level match.end match the current match.end ✅
    - marker_is_valid = True ✅
  - now check if we are looking at a nested list ✅
    - first check that we are looking for nested lists ✅
    - and that the previous number of tabs + 1 matches the current number of found tabs ✅
    - or that the list levels, current level, last location + 2 matches the current found location ✅
    - or that the list levels, current level, last location + 4 matches the current found location ✅
  - final check is for when the matched list marker sits closer to the left margin than the above list item. This will close the nested lists above.
    - check the list_type to match 'previous' and ✅
      - level 0 tabs property is not equals to -1 and ✅
      - number of tabs in current match is less than the current level tabs number ✅
      - or current match end is less than current level end ✅
        - use a loop to check the previous levels 'end' value not including the current level value. A match indicates the current item belongs to a lower level list. ✅
    
  - return 'marker_is_valid' ✅

**Note:** during this iteration of the planning it became apparent that the list of dictionaries that keeps track of the current level, last match location and tabs matched needed to be updated. The tabs count starts at zero and as such it was clashing with the checker for item on the same level. To fix it I created a variable to hold a boolean indicating if Tabs are being used to create this list or not and with it find out the number of Tabs used to indent the item or store -1 to indicate the absence of Tabs in this list.

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

5. filter text for boldness or links
- create function 'text_filter' takes in a single parameter 'text' ✅
- create variable 'html_text' to store the final filtered text ✅
- first check for bold text
- Boldness:
  - create function 'get_boldness' that takes a string 'text' ✅
  - use regex to find all matches to iterate over and store in 'match' variable ✅
  - create variable 'html_bold' to store updated text ✅
  - create variable to store the last match location 'match_end' ✅
  - **loop** regex returned an iterable item, loop through it ✅
    - in 'html_bold' ✅
      - concat any text from 'match_end' up to the start of the bold match ✅
      - concat `<b>` with any text from start of bold match to the end ✅
      - 'match_end' var is equal the end location of the current matched text ✅
  - if var 'match_end' is more than 0, a match was found: ✅
    - concat any leftover text from the end of last match to the length of the text ✅
  - return the converted text 'html_bold' ✅
- Links:
They need to be completely replaced. Grabbing the link and text for link
from: `[text_for_link](link)`
to: `<a href="link">text_for_link</a>`
  - create function 'get_links' to take arguments 'text' ✅
  - regex the links and store them result in 'match' var  ✅
  - create variable 'html_link' to store updated text ✅
  - create 'match_end' variable to store the end location of the current match ✅
  - **loop** use regex iterable from matched links ✅
    - in 'html_link' 
      - extract link text and store in 'link_text' ✅
      - extract link url and store in 'link_url' ✅
      - concat any text from 'match_end' up to the start of the link match ✅
      - 'match_end' variable to store the end location of the currently matched link ✅
    - if variable 'match_end' is more than 0 ✅
      - concat leftover text from the end of last matched link to the end of the text ✅
    - return 'html_link' ✅

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
