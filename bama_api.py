import requests
from urllib.parse import urljoin
url="https://bama.ir/cad/api/search"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
car_url_from_api=[]
base_url="https://bama.ir/car"
for i in range(1,2):
    params={"pageIndex":i}
    response=requests.get(url,headers=header,params=params)
    data=response.json()["data"]["ads"]
    for item in data:
        # print(item)#میشه عکس هم ازش دراوورد
        if item:
            car_url=urljoin(base_url,item["detail"]["url"])
            car_url_from_api.append(car_url)
# print(car_url_from_api)
with open("car_url_from_api.txt","w") as file:
    file.write(','.join(car_url_from_api))