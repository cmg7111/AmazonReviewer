<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">


    <title>Amazon Reviewer</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
      
.menubar ul{
background:#376775;
height:50px;
list-style:none;
margin:auto;
padding: 0px;
text-align:center;
}

.menubar li{
padding:0px;
text-align: center;
display:inline-block;
}

.menubar li a{
background: #376775;
color:#ffffff;
display:block;
font-weight:normal;
line-height:50px;
margin:auto;
padding:0px 25px;
text-align:center;
text-decoration:none;
}

.menubar li a:hover, .menubar ul li:hover a{
background:  #0f3e48;
color:#FFFFFF;
text-decoration:none;
}

.menubar li ul{
background: #376775;
display:none; /* 평상시에는 드랍메뉴가 안보이게 하기 */
height:auto;
padding:0px;
margin:0px;
border:0px;
position:absolute;
width:200px;
z-index:200;
/*top:1em;
/*left:0;*/
}

.menubar li:hover ul{
display:block; /* 마우스 커서 올리면 드랍메뉴 보이게 하기 */
}

.menubar li li {
background: #0f3e48;
display:block;
float:none;
margin:0px;
padding:0px;
width:200px;
}

.menubar li:hover li a{
background:none;
}

.menubar li ul a{
display:block;
height:50px;
font-size:12px;
font-style:normal;
margin:0px;
padding:0px 10px 0px 15px;
text-align:left;
}

.menubar li ul a:hover, .menubar li ul li:hover a{
background: #184d5f;
border:0px;
color:#ffffff;
text-decoration:none;
}

    </style>
  </head>

  <body>

     <div class="menubar">
   <ul>
            <li><a href="index.php">Amazon Reviewer</a></li>
       <li><a href="review_crawl2.php">리뷰 검색</a></li>
        <li><a href="review_wordcloud.php">워드 클라우드</a></li>
    </ul>
  </div>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>Amazon Reviewer</h1>
        <p>상품의 리뷰정보를 편하게 확인하세요. <br><br>긍정적 / 부정적 리뷰를 보여줍니다.</p>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
          <h2>리뷰 검색</h2>
          <p>당신이 원하는 상품의 리뷰정보를 보여줍니다.</p>
          <p><a class="btn btn-default" href="review_crawl2.php" role="button">View details &raquo;</a></p>
        </div>
        <div class="col-md-4">
          <h2>워드 클라우드</h2>
          <p>워드 클라우드로 보기좋게 리뷰 확인하기</p>
          <p><a class="btn btn-default" href="review_wordcloud.php" role="button">View details &raquo;</a></p>
       </div>
      </div>

      <hr>

      <footer>
        <p>&copy; 굿모닝아이텍_조승진, 김승호</p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
