The program MazeSolver uses a breadth-first search algorithm to solve Maze o' Mine.

The program must know the starting coordinates. This can be inferred from making steps and seeing
the updated location of your avatar.

The function commandCenter takes the map and paths as its parameters. The map is a representation of the maze, with
visited, unvisited, and wall tiles marked accordingly. In the beginning, all tiles are unvisited.
The function takes the first path in its queue, removes it from the path array, and visits each unvisited tile adjacent to it.

If the adjacent tile is not a wall, then the tile is marked visited, and a path is created to that tile, and that path is
added to the array.

This method is used so that when a path hits a dead-end, it is removed, but when it hits a fork, the program can handle
following any number of paths.

When a path hits the winning tile, the program will print "Winner" and the connection is closed.