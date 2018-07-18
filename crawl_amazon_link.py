import sys
import requests
from bs4 import BeautifulSoup
import math
import pymysql

TARGET_URL_BASIS = 'https://www.amazon.com/s/'
TARGET_URL_KEYWORD = 'ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
# https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=nike+zoomwinflo
TARGET_URL_REST= '&sort=review-rank'

conn = pymysql.connect(host='ec2-18-211-19-90.compute-1.amazonaws.com', user='root', password='root', db='reviewer', charset='utf8', port=3306)

curs = conn.cursor()


def get_URL(URL,headers):
    #print(URL)
    request = requests.session()
    req = request.get(URL, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    i = 0
    #print(soup)
    for result in soup.findAll('a', {'class':'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}):     
        url = result.get('href')
        url=link_repalce(url)
        sql_insert="INSERT INTO link (href) VALUES (%s)"
        curs.execute(sql_insert,(url))
        conn.commit()
        #output_file.write(url+'\n')
        i += 1
        if i == 6:
            break
    i = 0
    for result in soup.findAll('a', {'class':'a-link-normal s-access-detail-page s-overflow-ellipsis s-color-twister-title-link a-text-normal'}):        
        url = result.get('href')
        url=link_repalce(url)
        sql_insert="INSERT INTO link (href) VALUES (%s)"
        curs.execute(sql_insert,(url))
        conn.commit()
        #output_file.write(url+'\n')
        i += 1
        if i == 6:
            break

    i = 0
    for result in soup.findAll('a', {'class':'a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'}):     
        url = result.get('href')
        url=link_repalce(url)
        sql_insert="INSERT INTO link (href) VALUES (%s)"
        curs.execute(sql_insert,(url))
        conn.commit()
        #output_file.write(url+'\n')
        i += 1
        if i == 6:
            break
    
def link_repalce(txt):
    text=txt.replace("dp","product-review")
    if text[0:3]=='/gp' :
            text='https://www.amazon.com'+text
    #print(text)
    return text


def main(argv):
    if len(argv) != 2:
        print("[키워드]")
        return
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        
    keyword = argv[1]
    #print(keyword)
            
    #write_file = open('link.txt', 'a+', encoding = 'utf8')
   
    URL = TARGET_URL_BASIS + TARGET_URL_KEYWORD + str(keyword) + TARGET_URL_REST
    #print(URL)
    get_URL(URL,headers)

    #write_file.close()
    conn.close()

if __name__=='__main__':
    main(sys.argv)
