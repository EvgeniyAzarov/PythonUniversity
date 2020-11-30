import openpyxl

if __name__ == '__main__':
    #file_name = input("Input excel file: ")
    file_name = "test.xlsx"
    wb = openpyxl.load_workbook(filename=file_name)

    sheets = wb.sheetnames
    print(sheets)

    for sheet in reversed(sheets):
        sh = wb[sheet]
        empty = True
        for row in sh.rows:
            for cell in row:
                if cell is not None:
                    empty = False
                    break
            break
        
        if empty and len(wb.worksheets) > 1:
            del wb[sheet]
            print("Deleted: {}".format(sheet))
    
    wb.save(file_name)
            
