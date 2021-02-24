#!/usr/bin/python3

import cgi
from string import Template

COORD_FORM = '<td><input name="coord" type="number" size="10"/></td>\n'

if __name__ == '__main__':
    form = cgi.FieldStorage()
    n = int(form.getfirst("n"))
    
    with open("vecform.html") as f:
        page = f.read()

    page = Template(page).substitute(coords=COORD_FORM*n)
    
    print("Content-type: text/html charset=utf-8\n")
    print(page)
