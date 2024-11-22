import requests
from bs4 import BeautifulSoup
all_cars_url=[]
with open("car_url_from_api.txt","r") as file:
    all_cars_url=file.read().split("\n")
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
i=0
for url in all_cars_url:
    response=requests.get(url=url,headers=header)

