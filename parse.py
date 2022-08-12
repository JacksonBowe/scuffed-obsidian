from dataclasses import dataclass, field
import json
import re
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

base = 'http://localhost:9000/#/'
start_path = './src/content'
content = {}



files = []

def path_to_dict(path):
    name = os.path.basename(path)
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path) if not x.startswith("_")]
    else:
        d['type'] = "file"

        # print(name)
        if name.endswith('.md'):

            # Read the file and fix broken markdown links
            with open(path, 'r+') as f:
                lines = f.readlines()
                new_lines = []

                in_container = False
                for line in lines:
                    # line = ''
                    line = line.lstrip(' ')
                    if line.replace(' ', '') == '>':
                        print('Found empty blockquote')
                        continue


                    # x = re.sub(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", '{}'.format(), line)
                    # if line.startswith('#'):
                    #     parts = line.split(' ')
                    #     if parts[0].count('#') == len(parts[0]):
                    #         print('here')
                    #         line = f"{parts[0]} <h{len(parts[0])}>{line[len(parts[0]) + 1:]}</h{len(parts[0])}>"
                    #         print(line)

                    # Convert callouts to admonition containers
                    # > [!info] xxx  --> !!! info xxx

                    # Fix obsidian-export bugs
                    # if in_container:
                        # if line.startswith('>') or line.startswith(' '):
                        #     while line.startswith('>') or line.startswith(' '):
                        #         print('Line starts with garbage, stripping')
                        #         line = line.lstrip(' ')
                        #         line = line.lstrip('>')
                        # else:
                        #     print('Leaving container')
                        #     in_container = False

                    if in_container:
                        if not line.startswith('>'):
                            in_container = False
                            break
                        else:
                            while line.startswith('>') or line.startswith(' '):
                                print('Line starts with garbage, stripping')
                                line = line.lstrip(' ')
                                line = line.lstrip('>')



                    line = line.replace('\[', '[')
                    line = line.replace('\]', ']')
                    callouts = re.findall(r"((\>+) \[(.*?)\]([+-]?) (.*))", line)
                    if callouts:
                        print('Entering container')
                        in_container = True
                        print('line', line)
                        print('callouts', callouts)
                        # in_container = True
                        for callout in callouts:
                            print("line", line)
                            # while line.startswith('>') or line.startswith(' '):
                            #     print('Line starts with garbage, stripping')
                            #     line = line.lstrip(' ')
                            #     line = line.lstrip('>')
                            line = line.replace(f'[{callout[2]}] {callout[4]}', f'!!! {callout[2][1:].lower()} {callout[4]}')
                        print(f'new_line: {line}')


                        # Inside a callout

                    # Convert links
                    links = re.findall(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", line)

                    if not links:
                        new_lines.append(line)
                        continue
                    print('Links found', links)
                    print('old_line', line)
                    for link in links:

                        old_link = "[{}]({}{})".format(link[1], link[2], link[3])
                        new_link = "[{}]({}{})".format(link[1], '#/content/' + link[2].replace('\\', '/'), link[3])
                        line = line.replace(old_link, new_link)
                        print(line)
                        print('old_link', old_link)
                        print('new_link', new_link)

                    print('new_line', line)
                    new_lines.append(line)

                # print('lines', new_lines)
                f.seek(0)
                f.writelines(new_lines)
                f.truncate()



                #   pass

            d['name'] = d['name'].replace('.md', '')
            d['src'] = path.replace('/src', '.').replace('\\', '/')
    return d



# print(json.dumps(path_to_dict(start_path), indent=4))
# print(files)


with open(start_path + '/_map.json', 'w') as f:
    json.dump(path_to_dict(start_path), f, indent=4)
