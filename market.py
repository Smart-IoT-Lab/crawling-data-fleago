class Market:
    # 시장 이름, 지역구, 장소, 행사유형, 소개, 홈페이지(url)
    # 지역구 : string type, 서울시의 구 행정구역
    # 장소 : string type, '/' 구분 - 여러 장소에서 진행되는 행사
    # 행사 유형 : list type, 6가지 - 예술, 마을, 먹거리, 체험, 공연, 나눔
    #
    # todo list
    #   1. add profile image

    def __init__(self, name, district, location, event_type , introduction, page_url):
        self.name = name
        self.district = district
        self.location = location
        self.event_type = event_type
        self.introduction = introduction
        self.page_url = page_url

    def __str__(self):
        return self.name

    def print_information_of_market(self):
        print("시장 이름: {}".format(self.name))
        print("지역구: {}".format(self.district))
        print("장소: {}".format(self.location))
        print("행사 유형: {}".format(self.event_type))
        print("소개: {}".format(self.introduction))
        print("홈페이지 주소:{}".format(self.page_url))

