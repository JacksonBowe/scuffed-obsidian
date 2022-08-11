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
						# print(lines)
						# x = re.sub(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", lines)
						# print(x)
						for line in lines:
							# line = ''
							links = re.findall(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", line)
							# x = re.sub(r"\[((.*?)\]\((?!http)(\S*?)(\.md)?(#\S+)?)\)", '{}'.format(), line)
							if not links: continue
							print('Links found', links)
							print('old_line', line)
							for link in links:

								old_link = "[{}]({}{})".format(link[1], link[2], link[3])
								new_link = "[{}]({}{})".format(link[1], '../content/' + link[2].replace('\\', '/'), link[3])
								line = line.replace(old_link, new_link)
								print(line)
								print('old_link', old_link)
								print('new_link', new_link)

							print('new_line', line)

						print('lines', lines)
						f.seek(0)
						f.writelines(lines)
						f.truncate()
						#   pass

					d['name'] = d['name'].replace('.md', '')
					d['src'] = path.replace('/src', '.').replace('\\', '/')
		return d



# print(json.dumps(path_to_dict(start_path), indent=4))
# print(files)


with open(start_path + '/_map.json', 'w') as f:
	json.dump(path_to_dict(start_path), f, indent=4)
