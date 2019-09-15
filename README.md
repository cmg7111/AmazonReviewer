# 아마존 쇼핑 리뷰 긍/부정 분석 （2018.07.02~2018.08.03）
* * *
#### Co-op Project (Summer 2018) / 산학협력 프로젝트 with GIT(Goodmorning Information Technology Co. Ltd.)

### Amazon Review Data Analyze  
#### 역할
1） 백엔드 서버 구성（AWS EC2, MySQL, Apache）  
2） 아마존 사이트 리뷰 크롤링（Python Beautifulsoup4）  
3） 프론트엔드 제작（HTML5, PHP, JS）  

아마존(http://amazon.com) 의 특정 제품 리뷰데이터 검색 및 AWS Comprehend API를 활용하여 리뷰의 긍 / 부정을 평가하고, 해당 리뷰의 분류 및 워드클라우드를 작성하여 보여주는 웹 서비스

#### 긍 부정 분석(AWS Comprehend API)
1) 검색하고자 하는 제품명 입력 후 '리뷰 검색' 버튼 클릭
2) 해당 제품 리뷰데이터 데이터베이스 저장 후 AWS Comprehend API를 통하여 긍/부정 분류 후 데이터베이스 분류
3) 제품 목록에서 조회를 원하는 제품을 선택 후 '이전 리뷰 보기' 버튼 클릭
4) 결과 출력

![](https://cmg7111.github.io/proj_image1.PNG)

#### 워드클라우드 작성(WordCloud 패키지)
1) 리뷰 검색 후, 제품목록에서 조회를 원하는 제품 선택 후 '워드클라우드 보기' 버튼 클릭
2) 해당 제품의 긍/부정 리뷰데이터를 exec함수를 통해 워드클라우드 작성 python 파일 실행
3) 결과 출력

![](https://cmg7111.github.io/proj_image2.PNG)


