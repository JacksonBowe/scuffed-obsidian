from dataclasses import dataclass, field
import json
from typing import List, Dict
import os

def is_md(name: str) -> bool:
  return name.endswith('.md')

x = os.listdir('./src/content')

@dataclass
class folder:
  name: str
  # files: Dict[str: str] = field(default_factory=dict)
  sub_folders: List['folder'] = field(default_factory=list)


# for item in x:
#   if is_md(item):
#     print(item)


# print(x)

start_path = './src/content'
content = {}

# for path, dirs, files in os.walk(start_path):
#   path = path.replace('\\', '/')
#   print('path', path)
#   print('dirs', dirs)
#   print('files', files)
#   print()

#   for file in files:
#     content[file]

  # for dir in dirs:
  #   print('dir', dir)
    # content[dir] = {}
  # for filename in files:
  #   content[dir][filename] = os.path.join(path.replace('/src', '.'),filename)
  #   print(os.path.join(path.replace('/src', '.'),filename))


# print(json.dumps(content, indent=4))

def path_to_dict(path):
    d = {'name': os.path.basename(path).replace('.md', '')}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d['src'] = path.replace('/src', '.').replace('\\', '/')
    return d

print(json.dumps(path_to_dict(start_path), indent=4))
