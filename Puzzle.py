# Author: Matt Sanders
# Description: Defining a graph algorithm to solve a puzzle.
#              Given the board, a source cell, and a destination
#              cell, the algorithm finds the shortest path to the
#              destination cell from the source cell.

def solve_puzzle(Board, Source, Destination):
    """
    Finds the shortest path on the 'board' from 'source' to
    'destination' utilizing a graph traversal algorithm. It
    returns a list of cells as a 'path'.
    """

    visited = []
    directions = []
    stack = [Source]
    path = [Source]
    choices = []  # List used to find the next cell with the minimum distance from target cell

    while stack:

        curr = stack.pop()  # Holds the current cell

        # If we reach the destination, that cell is added to path and the path is returned
        if curr == Destination:

            if curr not in path:  # Checks if the source is the destination
                path.append(curr)

            # Runs through the path and creates a list of directions (U, D, R, L), based on the steps in the path
            for index in range(len(path) - 1):

                if path[index + 1][0] - path[index][0] > 0:
                    directions.append('D')
                elif path[index + 1][0] - path[index][0] < 0:
                    directions.append('U')

                if path[index + 1][1] - path[index][1] > 0:
                    directions.append('R')
                elif path[index + 1][1] - path[index][1] < 0:
                    directions.append('L')

            return path, directions

        if (curr[0] - 1) >= 0:  # Checks for top edge of the board

            if Board[curr[0] - 1][curr[1]] != '#' and (curr[0] - 1, curr[1]) not in visited:

                # Calculates distance from cell above current cell to target
                dist_1 = abs(Destination[0] - (curr[0] - 1))
                dist_2 = abs(Destination[1] - curr[1])

                choices.append((dist_1 + dist_2, (curr[0] - 1, curr[1])))  # adds tuple of coordinates and distance to target

        if curr[0] + 1 < len(Board):  # Checks for bottom edge of the board

            if Board[curr[0] + 1][curr[1]] != '#' and (curr[0] + 1, curr[1]) not in visited:

                # Calculates distance from cell below current cell to target
                dist_1 = abs(Destination[0] - (curr[0] + 1))
                dist_2 = abs(Destination[1] - curr[1])

                choices.append((dist_1 + dist_2, (curr[0] + 1, curr[1])))

        if (curr[1] - 1) >= 0:  # Checks for left edge of the board

            if Board[curr[0]][curr[1] - 1] != '#' and (curr[0], curr[1] - 1) not in visited:

                # Calculates distance from cell left of current cell to target
                dist_1 = abs(Destination[0] - curr[0])
                dist_2 = abs(Destination[1] - (curr[1] - 1))

                choices.append((dist_1 + dist_2, (curr[0], curr[1] - 1)))

        if curr[1] + 1 < len(Board[0]):  # Checks for right edge of the board

            if Board[curr[0]][curr[1] + 1] != '#' and (curr[0], curr[1] + 1) not in visited:

                # Calculates distance from cell right of current cell to target
                dist_1 = abs(Destination[0] - curr[0])
                dist_2 = abs(Destination[1] - (curr[1] + 1))

                choices.append((dist_1 + dist_2, (curr[0], curr[1] + 1)))

        if not choices:

            if path:

                # Backtracks to find a new path to target
                stack.append(path.pop())
                visited.append(curr)
            else:
                return None
        else:
            stack.append(min(choices)[1])  # Adds the cell with minimum distance to target to stack to look at next
            visited.append(curr)

            if curr not in path:  # Checks for the current cell in the path
                path.append(curr)

            choices.clear()  # Clears the current path choices

    return None
