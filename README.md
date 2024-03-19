# Graph-Traversals
My implementation of Graph Traversals.

## Depth First Search - DFS
* Proceeds in a "straight line", and comes back when it finds a leaf or a node whose neighbours have all been visited.
* Uses a stack[^1] to store unvisited vertices.  
* Visits sub-tree by sub-tree.
* Optimal to search for nodes that may be far away from a given root.
### DFS pseudo-code (recursive):
```
<- receives
<-+ incremented/appended to

!initialize:
  result[]  <-  empty list
  visited[] <-  list of Falses the same size as the number of vertices in the graph
  v         <-  "root" vertex, starting point

!begin:
  visited[v] <- True
  result <-+ v
  
  for every vertex adjacent to v:
    if such vertex has not been visited:
      DFS(vertex)

return result
```
## Breadth First Search - BFS
* Proceeds visiting nodes level by level.
* Uses a queue to store unvisited vertices.
* Optimal to search for nodes that may be closer to a given root.
* ### BFS pseudo-code (iterative):

```
<- receives
<-+ incremented/appended to

!initialize:
  result[]  <-  empty list
  visited[] <-  list of Falses the same size as the number of vertices in the graph
  queue[]   <-  empty list
  v         <-  "root" vertex, starting point

!begin:
  visited[v] <-  True
  queue      <-+ v

  while queue not empty:
    v <- queue.pop()
    result <-+ v

    for every vertex adjacent to v:
      if such vertex has not been visited:
        queue <-+ vertex
        visited[vertex] <- True

return result
```
## Sample execution
<p align="center">
<img width ="500" height = "500" src ="https://github.com/GabrielPazinatto/Graph-Traversals/assets/133925406/698533c8-6620-4565-abff-1fb3bddfd0ce">
</p>

For the graph above [^2] the order in which the vertices are visited is:
* DFS: [0, 1, 6, 7, 3, 2, 4, 5]
* BFS: [0, 1, 2, 6, 3, 4, 7, 5]

<sub>Input text file for this graph available in repo files.</sub>

[^1]: A stack is not actually necessary in an implementation, but the concept remains.
[^2]: Image generated in https://csacademy.com/app/graph_editor/
