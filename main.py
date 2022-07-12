from bs4 import BeautifulSoup
import requests
from csv import writer
import hyperlink

city="amsterdam/"
home_page="https://www.pararius.com/apartments/" + city
total_pages=10

url_list=[home_page] 

for i in range(1,total_pages):
    url_list.append(home_page+"page-"+str(i))
    
with open('Properties.csv','w',newline='') as file:
    writer = writer(file)
    header = ['Title','Location','Price','Area','Room','Brokerage Firm','Brokerage Firm link']
    writer.writerow(header)
    for url in url_list:
        page =requests.get(url)

        soup = BeautifulSoup(page.content,'html.parser')
        lists =soup.find_all('section',class_='listing-search-item')

        for list in lists:
                title = list.find('a',{'class':"listing-search-item__link--title"}).text.replace('\n','')
                location = list.find('div',{'class':'listing-search-item__location'}).text.replace('\n','')
                price = list.find('div',{ 'class':'listing-search-item__price'}).text.replace('\n','')
                area = list.find('li',{'class':'illustrated-features__item--surface-area'}).text.replace('\n','')
                room = list.find('li',{ 'class':'illustrated-features__item--number-of-rooms'}).text.replace('\n','')
                broker= list.find('div',{'class': 'listing-search-item__info'})
                link=broker.find('a',{'class': 'listing-search-item__link'})
                
                broker_link="https://www.pararius.com"+link['href']
                info=[title,location,price,area,room,broker.text.replace('\n',''),hyperlink.URL.from_text(broker_link)]
                writer.writerow(info)

