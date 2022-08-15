from dataclasses import dataclass, field
import json
import re
from tracemalloc import start
from typing import List, Dict, ClassVar, Tuple
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


@dataclass
class File:
    name: str
    path: str
    content: str
    url: str

    def __init__(self, path) -> None:
        self.path = path.replace('\\', '/')
        self.url = path.replace('/src', '.').replace('\\', '/').replace('..', '#').replace(' ', '%20')
        self.name = self.path.split('/')[-1]
        pass

    def read(self) -> str:
        with open(self.path, 'r') as f:
            return f.read()

@dataclass
class Line:
    value: str
    in_container: ClassVar[bool] = False

    def __init__(self, line: str) -> None:
        self.value = line.lstrip(' ') # obsidian-export puts random ass spaces at the front, get that shit out of here
        self.value =  self.value.replace('\[', '[')
        self.value =  self.value.replace('\]', ']')

        # if self.in_container:
        #     self._trim_start_for_container()

    def _trim_start_for_container(self):
        # print('container line', [self.value])
        if not self.value.startswith('>'):
            # print('breaking')
            self.in_container = False
        else:
            while self.value.startswith('>') or self.value.startswith(' '):
                # print('Line starts with garbage, stripping')
                self.value = self.value.lstrip(' ')
                self.value = self.value.lstrip('>')

    def is_empty_quote(self) -> bool:
        temp = self.value.replace(' ', '')
        temp = temp.replace('\n', '')
        return temp == '>'

    def callouts(self) -> List[tuple]:
        # > [!INFO] Test --> [('> [!INFO] Test', '>', '!INFO', '+', 'Test')]
        return re.findall(r"(([\> ]+) \[(.*?)\]([+-]?) (.*))", self.value)

    def convert_callouts(self: List[Tuple[str, str, str, str, str]]):
        # Convert callouts to admonition containers
        # > [!info] xxx  --> !!! info xxx
        callouts = self.callouts()
        if callouts:
            # print('Entering container')
            Line.in_container = True
            # print('line:', self.value)
            # print('callouts:', callouts)
            # in_container = True
            for callout in callouts:
                self.value = self.value.replace(f'{callout[0]}', f'!!! {callout[2][1:].lower()} {callout[4] or callout[2][1:].lower().capitalize()}')
            # print(f'new_line: {self.value}')
        else:
            if Line.in_container and (self.value == '\n' or self.value is None):
                self.value = '!!! ' + self.value
                Line.in_container = False
            # elif Line.in_container:
                # print('******************************', [self.value])

        if self.in_container: self._trim_start_for_container()

    def links(self):
        return re.findall(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", self.value)

    def convert_links(self):
        links = self.links()
        if not links: return
        for link in links:
            old_link = "[{}]({}{})".format(link[1], link[2], link[3])
            file = next((f for f in files if f.name == link[1] + link[3]), None)   #files[link[1]] # Get the File pertaining to the file name captured in link[1]
            if file is None: return
            new_link = "[{}]({})".format(link[1], file.url)
            self.value = self.value.replace(old_link, new_link)



start_path = './src/content'
content = {}



files = []

def path_to_dict(path):
    # if 'files' not in locals(): files = {}
    name = os.path.basename(path)
    item = {'name': name}
    if os.path.isdir(path):
        item['type'] = "directory"
        item['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path) if not x.startswith(".")]
    else:

        item['type'] = "file"
        item['name'] = item['name'].replace('.md', '')
        item['src'] = path.replace('/src', '.').replace('\\', '/')

        files.append(File(path))

    return item

def parse(file: File):
    print('Parsing file: {}'.format(file.name))
    # Read the file and fix broken markdown links
    with open(file.path, 'r+') as f:
        lines = f.readlines()
        new_lines = []
        for i, line in enumerate(lines):            
            line = Line(line)

            if line.is_empty_quote():
                continue

            line.convert_callouts()
            line.convert_links()
            new_lines.append(line)

            if i == len(lines) - 1 and Line.in_container:
                # If the file ends with a container, need to manually close as there's no next line to do it dynamically
                new_lines.append(Line('!!!'))
                Line.in_container = False

        f.seek(0)
        f.writelines([line.value for line in new_lines])
        f.truncate()
        
        # Read the new content back and save it to the File
        f.seek(0)
        file.content = f.read()



# Read the directory structure and extract all files. Place files into a key:value lookup
with open(start_path + '/.map.json', 'w') as f:
    json.dump(path_to_dict(start_path), f, indent=4)


# print(json.dumps(files, indent=4))

for file in files:
    parse(file)

with open(start_path + '/.search.json', 'w') as s:
    json.dump([{
        'title': file.name,
        'body': file.content,
        'id': idx
    } for idx, file in enumerate(files)], s, indent=4)


    




