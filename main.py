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
"""
def topology_sort(node, adj_list, visited_list, result):
  visited_list[node] = True

  # recurse on all unvisited neighbors 
  for n in adj_list[node]:
    print("AT node: ", node)
    print("Checking neighbor: ", n)
    if visited_list[n] == False:
      topology_sort(n, adj_list, visited_list, result)
  # add current node to stack
  result.append(node)
  print("Done checking node, STACK:", result)
  return result
  
  

def find_compilation_order(dependencies):
  # Write your code here

  adj_list, visited_list = defaultdict(list), defaultdict(bool)
  for dep in dependencies:
    adj_list[dep[1]].append(dep[0])
    if dep[0] not in adj_list:
      adj_list[dep[0]] = []
    visited_list[dep[0]] = False
    visited_list[dep[1]] = False
  result = []
  for node in adj_list:
    if visited_list[node] == False:
      topology_sort(node, adj_list, visited_list, result)
  print(adj_list)
  return result[::-1]

#print(find_compilation_order([["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]))
print(find_compilation_order([["B","A"],["A","B"]]))

"""
# from collections import defaultdict
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u-1].append(v-1)
    def helper(self,u,visited, res):
        print("visiting: ", u)
        for i in self.graph[u]:
            print("Neighbors of", u)
            print("looking at neigh:", i)
            if visited[i] == False:
                self.helper(i, visited, res)
        visited[u] = True
        res.insert(0, u+1)
    def topological_sort(self):
        visited = [False]*self.V
        print(visited)
        res =[]
        for i in reversed(range(self.V)):
            if visited[i] == False:
                self.helper(i, visited, res)
                
        return res
## Driver code
## Driver code  
A = 2
B = [[1, 2], [2, 1]]
graph = Graph(A)
for u, v in B:
    graph.add_edge(u, v)
        
res = graph.topological_sort()
print(res) # [5, 6, 1, 3, 4, 2]