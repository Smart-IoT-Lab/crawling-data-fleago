import requests
from bs4 import BeautifulSoup as bs
import re
from pyprnt import prnt
from market import Market
from firebase import firebase


class Crawling:
    def __init__(self):
        pass
    
    @staticmethod
    def create_new_session():
        """
        create new session
        :return: session
        """
        with requests.Session() as session:
            return session

    @staticmethod
    def remove_html_tags(data):
        """
        remove tag between data
        :param data: data whtch in plain data, html tag, black(space, tag)
        :return: plain data
        """
        p = re.compile(r'<.*?>')
        return p.sub('', data).strip()

    def read_total_data(self):
        """
        get total data from source url
        source url list:
            1. http://seoulmarket.org/search/ --> base data
        """

        url = "http://seoulmarket.org/search/"
        req = self.create_new_session().get(url)
        if req.status_code == 200:
            # print(req.text)
            return req.text
        else:
            print("Connection Failed! bb")
            return False

    def parsing_market_total_data(self, html):
        """
        get market object from total data
        """
        market_list = []
        soup = bs(html, 'html.parser')

        names = [self.remove_html_tags(str(x)) for x in soup.find_all("div", {"class": "kboard-avatar-cut-strings"})]
        districts = [self.remove_html_tags(str(x)) for x in soup.find_all("div", {"class": "mk_item mk-location"})[1:]]
        locations = [self.remove_html_tags(str(x)) for x in soup.find_all("div", {"class": "mk_item mk-place"})[1:]]
        event_types = [self.remove_html_tags(str(x)).split() for x in soup.find_all("div", {"class": "mk_item mk-type"})[1:]]
        introductions = [self.remove_html_tags(str(x)) for x in soup.find_all("div", {"class": "mk_item mk-intro"})[1:]]
        page_urls = [self.remove_html_tags(str(x)) for x in soup.find_all("div", {"class": "mk_item mk-link"})[1:]]

        for idx, (name, district, location, event_type, introduction, page_url) in enumerate(zip(names, districts, locations, event_types, introductions, page_urls), start=1):
            market = Market(name, district, location, event_type, introduction, page_url)
            market_list.append(market)


def main():
        craw = Crawling()
        html = craw.read_total_data()
        if html is False:
            print("Connection Failed!")
            return
        else:
            craw.parsing_market_total_data(html)


if __name__ == "__main__":
    main()