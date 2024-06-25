import time

from parsing import send_request, get_links, parse_page
from database import Manager


def main():
    url = "https://www.ultra.kg/catalog/noutbuki-i-pk/noutbuki/?PAGEN_1=4"
    html = send_request(url=url)

    def parse_data(url: str):
        html = send_request(url)
        data = parse_page(html)

        return data

    for url in get_links(html):
        sleep_time = 60
        while True:
            try:
                data = parse_data(url)
            except Exception:
                sleep_time *= 1.5
                time.sleep(sleep_time)
                continue
            else:
                sleep_time = 60

                for key in data.keys():
                    data[key] = data[key].replace('"', "'")

                sql_request = f"""
                INSERT INTO laptop (title, image, price, property)
                VALUES ("{data.get('title')}", "{data.get('image')}", "{data.get('price')}", "{data.get('property')}");
                """
                Manager.insert(sql_request, check_unique = True)
                break



if __name__ == "__main__":
    Manager.create_tables()
    main()
