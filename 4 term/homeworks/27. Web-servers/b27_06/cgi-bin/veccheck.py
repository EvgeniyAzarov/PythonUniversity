#!/usr/bin/python3

import cgi
from string import Template


def good_coords_num(vec : tuple, a, b):
    res = 0
    for x in vec:
        if a <= float(x) <= b:
            res += 1
    return res


if __name__ == '__main__':
    form = cgi.FieldStorage()
    vec = form.getvalue("coord")
    
    a = float(form.getfirst('a'))
    b = float(form.getfirst('b'))

    with open('resultpage.html') as f:
        page = f.read()
    
    res = good_coords_num(vec, a, b)
    page = Template(page).substitute(result=res)

    print("Content-type: text/html charset=utf-8\n")
    print(page)

