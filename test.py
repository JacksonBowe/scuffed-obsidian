lines = ["### yo"]


for line in lines:
    if line.startswith('#'):
        parts = line.split(' ')
        if parts[0].count('#') == len(parts[0]):
            print('here')
            line = f"{parts[0]} <h{len(parts[0])}>{line[len(parts[0]) + 1:]}</h{len(parts[0])}>"
            print(line)


