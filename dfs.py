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

def topology_sort(node, adj_list, visited_list, result, in_degree):
  visited_list[node] = True

  # recurse on all unvisited neighbors 
  for n in adj_list[node]:
    print("AT node: ", node)
    print("Checking neighbor: ", n)
    in_degree[n] -=1
    result.append(node)
    if visited_list[n] == False and in_degree[n] == 0:
      topology_sort(n, adj_list, visited_list, result, in_degree)
  # add current node to stack
 
  print("Done checking node, STACK:", result)
  return result
  
  

def find_compilation_order(dependencies):
  # Write your code here

  adj_list, visited_list, in_degree = defaultdict(list), defaultdict(bool), defaultdict(int)
  for dep in dependencies:
    adj_list[dep[1]].append(dep[0])
    if dep[0] not in adj_list:
      adj_list[dep[0]] = []
    visited_list[dep[0]] = False
    visited_list[dep[1]] = False
    in_degree[dep[0]] +=1
    if dep[1] not in in_degree:
      in_degree[dep[1]] = 0
  print(in_degree)
  result = []
  for node in adj_list:
    if visited_list[node] == False:
      topology_sort(node, adj_list, visited_list, result, in_degree)
  print(adj_list)
  return result[::-1]

print(find_compilation_order([["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]))
#print(find_compilation_order([["B","A"],["A","B"]]))

