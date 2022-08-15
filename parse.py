from dataclasses import dataclass, field
import json
import re
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
    url: str

    def __init__(self, path) -> None:
        self.path = path.replace('\\', '/')
        self.url = path.replace('/src', '.').replace('\\', '/').replace('..', '#').replace(' ', '%20')
        self.name = self.path.split('/')[-1]
        pass

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
            if Line.in_container and self.value == '\n':
                self.value = '!!! ' + self.value
                Line.in_container = False

        if self.in_container: self._trim_start_for_container()

    def links(self):
        return re.findall(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", self.value)

    def convert_links(self):
        links = self.links()
        if not links: return
        # print('Links found', links)
        # print('old_line', self.value)
        for link in links:
            # print('found', link)
            old_link = "[{}]({}{})".format(link[1], link[2], link[3])
            file = files[link[1]] # Get the File pertaining to the file name captured in link[1]
            new_link = "[{}]({})".format(link[1], file.url) # .replace('../', '')
            self.value = self.value.replace(old_link, new_link)
            # print('old_link', old_link)
            # print('new_link', new_link)



start_path = './src/content'
content = {}



files = {}

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

        files[item['name']] = File(path)

    return item

def parse(file: File):
    print('Parsing file: {}'.format(file.name))
    # Read the file and fix broken markdown links
    with open(file.path, 'r+') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            line = Line(line)

            if line.is_empty_quote():
                # print('Found empty blockquote')
                continue

            line.convert_callouts()
            line.convert_links()
            new_lines.append(line)

        f.seek(0)
        f.writelines([line.value for line in new_lines])
        f.truncate()


# Read the directory structure and extract all files. Place files into a key:value lookup
with open(start_path + '/.map.json', 'w') as f:
    json.dump(path_to_dict(start_path), f, indent=4)


# print(json.dumps(files, indent=4))

for (file_name, paths) in files.items():
    parse(paths)



