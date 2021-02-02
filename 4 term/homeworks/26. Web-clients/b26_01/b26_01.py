import openpyxl
import requests
from bs4 import BeautifulSoup

outfile="weather.xlsx"
url = "https://sinoptik.ua/погода-"

if __name__ == '__main__':
    city = input("Город: ")
    #city = "киев"
    full_url = url + city

    response = requests.get(full_url)
    
    soup = BeautifulSoup(response.text, 'lxml')

    #with open("out.html", "w") as out:
    #    print(soup.prettify(), file=out)

    result_row = []
    result_row.append(city)
    
    curday = soup.find('div', class_="main loaded")
    day = curday.find('p', class_="date").contents
    month = curday.find('p', class_="month").contents

    date = " ".join(day + month)
    result_row.append(date)

    for i in range(2, 7):
        day = soup.find('div', class_="main", id=f"bd{i}")
        min_ = day.find('div', class_="min").text
        max_ = day.find('div', class_="max").text

        result_row.append(min_)
        result_row.append(max_)

    wb = openpyxl.load_workbook(filename=outfile) 
    sheet = wb.active
    sheet.append(result_row)
    wb.save(filename=outfile)

    

        
