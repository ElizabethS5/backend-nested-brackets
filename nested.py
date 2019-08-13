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


def test_bracket_list(bracket_list):
    """If bracket_list passes return 'Yes' else return 'No' and failing position"""
    copy = bracket_list[:]
    all_list = []
    rights = '>}])'
    lefts = '<{[('
    position = 1
    while copy:
        if copy[0][-1] in rights:
            if len(all_list) == 0:
                return f"NO {position}\n"
            elif copy[0] == '>' and all_list[-1] == '<':
                all_list.pop()
            elif copy[0] == ']' and all_list[-1] == '[':
                all_list.pop()
            elif copy[0] == '}' and all_list[-1] == '{':
                all_list.pop()
            elif copy[0] == ')' and all_list[-1] == '(':
                all_list.pop()
            elif copy[0] == '*)' and all_list[-1] == '(*':
                all_list.pop()
            else:
                return f"NO {position}\n"
        elif copy[0][0] in lefts:
            if len(copy) == 1:
                return f"NO {position}"
            else:
                all_list.append(copy[0])
        position += 1
        copy.pop(0)
    if len(all_list) != 0:
        return f'NO {position}\n'
    else:
        return 'YES\n'


def write_output(string):
    """Write string to file"""
    f = open('output.txt', 'w')
    f.write(string)
    f.close()


def main(args):
    """Use input.txt to write output.txt"""
    lines_from_input = get_lines('input.txt')
    bracket_lists = [string_to_list(line) for line in lines_from_input]
    output = ''
    for bracket_list in bracket_lists:
        output += test_bracket_list(bracket_list)
    write_output(output)


if __name__ == '__main__':
    main(sys.argv)
