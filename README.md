# Puzzle_algorithm


This algorithm solves a puzzle using a greedy approach combined with a graph traversal algorithm. It runs in polynomial time. It finds the shortest path from a given starting cell to a goal cell, if a path exists. Otherwise it tells the user that there is no path to get to the goal from the starting position. If the first path it tries ends up in a dead end, the algorithm backtracks to the next available closest direction to the end cell. 

The algorithm returns a tuple that has the vertex path and the directional path that it took to get to the goal cell. If the goal cannot be reached, it returns none.

format of the puzzle:

                  - - - - -
                  - # - - -
                  # - # - -          
 
 Anywhere there is a dash, that's an open cell; anywhere there is a '#', that is a 'wall' and that cell cannot bet walked through to get to the goal.
