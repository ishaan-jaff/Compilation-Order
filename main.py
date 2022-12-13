"""
Statement
There are a total of n
n
 classes labeled with the English alphabet (A
A
, B
B
, C
C
, and so on). Some classes are dependent on other classes for compilation. For example, if class B
B
 extends class A
A
, then B
B
 has a dependency on A
A
. Therefore, A
A
 must be compiled before B
B
.

Given a list of the dependency pairs, find the order in which the classes should be compiled.

input: [["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]
- build adj list and visited list python
"""

from collections import defaultdict

def find_compilation_order(dependencies):
  # pre processing
  # build adj list, visited list, in degree
  adj_list, in_degree, visited = defaultdict(list), defaultdict(int), defaultdict(bool)
  for dep in dependencies:
    start, end = dep[1], dep[0]
    adj_list[start].append(end)
    in_degree[end] +=1
    if start not in in_degree:
      in_degree[start] = 0
  print(adj_list, in_degree, visited)
  # traverse graph, topo sort
  result = []
  q = []
  # init q 
  for node in in_degree:
    if in_degree[node] == 0:
      q.append(node)
  while q:
    elem = q.pop(0)
    visited[elem] = True
    result.append(elem)
    # parse neighbors
    for n in adj_list[elem]:
      in_degree[n] -=1
      if visited[n] == False and in_degree[n]==0:
        q.append(n) # parse neighbors with 0 dependencies
  return result

print(find_compilation_order([["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]))

print(find_compilation_order([["E","A"],["B","A"],["C","E"],["D","E"],["B","D"]]))

print(find_compilation_order([["A","B"],["B","A"]]))