import requests
from bs4 import BeautifulSoup as bs
from market import Market


class Crawling:
    def __init__(self):
        pass
    
    @staticmethod
    def create_new_session():
        # 새로운 Session 생성
        with requests.Session() as session:
            return session

    def read_total_data(self):
        """
        get total data from source url
        source url list:
            1. http://seoulmarket.org/search/ --> base data
        """

        url = "http://seoulmarket.org/search/"
        req = self.create_new_session().get(url)
        if req.status_code == "200" and req.ok is True:
            print(req.text)
            return req.text
        else:
            print("Connection Failed! bb")
            return False

    def parsing_market_total_data(self, html):
        """
        get market object from total data
        """
        soup = bs(html, 'html.parser')
        name = soup.select("#kboard-avatar-list > div.kboard-list > div.mk_list_content > div.mk_list_content_box > "
                           + "div.mk_item.mk-name > div")



        pass


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