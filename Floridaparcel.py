from bs4 import BeautifulSoup
import requests
from csv import writer

# Enter Assessor's Parcel Number (APN) < in Florida only >
apn = ["0997-001-056","0997-001-058","1814-000-021","1814-037-028","1814-037-035"]

home ='https://floridaparcels.com/property/52/'

apn_list=[]
for i in apn:
    apn_list.append(home+i)

with open('Parcel Information.csv','w',newline='') as file:
    writer=writer(file)
    header=['Link', 'Property Address','Property city','Owner Name','owner address','owner city','owner zip']

    writer.writerow(header)

    for url in apn_list:

        page=requests.get(url)
        
        # If APN is invalid
        if(page.status_code==404):
            information=['Invalid APN']
            writer.writerow(information)
        
        else:
            soup=BeautifulSoup(page.content,'html.parser')

            address=soup.find('div',{'class':'col-md-8'})
            prop=address.find('h1').text
            prop_city=address.find('h3').text

            owner=soup.find('div',{'class':'sidefloat'})
            owner_name=owner.find('span',{'class':'fn'}).text
            owner_add=owner.find('span',{'class':'street-address'}).text.replace('\n','')
            owner_city=owner.find('span',{'class':'locality'}).text
            owner_zip=owner.find('span',{'class':'postcode'}).text

            information=[url,prop,prop_city,owner_name,owner_add,owner_city,owner_zip]
            writer.writerow(information)



