import bs4, requests

headers = {'User-Agent':'Not_Crawling X)'}

response = requests.get('http://kin.naver.com',headers=headers).text
soup = bs4.BeautifulSoup(response,'html.parser')

ranks = soup.select('#rankingChart > ul > li')

with open('rank.csv','w') as f:
    for rank in ranks:
        num = rank.select_one('span.no').text
        subject = rank.select_one('a.ranking_title').text
        f.write(f'{num}, {subject}\n')
