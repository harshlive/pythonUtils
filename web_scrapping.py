import requests
import bs4
import os

#Gets COVID daily cases count and creates Mac Notification

def get_covid_data() :
    res = requests.get('https://www.worldometers.info/coronavirus/country/india/')
    soup = bs4.BeautifulSoup(res.text,'lxml')
    new_cases = soup.find('li',{'class':'news_li'}).strong.text.split()[0]
    new_deceased = list( soup.find('li',{'class':'news_li'}).strong.next_siblings)[1].text.split()[0]   
    print(new_cases, new_deceased)
    notify('Covid Alert !!!','New Cases Reported Today : {} \nDeaths reported Today : {}'.format(new_cases,new_deceased))

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title) )

# notify("Title", "Heres an alert")
get_covid_data()