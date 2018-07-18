﻿<?php
$conn = mysqli_connect('ec2-18-211-19-90.compute-1.amazonaws.com', 'root','root','reviewer');
mysqli_set_charset($conn, 'utf8');
$product=$_POST['keyword'];
?>

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
     <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- font awesome -->
    <link rel="stylesheet" href="css/font-awesome.min.css" media="screen" title="no title" charset="utf-8">
    <!-- Custom style -->
    <link rel="stylesheet" href="css/style.css" media="screen" title="no title" charset="utf-8">

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

.ui-input-text{
    margin: .4em 0;
}
.ui-mini {
font-size: 13px;
}

.loader {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #376775; /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

thead tr{position: absolute; margin-top:-45px}

    </style>
  </head>


  <body>

    <div class="menubar">
      <ul>
        <li><a href="">Amazon Reviewer</a></li>
        <li><a href="">리뷰 검색</a></li>
        <li><a href="">워드 클라우드</a></li>
      </ul>
    </div>
      

    <!-- Main jumbotron for a primary marketing message or call to action -->
     <div class="jumbotron">
      <div class="container">
        <h1>리뷰를 검색 중입니다</h1>
        <p>사용자의 환경에 따라 30초~1분 가량 걸릴 수 있습니다.<br>잠시만 기다려주세요.
      </div>
    </div>

     <div class="container"  align="center">
      <!-- Example row of columns -->
      <div class="row">
	<form method="post" action="crawl_review_link.php" id="myform">
		<input type="hidden" name="keyword" value="<?php echo $product; ?>"/>
	</form>
       <article class="container">
        <div class="col-md-6 col-md-offset-3">
<br><br><br><br>
	<div class="loader">
	</div>    
<br><br><br><br> 
        </div>
      </div>
	
      <hr>

      <footer align="left">
        <p>&copy; 굿모닝아이텍_조승진, 김승호</p>
      </footer>
    </div> 	
      </div>
  <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>



<script>
	$("#myform").submit();
	var product;
	function search_click(){
		alert("리뷰 검색 중.. 확인을 누르고 잠시 기다려 주세요.");
	}
	
	function set_product(){
		alert("선택된 제품의 워드 클라우드를 출력합니다.");
		window.location.reload();
	}
		
</script>
