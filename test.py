import sys
import requests
from bs4 import BeautifulSoup
import math
import pymysql

#mysql connect
conn = pymysql.connect(host='ec2-35-169-85-70.compute-1.amazonaws.com', user='root', password='root', db='reviewer', charset='utf8')

curs = conn.cursor()

# ASIN은 아마존 제품코드
#TARGET_URL_BEFORE_ASIN = "https://www.amazon.com/product-reviews/"
TARGET_URL_REST = '/ref=cm_cr_arp_d_viewopt_rvwer?pageNumber='
TARGET_URL_REST2 ='&reviewerType=avp_only_reviews'
#ASIN = 'B078JGP3MG'

TARGET_URL_BASIS1 = 'https://www.amazon.com/s/'
TARGET_URL_PAGE_NUM1 = '&page='
TARGET_URL_KEYWORD1 = 'ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='

def link_repalce(txt):
    text=txt.replace("dp","product-review")
    print(text)
    return text

def get_URL(URL,headers):
    print(URL)
    request = requests.session()
    req = request.get(URL, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    i = 0
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


#rating(별점) 추출 및 총 리뷰 갯수 추출
def get_rating(URL,headers):
    try:
        request = requests.session()
        req = request.get(URL, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        rate = soup.findAll("span", {"data-hook": "rating-out-of-text"})
        review = soup.findAll("span", {"data-hook": "total-review-count"})
        #각 제품의 rating(별점) 정보
        global rating
        rating=rate[0].string[0:3]
        #print(rating)

        global review_page_num
        review_page_num=review[0].string.replace(",","")
        review_page_num=math.ceil(int(review_page_num)/10)
        if review_page_num>=3:
            review_page_num=3
        #print(review_page_num)
    except:
        pass

def main(argv):
    product=argv[1] 

    sql_create_table = "CREATE TABLE IF NOT EXISTS " + product + "(ID int auto_increment primary key, review TEXT , sentiment varchar(10))"
    curs.execute(sql_create_table)    
    sql_make_unique = "ALTER TABLE "+product+" ADD UNIQUE (review(1000))"
    curs.execute(sql_make_unique)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    URL = TARGET_URL_BASIS1 + TARGET_URL_KEYWORD1 + str(keyword)
    get_URL(URL,headers)

    sql_select="select href from link"
    curs.execute(sql_select)
    rows=curs.fetchall()

    #read_file=open('link.txt','r',encoding='utf8')
    #write_file=open('review.txt','w+',encoding='utf8')

   

   # target_URL=TARGET_URL_BEFORE_ASIN + ASIN + TARGET_URL_REST + str(1)
    print('z')

    for link in rows:
        url=link[0]
        get_rating(url,headers)
        num=0
        #print(review_page_num)
        for i in range(1,review_page_num+1):
            current_page_num = i
            url=link[0]
            url=url + TARGET_URL_REST + str(current_page_num) + TARGET_URL_REST2
            print(url)
            request = requests.session()
            
            req = request.get(url, headers=headers)
            soup = BeautifulSoup(req.content, 'html.parser')
           
            results = soup.findAll("span", {"data-hook": "review-body"})
            for i in results:
                try:
                    num+=1
                    print(num,i.string)
                   # i.string=i.string.replace("'",r"\'")
                    sql_insert="INSERT INTO "+product+"(review,sentiment) VALUES (%s,NULL)"
                    curs.execute(sql_insert,(i.string))
                    conn.commit()
                    #write_file.write(i.string+'\n')
                    #print('done')
                except:
                    pass

    #sql_trun="truncate table link"
    #curs.execute(sql_trun)
    conn.commit()

    #read_file.close()
    #write_file.close()       
    conn.close()

if __name__=='__main__':
    main(sys.argv)
