### Image grabber | Hangman Project
### 12.03.2020

# TODO create an internal method which converts the keyword to the
# specification of the link (bulbapedia takes Capital first format)

import requests
from bs4 import BeautifulSoup


class ImagePull:

    def __init__(self, keyword):
        self.keyword = keyword

    def pkmn_image_pull(keyword):
        # Pulls images of pokemon from Bulbapedia
        URL = f'https://bulbapedia.bulbagarden.net/wiki/{keyword}_(Pok%C3%A9mon)'

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        main_results = soup.find(id='mw-content-text')
        pkmn_data = main_results.find_all('table', class_='roundy')
        pkmn_data_list = []

        for data in pkmn_data:
            pkmn_data_list.append(data)
            if len(pkmn_data_list) > 1:
                break

        # Pulling national national dex number
        nat_dex_num = pkmn_data_list[0].find('a',
                                             href='/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number')
        nat_dex_num = nat_dex_num.text

        # Pulling .png link
        pkmn_png = pkmn_data_list[0].find('img')
        pkmn_png = pkmn_png.get('src')

        pkmn_png_link = f'https:{pkmn_png}'
        print(pkmn_png_link)

        return nat_dex_num, pkmn_png_link


# ImagePull.pkmn_image_pull('Toxtricity')
