### Definition grabber | Hangman Project
### 12.03.2020

# TODO: Add an internal method which converts the word to the specification
# of the link (all lower case)

# A class which calls a dictionary API and returns the definition of the selected word
import re
import requests
from bs4 import BeautifulSoup


class Definition:

    def __init__(self, word):
        self.word = word

    def definition_return(word):  # dictionary.com
        URL = f'https://www.dictionary.com/browse/{word}?s=t'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='base-pw')

        word_data = results.find_all('section',
                                     class_='css-rv7a0y-WordContentContainer e1hj943x0')

        for data in word_data:
            # Each job_elem is a new BeautifulSoup object.
            # You can use the same methods on it as you did before.
            POS_pronunciation = data.find('h3',
                                          class_='css-1qrq6c8-BlockTitleContainer e1hk9ate3')
            definition = data.find('div',
                                   class_='css-l5qngi-OrderedContentListContainer e1hk9ate0')

            if None in (POS_pronunciation, definition):
                continue  # Might not be perfect. NEEDS TESTING

            POS_text = POS_pronunciation.text.strip()
            rx = re.compile('([: .*.])')
            POS_text = rx.sub(' ', POS_text)
            POS_list = POS_text.split(';')

            definition_text = definition.text.strip()
            definition_list = definition_text.split(';')

            for item in POS_list:
                print(POS_list.index(item))
                print(item)
            print(len(POS_list))
            print('++++++++++++++++++++++')
            for item in definition_list:
                print(item)
            print(len(definition_list))
