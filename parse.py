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

            old_link = "[{}]({}{})".format(link[1], link[2], link[3])
            new_link = "[{}]({}{})".format(link[1], '#/content/' + link[2].replace('\\', '/'), link[3]) # .replace('../', '')
            self.value = self.value.replace(old_link, new_link)
            # print('old_link', old_link)
            # print('new_link', new_link)

        # print('new_line', self.value)



base = 'http://localhost:9000/#/'
start_path = './src/content'
content = {}



files = {}

def path_to_dict(path):
    name = os.path.basename(path)
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path) if not x.startswith("_")]
    else:
        d['type'] = "file"
        d['name'] = d['name'].replace('.md', '')
        d['src'] = path.replace('/src', '.').replace('\\', '/')
        

        print('path', path, 'name', d['name'],'src', d['src'])
        # print(name)
        if name.endswith('.md'):
            files[d['name']] = d['src']
            # Read the file and fix broken markdown links
            # with open(path, 'r+') as f:
            #     lines = f.readlines()
            #     new_lines = []
            #     # print('origional', [line for line in lines])
            #     for line in lines:

            #         # print('yo', [line])
            #         line = Line(line) # obsidian-eport puts random ass spaces at the front, get that shit out of here

            #         if line.is_empty_quote():
            #             print('Found empty blockquote')
            #             continue
            #         # print('here', [line.value])

            #         line.convert_callouts()
            #         line.convert_links()
            #         new_lines.append(line)

            #     # print('result', [line.value for line in new_lines])
            #     f.seek(0)
            #     f.writelines([line.value for line in new_lines])
            #     f.truncate()



                #   pass

    
    return d



with open(start_path + '/_map.json', 'w') as f:
    json.dump(path_to_dict(start_path), f, indent=4)
    print(json.dumps(files, indent=4))
