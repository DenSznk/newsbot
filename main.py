from bs4 import BeautifulSoup
import requests
import json
from url_header import url, header

new_dict = {}


def get_content():
    r = requests.get(url=url, headers=header)
    soup = BeautifulSoup(r.text, 'lxml')
    posts = soup.find_all('div', class_='cell')
    for post in posts:
        post_title = post.find('div', class_='text_blk').text.strip()
        post_url = post.find('a')
        url_post = post_url.get('href')
        post_time = post.find('div').get('data-full_datetime')
        post_id = post.find('div').get('data-id')
        new_dict[post_id] = {
            'post_title': post_title,
            'url_post': url_post,
            'post_time': post_time
        }

    with open("new_dict.json", 'w') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)


def main():
    get_content()


if __name__ == '__main__':
    main()
