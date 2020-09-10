import urllib.request

from bs4 import BeautifulSoup


def main(date):
    list_total = []  # 해당날짜 전체 기사의 url list
    list_title = []  # 전체 기사 title
    list_uploadDate = []  # 전체 기사 날짜
    list_body = []  # 전체 기사 본문

    totalPageIdx = 1000  # pageIdx 탐색 개수
    # 해당 날짜의 전체 기사 링크들 저장
    for idx in range(1, totalPageIdx):
        url = "https://news.sbs.co.kr/news/newsflash.do?pageDate=" + \
            date+"&pageIdx="+str(idx)
        sourcecode = urllib.request.urlopen(
            url).read()
        soup = BeautifulSoup(sourcecode, "html.parser", from_encoding='ANSI')
        list_temp = []
        for href in soup.find("div", class_="w_news_list").find_all("li"):
            list_temp.append("https://news.sbs.co.kr"+href.find("a")["href"])

        # 노드가 더이상 없으면 종료
        if(len(list_temp) == 0):
            break
        for i in list_temp:
            list_total.append(i)

    # 기사 1개씩 탐색하며 list 에 추가
    for url in list_total:
        sourcecode = urllib.request.urlopen(
            url).read()
        soup = BeautifulSoup(sourcecode, "html.parser", from_encoding='ANSI')
        list_title.append(
            soup.find(id="vmNewsTitle").get_text().replace('\n', ''))
        list_body.append(
            soup.find("div", class_="text_area").get_text().replace('\n', ''))
        list_uploadDate.append(
            soup.find("span", class_="date").get_text().replace('\n', '')[2:12])

    print(list_title)
    print(list_uploadDate)
    print(list_body)


if __name__ == "__main__":
    main("20200909")
