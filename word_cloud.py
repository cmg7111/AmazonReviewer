import sys
import pathlib
import os
import pymysql
import matplotlib.pyplot as plt
from wordcloud import WordCloud


conn = pymysql.connect(host='ec2-18-211-19-90.compute-1.amazonaws.com', user='root', password='root', db='reviewer', charset='utf8')

curs = conn.cursor()

def main(argv):
	#pathlib.Path('/'+argv[1]).mkdir(parents=True, exist_ok=True)
	comm="mkdir -p "+argv[1]
	os.system(comm)

	file_name_pos=argv[1]+'_positive.png'
	file_name_neg=argv[1]+'_negative.png'
	print(file_name_pos)
	

	sql_select="select * from "+argv[1]
	curs.execute(sql_select)
	rows=curs.fetchall()
	text_pos=''
	text_neg=''
	for line in rows:
		if line[2]=='positive' :
			text_pos=text_pos+line[1]+'\n'
		elif line[2]=='negative' :
			text_neg=text_neg+line[1]+'\n'


	#read_positive=open('review_positive.txt','r',encoding='utf8')
	#read_negative=open('review_negative.txt','r',encoding='utf8')

	#text_pos=read_positive.read()
	#text_neg=read_negative.read()

	wordcloud_pos = WordCloud(width=800, height=400,).generate(text_pos)
	wordcloud_neg = WordCloud(width=800, height=400,).generate(text_neg)
	
	wordcloud_pos.to_file(file_name_pos)
	wordcloud_neg.to_file(file_name_neg)
	
	path_pos="/var/www/html/"+argv[1]+"/"+file_name_pos
	path_neg="/var/www/html/"+argv[1]+"/"+file_name_neg
	
	comm="mv "+file_name_pos+" /var/www/html/"+argv[1]
	os.system(comm)
	comm="mv "+file_name_neg+" /var/www/html/"+argv[1]
	os.system(comm)
	conn.close()

if __name__=='__main__':
	main(sys.argv)