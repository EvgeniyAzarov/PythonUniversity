import re
import os
import sys
from docx import Document
 

def find_replace_docx(filename, find, replace):
    doc = Document(filename)
    for par in doc.paragraphs:
        for run in par.runs:
            run.text = re.sub(find, replace, run.text)

    doc.save(filename)
                
                
if __name__ == '__main__':
    argv = sys.argv[1:]
    find = ""
    replace = ""
    
    m = 0
    for k in range(len(argv)):
        if k >= len(argv):
            break
        
        if argv[k] in ["--find", "-f"]:
            find = argv[k+1]
            m = k+2
             
        if argv[k] in ["--replace", "-r"]:
            replace = argv[k+1]
            m = k+2

    input_dirs = argv[m:] 

    for input_dir in input_dirs:
        for root, dirs, files in os.walk(input_dir):
            for filename in files:
                if filename.endswith('docx'):
                    find_replace_docx(os.path.join(root, filename), find, replace)
                       
