"""
    author: Zituo Yan
    description: Classify Triangle
    date: 29/01/2020
"""


def is_number(str):
    try:
        if str=='NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False


def classify_triangle(a, b, c):
    """
        classify which the triangle belongs to
    """
    if not (is_number(str(a)) and is_number(str(b)) and is_number(str(c))):
        return "invalid input"
    edges = sorted([a, b, c])
    if edges[2] >= edges[0] + edges[1]:
        return "not a triangle!"
    elif len(set(edges)) == 1:
        return "equilateral triangle!"
    elif len(set(edges)) == 2:
        if round(edges[2]**2) == round(edges[1]**2 + edges[0]**2):
            return "isosceles right triangle!"
        else:
            return "isosceles triangle!"
    elif round(edges[2]**2) == round(edges[1]**2 + edges[0]**2):
        return "right triangle!"
    else:
        return "scalene triangle!"
