import math

def print_twice(bruce):
    print(bruce)
    print(bruce)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = "Bing tiddle "
line2 = "tiddle bing."

cat_twice(line1, line2)