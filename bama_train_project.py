import requests
from bs4 import BeautifulSoup
import json

all_cars_url = []
all_info = []
with open("car_url_from_api.txt", "r") as file:
    all_cars_url = file.read().split("\n")
z = 0
for page_url in all_cars_url:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    car_dict = dict()
    response = requests.get(url=page_url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    picture_url = soup.select_one(".bama-carousel-holder__image-holder.single-image-holder img")
    if picture_url:
        picture_url = picture_url["src"]
    else:
        picture_url = " "
    title = soup.find("h1", class_="bama-ad-detail-title__title")

    car_model = soup.find_all("span", class_="bama-ad-detail-title__subtitle")
    year = car_model[0].text.strip()
    model = car_model[1].text.strip()
    location = soup.find("span", class_="address-text")
    price = soup.find("span", class_="bama-ad-detail-price__price-text")
    if price.text.strip() == "توافقی":
        price = price.text.strip()
    else:
        price = float(price.text.strip().replace(",", ""))
    car_detail_item = soup.select(".bama-vehicle-detail-with-icon__detail-holder span")
    car_detail = [item.text for item in car_detail_item]
    car_value_item = soup.select(".bama-vehicle-detail-with-icon__detail-holder p")
    car_value = [value.text for value in car_value_item]
    car_info_dict = {car_detail[i]: car_value[i] for i in range(len(car_detail))}

    description = soup.select_one(".desc p")
    if description:
        description = description.text.strip()
    else:
        description = "None"

    technical_detail_item = soup.select(".bama-vehicle-detail-with-link__row-title")
    technical_item = [item.text.strip() for item in technical_detail_item]
    technical_detail_value = soup.select(".bama-vehicle-detail-with-link__row-text")
    technical_value = [value.text.strip() for value in technical_detail_value]
    technical_info_dict = {technical_item[i]: technical_value[i] for i in range(len(technical_item))}

    car_dict.update(
        {"نام": title.text.strip(),
         "لینک عکس": picture_url,
         "سال ساخت": year,
         "مدل": model,
         "آدرس": location.text.strip(),
         "قیمت": price,
         "توضیحات": description
         })
    car_dict.update(car_info_dict)
    car_dict.update(technical_info_dict)
    all_info.append(car_dict)
    print("-" * 40)
    print(f"{title.text} تمام شد, ")
    z += 1

with open("car_information.json", "w", encoding="utf-8") as car_file:
    json.dump(all_info, car_file, ensure_ascii=False, indent=3)
print(z)