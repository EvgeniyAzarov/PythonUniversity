import re

VAR = r"\b[a-zA-Z_][\w_]*"
ASSIGNMENT = r"^\s*"+VAR+r"\s?=.*"

if __name__ == '__main__':
    with open("test_file.py", "r", encoding="utf-8") as inp:
        text = inp.read()

    variables = {}

    for match in re.finditer(ASSIGNMENT, text, flags=re.MULTILINE):
        value = match.group().split('=')[1]
        variable = re.search(VAR, match.group()).group()

        for var in re.finditer(VAR, value):
            if not var.group() in variables.keys():
                print("Variable {} is used but not defined before".format(var.group()))
                break
        else:
            variables[variable] = value


    print(variables) 
