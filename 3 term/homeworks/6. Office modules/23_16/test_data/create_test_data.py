import openpyxl


def create_xlsx(filename, *sheets):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    for name, table in sheets:
        ws = wb.create_sheet(name)
        for row in table:
            ws.append(row)

    wb.save(filename)


if __name__ == '__main__':
    shippers = ("shipper",
              (("id", "Name", "Rating", "Address"),
              ("S01", "Доміно", "5", "domino@com.ua"),
              ("S02", "Кондор", "6", "condor@com.ua"),
              ("S03", "Max", "10", "max@com.ua")))

    products = ("product",
                (("id", "Name"),
                ("P01", "Олівець"),
                ("P02", "Ручка кулькова"),
                ("P03", "Папір")))

    prices = ("price",
             (("S_id", "P_id", "Price", "Term"),
             ("S01", "P01", "2,5", "5"),
             ("S01", "P02", "2,4", "6"),
             ("S02", "P01", "2,6", "5"),
             ("S03", "P01", "3,0", "6")))

    create_xlsx("tender.xlsx", shippers, products, prices)
