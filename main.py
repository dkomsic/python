from random import random
from bs4 import BeautifulSoup
import requests
import csv
import time

source = requests.get('https://www.index.hr/oglasi/osobni-automobili/gid/27?pojam=&sortby=1&elementsNum=100&cijenaod=0&cijenado=10000000&tipoglasa=1&markavozila=11005&pojamZup=-2&attr_Int_179=2020&attr_Int_1190=2021&attr_Int_470=&attr_Int_910=&attr_bit_motor=&attr_bit_473=&attr_Int_1172=&attr_Int_1335=&attr_Int_359=&attr_Int_1192=&attr_bit_klima=&attr_bit_mjenjac=&attr_bit_brzina=&attr_bit_vrsta_pogona=&vezani_na=179-1190_470-910_1172-1335_359-1192').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary'])

for car in soup.find_all('a', class_='result'):
    carDetails = car['href']
    carLink = requests.get(carDetails).text
    carSoup = BeautifulSoup(carLink, 'lxml')
    carPrice = carSoup.find('div', class_='price').contents[1].contents[0]
    carName = carSoup.find('div', class_='likeH1').contents[0]
    csv_writer.writerow([carName, carPrice])
    print(carPrice, carName)
    time.sleep(12)


csv_file.close()