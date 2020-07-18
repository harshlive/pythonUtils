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

get_covid_data()

# Get Product Price Alert

def get_bag_cost_flipkart() :
    res = requests.get('https://www.flipkart.com/little-wish-m2007-30-l-backpack/p/itmb61c886a605c0?pid=BKPFGJCXUXXQGHHF&lid=LSTBKPFGJCXUXXQGHHFKQSCYW&marketplace=FLIPKART&srno=b_1_17&otracker=hp_omu_Minimum%2B10%2525%2BExtra%2BDiscount_2_24.dealCard.OMU_Minimum%2B10%2525%2BExtra%2BDiscount_L0UCC2CB8EMR_17&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Minimum%2B10%2525%2BExtra%2BDiscount_NA_dealCard_cc_2_NA_view-all_17&fm=neo%2Fmerchandising&iid=13485461-873c-4e13-8619-2d3c72936cb4.BKPFGJCXUXXQGHHF.SEARCH&ppt=browse&ppn=browse&ssid=cepjilgri80000001595097548514')
    soup = bs4.BeautifulSoup(res.text,'lxml')
    price = soup.find('div',{'class':'_1vC4OE _3qQ9m1'}).text
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format('Price of bag is {}'.format(price), 'Price Alert') )

get_bag_cost_flipkart()