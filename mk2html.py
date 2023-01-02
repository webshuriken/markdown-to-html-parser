from os.path import exists
import re


# get the markdown file from /docs folder
def get_md_file(title):
  file_info = False

  # check for popular extension first .md then .markdown
  ext_found = 'md' if exists(f'docs/{title}.md') else 'markdown' if exists(f'docs/{title}.markdown') else False

  # lets read the file or let the user down
  if ext_found != False:
    f = open(f'docs/{title}.{ext_found}')
    file_info = f.read()
    f.close()
  else:
    file_info = 'File Not Found, please make sure it exists'

  # give file back as string
  return file_info

# @description check for header in string
# @params file_line {string}
# @returns {tuple} of two values {bool, string}
def get_header(file_line):
  header = re.match(r'#{1,6}\s', file_line)
  if header:
    header_level = header.end() - 1
    html_header = f'<h{header_level}>{file_line[header.end():]}</h{header_level}>'
    return (True, html_header)
  else:
    return (False, 'Header not found')

# @description check for list items
# @params all_file_lines {list}
# @returns {tuple} of three values {bool, string, updatedFileLines}
def get_lists(all_file_lines):
  # list of dictionaries, each has the list level and match end location
  list_levels = [{"level": 0, "end": 0}]
  current_level = 0
  # will store the list as a combination of html tags and text items
  html_list = []
  # to start a list, the first item must start at 0 spaces or 2 spaces from margin
  match = re.match(r'^\s{,2}[\*-] ', all_file_lines[0])
  # go further, only, if there was a match
  if match:
    html_list.append('<ul>')
    list_levels[0]["end"] = match.end()
    # loop will find all items including the nested ones
    while current_level >= 0:
      # at this point we guaranty a valid list item, so lets append to 'html_list'
      html_list.append(f'<li>{all_file_lines[0][match.end():]}')
      # remove the first file line as its a list item
      all_file_lines.pop(0)
      # lets check for another list item
      match = re.match(r'\s*[\*-] ', all_file_lines[0]) 

      # is current item match same as current list level
      if match and match.end() == list_levels[current_level]["end"]:
        html_list[len(html_list) - 1] += '</li>'
      # is current item match a nested list
      elif match and match.end() == (list_levels[current_level]["end"] + 2):
        html_list.append('<ul>')
        current_level += 1
        list_levels.append({"level": current_level, "end": match.end()})
      # is current item match a level before the current active list level
      elif match and match.end() < list_levels[current_level]["end"]:
        # appending here is to guarante the closure of currently nested list
        html_list[len(html_list) - 1] += '</li>'
        html_list.append('</ul>')
        html_list.append('</li>')
        current_level -= 1
        # close all open lists until we arrive at a valid list level that matches
        i = current_level
        while i >= 0:
          # level found so lets exit loop
          if match.end() == list_levels[i]["end"]:
            i = -1
          else:
            html_list.append('</ul>')
            html_list.append('</li>')
            current_level -= 1
            i -= 1
      else:
        # as there are not more matches, close all nested lists and list items
        i = current_level
        while i >= 0:
          html_list.append('</li>')
          html_list.append('</ul>')
          i -= 1
        current_level = -1

  # prepares the tuple to be returned
  list_found = (False, 'No list here', all_file_lines)
  if len(html_list) >= 1:
    list_found = (True, html_list, all_file_lines)

  return list_found

# @description check for paragraphs
# @params all_file_lines {list}
# @returns {tuple} of three values {bool, string, updatedFileLines}
def get_paragraphs(all_file_lines):
  html_p = '<p>'
  # lets keep going until we find an empty line
  while all_file_lines[0].strip() != '':
    html_p += f'{all_file_lines[0]} '
    all_file_lines.pop(0)
  
  # close the paragraph tag
  html_p = html_p.rstrip() + '</p>'

  return (True, html_p, all_file_lines)

# @description filter text to find boldness and/or links
# @params text {string}
# @returns {string} the string with a ny link of bold tags
def text_filter(text):
  print("FILTERING THE TEXT FOR BOLDNESS")
  get_boldness(text)
  # search for links
  # return an iterable that tells us the location of the text found
  # match = re.finditer(r'\[[^\s]+\]\([^\s]+\)', string)

  # search for boldness
  # match = re.finditer(r'[*_]{2}(\w\s?)+\w[*_]{2}', string)


def get_boldness(text):
  match = re.finditer(r'[*_]{2}(\w\s?)+\w[*_]{2}', text)
  html_bold = ''
  match_end = 0
  # regex iterator, lets loop
  for item in match:
    html_bold += text[match_end:item.start()]
    html_bold += f'<b>{text[item.start():item.end()]}</b>'
    match_end = item.end()
  
  # finalize the bold update
  if (match_end > 0):
    html_bold += text[match_end:len(text)]

  return html_bold



# @description Parser logic taking care of transforming the markdown file to HTML
def init_parser():
  print('\n## Welcome this is Markdown to HTML parser ##\n')
  # global list store the created html tags
  html_list = []

  # lets get the file
  file_name = 'HTML'
  md_file = get_md_file(file_name)
  # split file into lines
  md_file_lines = re.split(r'[\n\r]', md_file)

  while len(md_file_lines) > 0:
    # check for empty item in array
    if md_file_lines[0].strip() == '':
      md_file_lines.pop(0)
      continue

    # lets check for header
    header = get_header(md_file_lines[0])
    if header[0]:
      html_list.append(header[1])
      md_file_lines.pop(0)
      continue

    text_filter(md_file_lines[0])

    # lets check for lists
    list = get_lists(md_file_lines)
    if list[0]:
      html_list.extend(list[1])
      md_file_lines = list[2]
      continue

    # at this point we can assume the line is a paragraph
    paragraph = get_paragraphs(md_file_lines)
    if (paragraph[0]):
      html_list.append(paragraph[1])
      md_file_lines = paragraph[2]
      continue
  
  # show me the final html_list
  print(f'FINAL LIST: \n{html_list}')

init_parser()