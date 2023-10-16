"""Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
   there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?"""
import math

def compute_paths(n):
    """
    Let the path through an n x n grid be a string of length 2*n:
    For instance for a 3 x 3 grid, the path could be "dddrrr" where d and r represent down and right turns respectively.

    The permutations of such path is n!, however this assumes there are no repeated elements.

    So, we must divide by the (number of repeated letters)!

    In this case, there are 2 cases of repeated letters (d and r) and each one is repeated n times.

    So, we divide by n! (for d) and n! (for n)

    Args:
        n (integer): the side length of the grid n x n

    Returns:
        numPaths: the number of possible paths through an n x n grid
    """
    numPaths = math.factorial(n*2)/(math.factorial(n)*math.factorial(n))
    return int(numPaths)

print(compute_paths(20))