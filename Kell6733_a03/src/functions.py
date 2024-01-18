"""
-------------------------------------------------------
[assignment 3, Functions]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

# Constants
OPERATORS = "+-*/"


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list = []
    stack_to_array(source, list)

    array_to_stack(source, list)

    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    string = string.lower()
    string = string.replace(" ", "")

    stack = Stack()
    for i in string:
        stack.push(i)

    palindrome = True

    while not stack.is_empty():
        if stack.pop() != string[0]:
            palindrome = False
        string = string[1:]

    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    stack = Stack()
    elements = string.split()
    for e in elements:
        if e not in OPERATORS:
            stack.push(e)
        else:
            top = float(stack.pop())
            second = float(stack.pop())
            if e == "+":
                stack.push(second+top)
            elif e == "-":
                stack.push(second-top)
            elif e == "*":
                stack.push(second*top)
            else:
                stack.push(second/top)
    answer = stack.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = []

    position = "Start"
    choice = maze[position]
    if "X" in choice:
        path.append("X")

    stack = Stack()
    while "X" not in choice:
        for i in choice:
            stack.push(i)
        position = stack.pop()
        if maze[position] != []:
            path.append(position)
        choice = maze[position]
        if "X" in choice:
            path.append("X")

    return path
