from dataclasses import dataclass, field
import json
import re
from typing import List, ClassVar, Tuple
import os

# --------------------------------------------------------------------------- #
#                                 General Utils                               #
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
#                                Document Classes                             #
# --------------------------------------------------------------------------- #
@dataclass
class File:
    name: str
    path: str
    content: str
    url: str
    links: list = field(default_factory=list)

    def __init__(self, path) -> None:
        self.path = path.replace('\\', '/')
        self.url = path.replace('/src', '.').replace('\\', '/').replace('..', '#').replace(' ', '%20')
        self.name = self.path.split('/')[-1]
        self.links = []
        pass

    def build_links(self):
        print('Building links')
        links = re.findall(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", self.content)
        for link in links:
            self.links.append(link[1] + '.' + link[4].split('.')[-1])

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

    def _trim_start_for_container(self):
        if not self.value.startswith('>'):
            self.in_container = False
        else:
            while self.value.startswith('>') or self.value.startswith(' '):
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
            Line.in_container = True
            for callout in callouts:
                self.value = self.value.replace(f'{callout[0]}', f'!!! {callout[2][1:].lower()} {callout[4] or callout[2][1:].lower().capitalize()}')
        else:
            if Line.in_container and (self.value == '\n' or self.value is None):
                self.value = '!!! ' + self.value
                Line.in_container = False

        if self.in_container: self._trim_start_for_container()

    def links(self):
        return re.findall(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", self.value)

    def convert_links(self):
        links = self.links()
        # print(links)
        if not links: return
        for link in links:
            old_link = "[{}]({}{})".format(link[1], link[2], link[3])
            file = next((f for f in FILES if f.name == link[1] + link[3]), None)   #FILES[link[1]] # Get the File pertaining to the file name captured in link[1]
            if file is None: return
            new_link = "[{}]({})".format(link[1], file.url)
            self.value = self.value.replace(old_link, new_link)




# --------------------------------------------------------------------------- #
#                                Worker Functions                             #
# --------------------------------------------------------------------------- #

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

        FILES.append(File(path))

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


        file.build_links() # TODO need to convert file names into their index representation





start_path = './src/content'
content = {}

FILES = []

if __name__ == "__main__":
    # Read the directory structure and extract all files. Place files into a key:value lookup
    with open(start_path + '/.map.json', 'w') as f:
        json.dump(path_to_dict(start_path), f, indent=4)


    # print(json.dumps(files, indent=4))

    for file in FILES:
        parse(file)

    with open(start_path + '/.files.json', 'w') as s:
        res = [{
            'title': file.name,
            'body': file.content,
            'src': file.url,
            'id': idx,
            'links': file.links
        } for idx, file in enumerate(FILES)]
        
        json.dump(res, s, indent=4)







