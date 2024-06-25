from typing import Generator
import time

import requests
from bs4 import BeautifulSoup

def send_request(url: str) -> str:
    # GET, POST, PUT, PATCH, DELETE

    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text

    raise Exception(response.status_code)


def get_links(html: str) -> Generator[str, str, str]:

    soup = BeautifulSoup(html, "html.parser")
    catalog = soup.find("div", {"id": "catalogSection"})
    items: list[BeautifulSoup] = catalog.find_all("div", {"class": "item"})

    for item in items:
        domen = "https://www.ultra.kg"
        url = item.find("div", {"class": "productColImage"}).find("a").get("href")
        link = domen + url
        yield link


def parse_page(html: str) -> dict[str, str]:
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("div", {"id": "main"}).find("h1", {"class": "changeName"}).text

    container = soup.find("div", {"id": "tableContainer"})

    domen = "https://www.ultra.kg"
    image = container.find("div", {"id": "pictureContainer"}).find("a").get("href")
    image_link = domen + image

    properties: list[BeautifulSoup] = container.find("div", {"class": "propertyList"}).find_all("div", {"class": "propertyTable"})
    property_text = ""

    for property in properties:
        name = property.find("div", {"class": "propertyName"}).text.strip()
        value = property.find("div", {"class": "propertyValue"}).text.strip()
        property_text += f"{name}: {value}\n"

    price = container.find("div", {"id": "elementTools"}).find("span", {"class": "priceContainer"}).text

    return {"title": title, "image": image_link, "price": price, "property": property_text}
