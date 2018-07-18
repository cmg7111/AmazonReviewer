import boto3
import json
import pymysql
import sys

       

curs = conn.cursor()

def main(argv):
	product=argv[1]
	print(product)
	#print(text)
	#print('Calling DetectSentiment')
	#output=json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), \
	#	sort_keys=True, indent=4)
	#print(output)
	#print('End of DetectSentiment\n')

	sql_select="select review, ID from "+product
	curs.execute(sql_select)
	rows=curs.fetchall()
	#write_positive=open('review_positive.txt','w+',encoding='utf8')
	#write_negative=open('review_negative.txt','w+',encoding='utf8')
	i=1
	for line in rows:
		text=line[0]
		ID=line[1]
		sql_update_pos="UPDATE "+product+" SET sentiment='positive' WHERE ID="+str(ID)
		sql_update_neg="UPDATE "+product+" SET sentiment='negative' WHERE ID="+str(ID)
		try:
			data=comprehend.detect_sentiment(Text=text, LanguageCode='en')
		except:
			pass
		if data["SentimentScore"]["Mixed"] > 0.4 :
			pass
		elif data["SentimentScore"]["Negative"] < data["SentimentScore"]["Positive"]:
			curs.execute(sql_update_pos)
			conn.commit()
		#	#write_positive.write(line[0])
		else :
			curs.execute(sql_update_neg)
			conn.commit()
		#	#write_negative.write(line[0])




	#특정 데이터 접근 시 이런방식으로 하면 됨.
	#data=comprehend.detect_sentiment(Text=text, LanguageCode='en')
	#data["SentimentScore"]["Neutral"]=data["SentimentScore"]["Neutral"]
	#print(data)
	#output=json.dumps(data, sort_keys=True, indent=4)

	#write_file=open('review_sentiment.txt','w',encoding='utf8')
	#write_file.write(output)

	#write_file.close()
	#write_positive.close()
	#write_negative.close()
	conn.close()

if __name__=='__main__':
	main(sys.argv)
