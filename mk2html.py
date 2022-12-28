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

def init_parser():
  print('\n## Welcome this is Markdown to HTML parser ##\n')
  # global list store the created html tags
  html_list = []

  # lets get the file
  file_name = 'HTML'
  md_file = get_md_file(file_name)
  # split file into lines
  md_file_lines = re.split(r'[\n\r]+', md_file)

  while len(md_file_lines) > 0:
    # lets check for header
    header = get_header(md_file_lines[0])
    if header[0]:
      html_list.append(header[1])
      md_file_lines.pop(0)
      continue

    # TODO: temp line. will remove an item from the list on each iteration
    # stopping an infinite loop
    md_file_lines.pop(0)

init_parser()