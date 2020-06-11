
def earliest_ancestor(ancestors, starting_node):
    # use BFS, right now im using a traversal.
    # traversal will go through enite map and map it out
    # a search will look through graph and will stop once it finds the item you're looking for.


    # does starting node have parents?
    # do does parents have parents?
    # increment generation
    prev_generations = 0
    
    parents = []

    for i in ancestors:
        if starting_node == i[1]:
            parents.append(i[0]) # add parents of starting node to list

    for i in ancestors:
        for j in parents:
            if j == i[1]:
                parents.append(i[0])
                # delete j from parents
                parents.
    # for each node:
        #if node not visited:
        #traverse from that node
        #increment counter
    


    def bft(self, starting_vertex):
        '''
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        
        queue = deque()
        queue.append(starting_vertex)
        visited = set()

        while len(queue) != 0:
            current = queue.popleft()
            print(current)
            visited.add(current)
            current_neighbors = self.get_neighbors(current)

            for neighbor in current_neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)'''
#
'''
For example, in this diagram and the sample input,
3 is a child of 1 and 2, and 5 is a child of 4:

 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9

Write a function that, given the dataset and the ID 
of an individual in the dataset, returns their earliest 
known ancestor – the one at the farthest distance from the 
input individual. If there is more than one ancestor tied 
for "earliest", return the one with the lowest numeric ID. 
If the input individual has no parents, the function should 
return -1.

Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10

  path [[10, 1], [1,3], [3,6]]
'''