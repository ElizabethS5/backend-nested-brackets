#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reads lines of input.txt and writes whether brackets are nested correctly to output.txt 
"""
__author__ = "ElizabethS5"

import sys


def get_lines(filename):
    """Open and read txt file, return list of lines"""
    f = open(filename, "r")
    lines = f.read().split('\n')
    f.close()
    return lines


def string_to_list(string):
    """Takes a string and puts brackets in list"""
    brackets = []
    copy = string[:]
    while copy:
        if copy[:2] == '(*' or copy[:2] == '*)':
            brackets.append(copy[:2])
            copy = copy[2:]
        else:
            brackets.append(copy[0])
            copy = copy[1:]
    return brackets


def test_bracket_list(bracket_list):
    """If bracket_list passes return 'Yes' else return 'No' and failing index"""
    copy = bracket_list[:]
    greater_less = [0]
    curly = [0]
    square = [0]
    paren = [0]
    aster = [0]
    combo = [greater_less[-1], curly[-1],
             square[-1], paren[-1], aster[-1]]
    position = 1
    while position <= len(bracket_list):
        if copy[0] == '>':
            if len(greater_less) == 1 or greater_less[-1] < max(combo):
                return f'No {position}\n'
            else:
                greater_less.pop()
        elif copy[0] == '}':
            if len(curly) == 1 or curly[-1] < max(combo):
                return f'No {position}\n'
            else:
                curly.pop()
        elif copy[0] == ']':
            if len(square) == 1 or square[-1] < max(combo):
                return f'No {position}\n'
            else:
                square.pop()
        elif copy[0] == ')':
            if len(paren) == 1 or paren[-1] < max(combo):
                return f'No {position}\n'
            else:
                paren.pop()
        elif copy[0] == '*)':
            if len(aster) == 1 or aster[-1] < max(combo):
                return f'No {position}\n'
            else:
                aster.pop()
        elif len(copy) == 1 and copy[0][0] in '<[{(':
            return f'No {position}\n'
        elif copy[0] == '<':
            greater_less.append(position)
        elif copy[0] == '{':
            curly.append(position)
        elif copy[0] == '[':
            square.append(position)
        elif copy[0] == '(':
            paren.append(position)
        elif copy[0] == '(*':
            aster.append(position)
        position += 1
        copy.pop(0)
        combo = [greater_less[-1], curly[-1],
                 square[-1], paren[-1], aster[-1]]
    if max(combo) != 0:
        return f'No {position}\n'
    else:
        return 'Yes\n'


def write_output(string):
    f = open('output.txt', 'w')
    f.write(string)
    f.close()


def main(args):
    """Add your code here"""
    lines_from_input = get_lines('input.txt')
    bracket_lists = [string_to_list(line) for line in lines_from_input]
    output = ''
    for bracket_list in bracket_lists:
        output += test_bracket_list(bracket_list)
    write_output(output)


if __name__ == '__main__':
    main(sys.argv)
