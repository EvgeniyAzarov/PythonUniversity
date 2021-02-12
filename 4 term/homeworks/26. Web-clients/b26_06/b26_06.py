import requests
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from string import Template

#URL = "https://www.timeanddate.com/worldclock/ukraine/kyiv"
URL = "https://www.worldtimeserver.com/current_time_in_UA.aspx"
CHANGE_DATE = "sudo date -s \"$date\""

if __name__ == '__main__':
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    with open("out.html", "w") as outfile:
        print(soup.prettify, file=outfile)

    time = soup.find("span", id="theTime").text.split()
    day = soup.find("h4").contents
    date_str = " ".join(day + time) 
    
    right_date = datetime.strptime(date_str, " %A, %B %d, %Y %I:%M:%S %p")
    cur_date = datetime.today()
    delta = cur_date - right_date
    
    print("Current time: ", cur_date)
    print("Right time: ", right_date)
    print("Time delta: ", delta)
    
    if delta > timedelta(seconds=10):
        command = Template(CHANGE_DATE).substitute({"date": right_date})
        os.system(command)
        print("Time successfully synchronized")
    else:
        print("Time already synchronized")    
