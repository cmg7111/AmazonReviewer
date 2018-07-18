    <?php
    error_reporting(E_ALL);
    ini_set("display_errors", 1);
   
    ini_set('max_execution_time', 100); 
    $item=$_POST['keyword'];
    echo $item;


    #상위 6개 제품 링크 크롤링
    $item=str_replace(" ","+",$item);
    echo $item;

    $tmp = shell_exec("python3 crawl_amazon_link.py $item");
    echo $tmp;

    #각 제품별 3개 리뷰 페이지 크롤링
    $item=str_replace("+","_",$item);
    $tmp = shell_exec("python3 crawl_amazon_review2.py $item");
    echo $tmp;
    
    #리뷰별 긍/부정 판단
    $item=str_replace(" ","_",$item);
    $tmp = exec("python3 sentiment.py $item");
    echo $tmp;

    #판단된 긍/부정 워드클라우드 작성
    $item=str_replace(" ","_",$item);
    $tmp = shell_exec("python3 word_cloud.py $item");
    echo $tmp;

    header("location: http://ec2-18-211-19-90.compute-1.amazonaws.com/review_crawl2.php");
    ?>
