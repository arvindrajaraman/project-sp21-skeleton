from parse import write_input_file, read_input_file, write_output_file
import networkx as nx

G = nx.Graph()

rows = [[1,1], [2,3], [4,6], [7,10], [11,15], [16,21], [22,28]]
paths = [[0,29]]
for row in rows:
    start, end = row
    path = [0]
    path += list(range(start, end + 1))
    path += [29]
    paths.append(path)

for path in paths:
    print(path)

w = 1
for path in paths:
    nx.add_path(G, path, weight=w)
    w += 1

nx.draw(G)
write_input_file(G, '30.in')