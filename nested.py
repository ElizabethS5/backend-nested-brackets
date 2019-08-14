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
    """Takes a string and puts characters in a list"""
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


def test_line_list(bracket_list):
    """If bracket_list passes return 'Yes' else return 'No' and failing position"""
    copy = bracket_list[:]
    stack = []
    closing_brackets = '>}])'
    opening_brackets = '<{[('
    position = 1
    while copy:
        if copy[0][-1] in closing_brackets:
            if len(stack) == 0:
                return f"NO {position}"
            elif copy[0] == '>' and stack[-1] == '<':
                stack.pop()
            elif copy[0] == ']' and stack[-1] == '[':
                stack.pop()
            elif copy[0] == '}' and stack[-1] == '{':
                stack.pop()
            elif copy[0] == ')' and stack[-1] == '(':
                stack.pop()
            elif copy[0] == '*)' and stack[-1] == '(*':
                stack.pop()
            else:
                return f"NO {position}"
        elif copy[0][0] in opening_brackets:
            if len(copy) == 1:
                return f"NO {position}"
            else:
                stack.append(copy[0])
        position += 1
        copy.pop(0)
    if len(stack) != 0:
        return f'NO {position}'
    else:
        return 'YES'


def write_output(string):
    """Write string to file"""
    f = open('output.txt', 'w')
    f.write(string)
    f.close()


def main(args):
    """Use input.txt to write output.txt"""
    lines_from_input = get_lines('input.txt')
    line_lists = [string_to_list(line) for line in lines_from_input]
    output = '\n'.join([test_line_list(line_list)
                        for line_list in line_lists])
    write_output(output)


if __name__ == '__main__':
    main(sys.argv)
