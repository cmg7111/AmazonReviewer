    <?php
    error_reporting(E_ALL);
    ini_set("display_errors", 1);
   
    ini_set('max_execution_time', 100); 
    $item=$_POST['keyword'];
    echo $item;


    #���� 6�� ��ǰ ��ũ ũ�Ѹ�
    $item=str_replace(" ","+",$item);
    echo $item;

    $tmp = shell_exec("python3 crawl_amazon_link.py $item");
    echo $tmp;

    #�� ��ǰ�� 3�� ���� ������ ũ�Ѹ�
    $item=str_replace("+","_",$item);
    $tmp = shell_exec("python3 crawl_amazon_review2.py $item");
    echo $tmp;
    
    #���亰 ��/���� �Ǵ�
    $item=str_replace(" ","_",$item);
    $tmp = exec("python3 sentiment.py $item");
    echo $tmp;

    #�Ǵܵ� ��/���� ����Ŭ���� �ۼ�
    $item=str_replace(" ","_",$item);
    $tmp = shell_exec("python3 word_cloud.py $item");
    echo $tmp;

    header("location: http://ec2-18-211-19-90.compute-1.amazonaws.com/review_crawl2.php");
    ?>
