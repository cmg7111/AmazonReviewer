import sys
import requests
from bs4 import BeautifulSoup
import math
import pymysql
import urllib.request

#mysql connect
conn = pymysql.connect(host='ec2-18-211-19-90.compute-1.amazonaws.com', user='root', password='root', db='reviewer', charset='utf8')

curs = conn.cursor()


#https://www.amazon.com/product-reviews/B078JGP3MG/ref=cm_cr_othr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1
# ASIN은 아마존 제품코드
#TARGET_URL_BEFORE_ASIN = "https://www.amazon.com/product-reviews/"
TARGET_URL_REST = '/ref=cm_cr_arp_d_viewopt_rvwer?&reviewerType=avp_only_reviews&pageNumber='
#ASIN = 'B078JGP3MG'


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
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    URL = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+product
    print(URL)
    #get_link(URL,headers)

    sql_create_table = "CREATE TABLE IF NOT EXISTS " + product + "(ID int auto_increment primary key, review TEXT NOT NULL, sentiment varchar(10), link TEXT, product_name TEXT)"
    curs.execute(sql_create_table)    
    sql_make_unique = "ALTER TABLE "+product+" ADD UNIQUE (review(1000))"
    curs.execute(sql_make_unique)

    sql_select="select href from link"
    curs.execute(sql_select)
    rows=curs.fetchall()

    #read_file=open('link.txt','r',encoding='utf8')
    #write_file=open('review.txt','w+',encoding='utf8')

    

   # target_URL=TARGET_URL_BEFORE_ASIN + ASIN + TARGET_URL_REST + str(1)
    

    for link in rows:
        url=link[0]
        #링크 저장
        pro_link=link[0].replace("product-review","dp")
        request = requests.session()
        req = request.get(pro_link, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        pro_name=soup.find("span",{"id":"productTitle"})
        pro_name=pro_name.string.strip()
        #print(pro_name)

        num=0
        get_rating(url,headers)
        #print(review_page_num)
        for i in range(1,review_page_num+1):
            current_page_num = i
            url=link[0]
            url=url + TARGET_URL_REST + str(current_page_num)
            #print(url)
            request = requests.session()
            
            req = request.get(url, headers=headers)
            soup = BeautifulSoup(req.content, 'html.parser')
           
            results = soup.findAll("span", {"data-hook": "review-body"})
            for i in results:
                try:
                    num+=1
                    #print(num,i.string)
                   # i.string=i.string.replace("'",r"\'")
                    sql_insert="INSERT INTO "+product+"(review,sentiment,link,product_name) VALUES (%s,NULL,%s,%s)"
                    curs.execute(sql_insert,(i.string,pro_link,pro_name))
                    conn.commit()
                    #write_file.write(i.string+'\n')
                    #print('done')
                except:
                    pass

    sql_trun="truncate table link"
    curs.execute(sql_trun)
    conn.commit()

    #read_file.close()
    #write_file.close()       
    conn.close()

if __name__=='__main__':
    main(sys.argv)
