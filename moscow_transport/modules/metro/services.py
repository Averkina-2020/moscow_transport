from datetime import datetime

import requests
from bs4 import BeautifulSoup


def parse_mosday():
    parsed_news_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get('https://mosday.ru/news/tags.php?metro', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('center')[1].find_all('tr')[:-1]
    for element in elements:
        image_block, main_block = element.find_all('td')
        image_url = image_block.find('a')
        if image_url:
            image_url = image_url.get('href')
        main_block = main_block.find('font')
        pubdate = datetime.strptime(main_block.find('b').text, '%d.%m.%Y')
        title, text = list(map(lambda x: x.text, main_block.find_all('font')))
        parsed_news = {
            'image_url': image_url,
            'pubdate': pubdate,
            'title': title,
            'pub_text': text
        }
        parsed_news_list.append(parsed_news)
    return parsed_news_list
