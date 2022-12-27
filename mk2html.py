from os.path import exists


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


def init_parser():
  file_name = 'HTML'
  print('\n## Welcome this is Markdown to HTML parser ##\n')
  print(f'.. Lets get the file: {file_name}')
  f = get_md_file(file_name)

  print('.. Here is what the file says:')
  print(f'.. {f}')

  print('')

init_parser()